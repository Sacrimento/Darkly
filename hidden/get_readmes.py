import urllib3
import sys
import re
import os

ip = sys.argv[1] if len(sys.argv) > 1 else '192.168.1.240'
baseurl = 'http://' + ip + '/.hidden/'
reg = re.compile('<a href=\"([a-z]+\/)\">')
http = urllib3.PoolManager()

def explore(url, seen, unique):
    print('Analyzing', url, end='\r')
    page = http.request('GET', url)
    for line in str(page.data).split('\\n'):
        l = str(line[:40])
        m = re.findall(reg, l)
        if m:
            explore(url + m[0], seen, unique)
        elif 'README' in l:
            content = http.request('GET', url + 'README').data
            analyze(seen, unique, content)

def analyze(seen, unique, content):
    if content not in seen:
        seen.add(content)
        unique.add(content)
    elif content in seen and content in unique:
        unique.remove(content)

if __name__ == '__main__':
    seen = set()
    unique = set()

    explore(baseurl, seen, unique)
    
    print('\n\n Found unique README content :', unique.pop().decode()[:-1])
