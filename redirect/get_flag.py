import os
import requests
import re

ip = os.getenv('darkly_ip')
url = f'http://{ip}/index.php?page=redirect&site=toto'

if __name__ == '__main__':
    r = requests.get(url)
    m = re.findall('the flag : ([a-z0-9]+)<', r.text)
    print(*m)
