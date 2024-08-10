# Challenge `Simple Local Read` writeup

- Vulnerability: Format String Vulnerability

- Where: Local Read through Format String Vulnerability

- Impact: Attacker can read arbitrary values from memory

---

## Steps to reproduce

1. **Connect to the Server:**
   - Server: mustard.stt.rnl.tecnico.ulisboa.pt
   - Port: 23191

2. **Objective:**
   - The goal of this challenge is to exploit a format string vulnerability to read the value of the `secret_value` variable.

3. **Exploit Steps:**
   - A format string vulnerability is present in the `printf` statement. The payload uses `%7$s` to attempt to leak the contents of the seventh argument on the stack.
   - Since `secret_value` is loaded into the stack, using `%s` instead of `%x` allows reading the value pointed to by the address.


[(POC)](Simple_Local_Read.py)

