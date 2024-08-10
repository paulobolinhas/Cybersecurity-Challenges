# Challenge `Python requests` writeup

- Vulnerability: Endpoint is vulnerable to brute force attack 

The challenge is susceptible to exploiting a brute force attack, allowing an attacker to manipulate the state and prematurely reach the target value without fulfilling the intended conditions, by doing many /more requests.

- Where: Endpoint /more

The vulnerability is present in the /more endpoint, where additional numbers are obtained to reach the target value.

- Impact: Unauthorized completion of the challenge

Exploiting this vulnerability allows an attacker to manipulate the challenge's state and reach the target value without genuinely obtaining the required numbers. This unauthorized completion of the challenge enables the attacker to access the /finish endpoint and retrieve the flag prematurely.

---

## Steps to reproduce

1. Access the /hello endpoint to initiate and obtain the initial target value(number we want) and first cookie.

2. While the current value is not equal to the target value:
  - 2.1. Access the /more endpoint with the previous cookie.
  - 2.2. Update the current value based on the new positive or negative number (sum) obtained.

3. Once the current value matches the target value, access the /finish endpoint to retrieve the flag.

[(POC)](Python_requests.py)

