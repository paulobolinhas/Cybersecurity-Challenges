# Challenge `PwnTools Sockets` writeup

- Vulnerability: Endpoint is vulnerable to brute force attack 

Similar to the Python requests challenge, the PwnTools Sockets challenge is susceptible to exploiting a brute force attack. The server does not adequately validate the input for the MORE command, allowing an attacker to manipulate the state and prematurely reach the target value without fulfilling the intended conditions, by doing many MORE requests.

- Where: Sockets communication with the server

The vulnerability is present in the communication over sockets, specifically in handling the MORE command. The lack of proper input validation in processing this command creates an avenue for brute force exploitation.

- Impact: Unauthorized completion of the challenge

Exploiting this vulnerability allows an attacker to manipulate the challenge's state and reach the target value without genuinely obtaining the required numbers. This unauthorized completion of the challenge enables the attacker to send the FINISH command prematurely and retrieve the flag without fulfilling the intended conditions.

---

## Steps to reproduce

1. Connect to the server using PwnTool 'remote' and receive the initial challenge information, including the target value.

2. While the current value is not equal to the target value:
  - 2.1. Send the MORE command to the server in order to get a new number.
  - 2.2. Update the current value based on the number retrieved from the response received from the server (sum).

3. Once the current value matches the target value, send the FINISH command to the server to retrieve the flag.

[(POC)](PwnTools_Sockets.py)

