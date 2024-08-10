# Challenge `Python requests Again` writeup

- Vulnerability 1: Replay attack exploit

The challenge is susceptible to exploiting the remaining tries value on the first cookie (value 1), allowing an attacker to use the same first cookie repeatedly, a type of replay attack, and reach the target value without fulfilling the intended conditions.

- Where: Remaining tries value

The vulnerability 1 is present in the remaining tries value that is stored in the first cookie (value 1).

- Vulnerability 2: Endpoint is vulnerable to brute force attack 

The challenge is susceptible to exploiting a brute force attack, allowing an attacker to manipulate the state and prematurely reach the target value without fulfilling the intended conditions, by doing many /more requests.

- Where: Endpoint /more

The vulnerability 2 is present in the /more endpoint, where additional numbers are obtained to reach the target value.

- Impact: Unauthorized completion of the challenge

Exploiting these vulnerabilities allows an attacker to manipulate the state and reach the target value without genuinely obtaining the required numbers. By repetition, with the remaining tries value of the first cookie, an attacker has total control of this challenge. This unauthorized completion of the challenge enables the attacker to access the /finish endpoint and retrieve the flag prematurely.

- NOTE:

The challenge 'Python requests Again' is much like the previous one, but now we are only given one chance to reach target.

---

## Steps to reproduce

I used the exactly same script from the previous challenge.
It works because im always using the first cookie to continuously have 1 remaining try, until i get the right sum.

[(POC)](Python_requests_Again.py)

