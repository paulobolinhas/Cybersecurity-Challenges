# Challenge `Write to Memory` writeup

- Vulnerability: Format String Vulnerability

- Where: Write to Memory using `%n` specifier

- Impact: Attacker can write to arbitrary memory addresses

---

## Steps to reproduce

1. **Connect to the Server:**
   - Server: mustard.stt.rnl.tecnico.ulisboa.pt
   - Port: 23193

2. **Objective:**
   - This challenge involves exploiting a format string vulnerability to write a specific value to the `target` variable using the `%n` specifier.

3. **Exploit Steps:**
   - Inspect the stack by sending an arbitrary number of `%08x` to understand the stack layout.
   - Identify the address of the `target` variable using the binary or a debugger like GDB.
   - Construct a payload to overwrite the value of the `target` variable using the `%n` specifier.

[(POC)](Write_to_Memory.py)

