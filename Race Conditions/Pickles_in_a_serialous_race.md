# Challenge `Pickles in a seri(al)ous race` writeup

- Vulnerability: Pickle Injection

- Where: #Main functionality

pickle.loads & pickle.dumps on read and write

- Impact: Remote Code Execution

allows an attacker to execute arbitrary commands on the server.

## Steps to reproduce

1. Open a session and read a classy note until you choose 'Read note' (do not insert the name yet)
2. Dumps a pickle with command 'grep -r "SSof{" .' (payload made in a RCE class)
3. Open a session and write in a free note with that pickle as content (don't forget to regist the note with '2space\n')
4. Only send the name to read now (name of the written previously note), with the initial Read session/connection
5. See connection content (pwn tool - recvall()) and Ctrl + F "SSof{" to find the flag
6. You will probably have to run the code more than 1 time to get the data in time (race condition)

[(POC)](Pickles_in_a_serialous_race.py)
