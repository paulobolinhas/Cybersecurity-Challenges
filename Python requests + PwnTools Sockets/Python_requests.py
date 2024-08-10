import requests
import re

SERVER = 'http://mustard.stt.rnl.tecnico.ulisboa.pt:23053'  

response = requests.get(f'{SERVER}/hello')
target = re.findall(r'\b\d+\b', response.text)
cookies = response.cookies
current_value = 0

while current_value != int(target[0]):
    response = requests.get(f'{SERVER}/more', cookies=cookies)
    number = int(re.findall(r'-?\b\d+\b', response.text)[0])
    current_value += number
    print(f'Current value: {current_value}')

response = requests.get(f'{SERVER}/finish', cookies=cookies)

flag = response.text
print(f'Flag: {flag}')