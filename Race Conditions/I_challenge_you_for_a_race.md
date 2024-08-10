# Challenge `I challenge you for a race` writeup

- Vulnerability: Time of Check to Time of Use (TOCTOU)

- Where: /challenge/read_file.c

- Impact: Allows an attacker to replace the symbolic link with a link to /challenge/flag, potentially revealing sensitive information, in this case, the flag.

## Steps to reproduce

1. Connect to the machine via SSH using the provided credentials: 
ssh username@server -p port
2. Observe that the only writable directory is /tmp. Create a directory with a unique name inside /tmp.
3. On a script sh bash:
  - 3.1. Create a dump file
  - 3.2. Create a symbolic link pointing to dump
  - 3.3. Run the program in the background with the symbolic link as an argument
  - 3.4. Replace it with a link to /challenge/flag exploiting the TOCTOU vulnerability
4. Run "scp -P port .sh ssh username@server -p port" to put the bash on the server
5. chmod +x the script and run it

[(POC)](I_challenge_you_for_a_race.sh)
