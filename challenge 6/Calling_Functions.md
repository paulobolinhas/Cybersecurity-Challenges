# Challenge `Calling Functions` writeup

- Vulnerability: Buffer Overflow

- Where: buffer (exploit fp func)

- Impact: Attacker can modify the function pointer fp to point to the address of the win() function

---

## Steps to reproduce

1. Connect to server mustard.
2. First fill the buffer with 32 'A' characters to overflow the buffer.
3. Get the initial adress of the win() func with 'disassemble win'.
4. Append, in the payload, the little-endian representation of the address of the win() function.
5. Print server response.

[(POC)](Calling_Functions.py)

