# Challenge `Match an Exact Value` writeup

- Vulnerability: Buffer Overflow

- Where: buffer (exploit test var)

- Impact: Attacker can change the value of a var through buffer in order to exploit the flag

---

## Steps to reproduce

1. Connect to server mustard.
2. In this challenge, you need to perform a buffer overflow again, but this time, the goal is to change the value of the test variable to the specific value 0x61626364 (the ASCII string "abcd"). 
3. First fill the buffer with 64 'A' characters because 'buffer[64]'.
4. Then append the little-endian representation of 0x61626364 using struct from the pwn library or "dcba". This should overwrite the test variable with the value 0x61626364.
3. Print server response.

[(POC)](Match_an_Exact_Value.py)

