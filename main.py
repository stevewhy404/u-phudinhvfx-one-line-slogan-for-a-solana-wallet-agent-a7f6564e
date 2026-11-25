#!/usr/bin/env python3
"""One-line slogan for a Solana wallet agent.

Writes a single slogan (<=140 chars, <=20 words) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os

SLOGAN = "Your Solana wallet grew a brain \u2014 it signs, swaps, and saves while you sleep."

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SLOGAN)

if __name__ == "__main__":
    main()
