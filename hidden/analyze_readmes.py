import os

if __name__ == '__main__':
    seen = set()
    for fi in os.listdir('readmes'):
        with open('readmes/'+fi) as f:
            content = f.read()
            if content not in seen:
                seen.add(content)
                print('-----------------------------------------')
                print(content)
                print('-----------------------------------------')