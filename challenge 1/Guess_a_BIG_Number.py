import requests

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23052"

s = requests.Session()
s.get(link)

# search space
low = 0
high = 100000

while low < high:
    # middle point
    mid = (low + high) // 2

    # request with the current guess
    response = s.get(link + f"/number/{mid}")

    if "SSof" in response.text:
        print(response.text)
        break
    elif "Higher!" in response.text:
        low = mid + 1
    elif "Lower!" in response.text:
        high = mid