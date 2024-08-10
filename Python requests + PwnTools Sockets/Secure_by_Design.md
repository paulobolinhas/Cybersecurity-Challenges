# Challenge `Secure by Design` writeup

- Vulnerability: Authentication Bypass through Base64 encoding

The challenge is susceptible to an authentication bypass through Base64 encoding. By manipulating the encoded username in the POST request, an attacker can impersonate a different user and potentially gain unauthorized access.

- Where: POST request payload and cookies

The vulnerability is present in the POST request payload, where the "username" parameter is Base64 encoded. Additionally, the cookies used for authentication are manipulated to set a different user. 

- Impact: Unauthorized access to the system

Exploiting this vulnerability allows an attacker to impersonate another user by manipulating the Base64-encoded username. This unauthorized access could lead to various security risks, depending on the privileges associated with the impersonated user.

NOTE: 

The use of Base64 encoding for authentication introduces a flaw if the server relies solely on this encoding for user identification.

## Steps to reproduce

1. Access the initial page to gather information about the authentication mechanism and obtain the encoded username.
2. Decode the original encoded username to understand its structure.
3. Create a new encoded username with the desired user (example: "admin").
4. Create a new cookie with this value placed.
5. Make a POST request with the new cookie with the manipulated username and send it to the server.
6. Observe the response to verify if the authentication bypass was successful.

[(POC)](Secure_by_Design.py)

