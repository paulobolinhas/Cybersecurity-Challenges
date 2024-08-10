# Challenge `Return Address` writeup

- Vulnerability: Buffer Overflow

- Where: buffer (exploit fp func)

- Impact: Attacker can call the win function without it being explicitly called in the code.

---

## Steps to reproduce

1. Connect to server mustard.
2. Since you're limited to calling functions within main or through challenge(), you need to leverage the return address on the stack to redirect the program flow to the win function.
3. Make a breakpoint on challenge func, with 'break challenge' and run.
4. Check the buffer address with 'p &buffer' and the eip with 'i f'.
5. Do the substraction to get the number to overflow with 'p /x' and convert the hexadecimal result to decimal 
-> p /x 0xffffcfbc - 0xffffcfa6 = 0x16 = 22 
6. Payload the 22 "A"'s with the little-endian representation of the address of the win() function.
7. Print server response.

[(POC)](Return_Address.py)

