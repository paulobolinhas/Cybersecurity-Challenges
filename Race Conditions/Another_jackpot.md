# Challenge `Another jackpot` writeup

- Vulnerability: Race Condition - Commit before verifies

- Where: login() func in server.py between commit and the query to the DB

- Impact: The race condition allows an attacker to potentially exploit the timing between login attempts and jackpot checks.

## Steps to reproduce

1. Create a persistent session object using requests.Session().
2. Define a jackpot function that continuously sends GET requests to the URL "http://mustard.stt.rnl.tecnico.ulisboa.pt:23652/jackpot" with admin user and pssw. If the response text contains the string `SSof{`, it prints the response text, that contains the flag.
3. Define a login function that continuously sends POST requests to the URL "http://mustard.stt.rnl.tecnico.ulisboa.pt:23652/login" with admin user and pssw.
4. Create a ThreadPoolExecutor. Submit the jackpot and login functions to the executor, which will run them concurrently. 
5. You will acess to the jackpot before the commit, with admin, so only after that, the commit to the DB and verification are done, finally the flag has to appear.
6. Ctrl+C the program.

[(POC)](Another_jackpot.py)
