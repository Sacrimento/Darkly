import requests
import sys
import wget
import re
import os
import shutil
import uuid

ip = sys.argv[1] if len(sys.argv) > 1 else '192.168.1.240'
baseurl = 'http://' + ip + '/.hidden/'
reg = re.compile('<a href=\"([a-z]+\/)\">')

def explore(url):
    page = requests.get(url)
    for line in page.iter_lines():
        l = str(line[:40])
        m = re.findall(reg, l)
        if m:
            explore(url + m[0])
        elif 'README' in l:
            download(url)

def download(url):
    print(url)
    wget.download(url + 'README', out='readmes/' + str(uuid.uuid4()) + '.txt')

if __name__ == '__main__':
    i = input('Are you sure ? this will take long: ')
    if i not in ('Y', 'y'):
        exit()
    if os.path.isdir('readmes'):
        shutil.rmtree('readmes')
    os.mkdir('readmes')
    explore(baseurl)

