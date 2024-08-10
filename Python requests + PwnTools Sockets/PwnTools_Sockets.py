from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23055

s = remote(SERVER, PORT, timeout=9999)

all_data = s.recvuntil(b"What do you want?")

target = int(re.findall(rb'\b\d+\b', all_data)[0])
current_value = 0

while current_value != target:
    s.sendline(b'MORE')

    response = s.recvuntil(b"What do you want?")
    number = int(re.findall(rb'-?\b\d+\b', response)[0])

    current_value += number
    print(f'Current value: {current_value}')

    if current_value == target:
        break

s.sendline(b'FINISH')
flag = s.recvall().decode()
print(f'Flag: {flag}')
