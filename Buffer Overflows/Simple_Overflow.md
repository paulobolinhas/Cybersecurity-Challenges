# Challenge `Simple Overflow` writeup

- Vulnerability: Buffer Overflow

- Where: buffer (exploit test var)

- Impact: Attacker can change the value of a var through buffer in order to exploit the flag

---

## Steps to reproduce

1. Connect to server mustard.
2. Overflow the server buffer with "A"'s, in this case, * 128, because 'char buffer[128]' and send a char after to complete the payload.
3. Print server response.

[(POC)](Simple_Overflow.py)

