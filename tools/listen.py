#!/usr/bin/env python3
"""Listen to our audio through qwen-omni (cheapest omni on the gateway).

  listen.py cut <start> <dur> <name>          cut a review clip from the mix
  listen.py ask <name> ["question"]           upload (once) + ask the model
  listen.py ask-all                            run the standard flaw prompt on all clips

Uses R2 (presigned GET, 24h) for the audio URL the gateway fetches.
"""
import base64
import datetime
import hashlib
import hmac
import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.error
import urllib.parse
import warnings
warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV = "/home/box/.config/powpowpow/r2.env"
AENV = "/home/box/repos/characters/audition/.env"
MIX = os.path.join(ROOT, "build/dual_reading/vatula_full_dual_reading.mp3")
CLIPS = "/tmp/opencode/listen"
MODEL = "qwen3.8-omni-flash"

FLAW_PROMPT = (
    "Listen for FLOW only. Does this audio excerpt flow nicely? "
    "Report ONLY obviously jarring moments, each with timestamp mm:ss within the clip:\n"
    "- speech interrupted or a pause that feels dead/wrong;\n"
    "- a jarring jump in volume or room sound;\n"
    "- anything that briefly confuses the ear.\n"
    "Ignore minor word-boundary or excerpt-edge details. "
    "One short bullet per jarring moment; end with FLOWS if it all reads naturally."
)


def env(path):
    out = {}
    for line in open(path):
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def ask(name, question):
    a = env(AENV)
    clip = os.path.join(CLIPS, f"{name}.mp3")
    b64 = base64.b64encode(open(clip, "rb").read()).decode()
    q = question or FLAW_PROMPT
    # provider 1: Gemini free tier ($0) — cheapest, key in audition/.env
    gkey = a.get("GEMINI_API_KEY", "").strip()
    if gkey:
        for gmodel in ("gemini-3.1-flash-lite", "gemini-2.5-flash-lite"):
            payload = {"contents": [{"parts": [
                {"inline_data": {"mime_type": "audio/mpeg", "data": b64}},
                {"text": q}]}]}
            url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
                   f"{gmodel}:generateContent?key={gkey}")
            try:
                out = json.load(urllib.request.urlopen(
                    urllib.request.Request(url, data=json.dumps(payload).encode(),
                                           headers={"Content-Type": "application/json"}),
                    timeout=300))
                return out["candidates"][0]["content"]["parts"][0]["text"]
            except Exception as ex:
                print(f"[listen] gemini {gmodel} failed: {ex}; trying next", file=sys.stderr)
    # provider 2: qwen omni on the Alibaba gateway (fallback, ~$0.0005/pass)
    payload = {"model": MODEL, "modalities": ["text"],
               "reasoning_effort": a.get("LISTEN_THINK", "low"),
               "messages": [{"role": "user", "content": [
                   {"type": "input_audio",
                    "input_audio": {"data": "data:audio/mpeg;base64," + b64, "format": "mp3"}},
                   {"type": "text", "text": q}]}]}
    req = urllib.request.Request(a["DASHSCOPE_BASE_URL"].strip() + "/chat/completions",
                                 data=json.dumps(payload).encode(),
                                 headers={"Authorization": "Bearer " + a["DASHSCOPE_API_KEY"].strip(),
                                          "Content-Type": "application/json"})
    try:
        out = json.load(urllib.request.urlopen(req, timeout=300))
        return out["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        return f"HTTP {e.code}: {e.read().decode()[:400]}"


def cut(start, dur, name):
    os.makedirs(CLIPS, exist_ok=True)
    dst = os.path.join(CLIPS, f"{name}.mp3")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", str(start), "-t", str(dur),
                    "-i", MIX, "-ac", "1", "-ar", "24000", "-b:a", "64k", dst], check=True)
    print(dst, os.path.getsize(dst), "bytes")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    cmd = sys.argv[1]
    if cmd == "cut":
        cut(float(sys.argv[2]), float(sys.argv[3]), sys.argv[4])
    elif cmd == "ask":
        q = sys.argv[3] if len(sys.argv) > 3 else None
        print(ask(sys.argv[2], q))
    elif cmd == "whole":
        dst = os.path.join(CLIPS, "whole.mp3")
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", MIX,
                        "-ac", "1", "-ar", "24000", "-b:a", "48k", dst], check=True)
        print(f"whole mix: {os.path.getsize(dst)/1e6:.1f} MB", file=sys.stderr)
        q = sys.argv[2] if len(sys.argv) > 2 else None
        print(ask("whole", q))
    elif cmd == "ask-all":
        names = sorted(n[:-4] for n in os.listdir(CLIPS) if n.endswith(".mp3"))
        for n in names:
            print(f"\n===== {n} =====")
            print(ask(n, None))
    else:
        print("commands: cut | ask | ask-all")


if __name__ == "__main__":
    main()
