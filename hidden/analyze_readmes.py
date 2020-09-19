import os

if __name__ == '__main__':
    seen = set()
    unique = set()
    for fi in os.listdir('readmes'):
        with open('readmes/'+fi) as f:
            content = f.read()
            if content not in seen:
                seen.add(content)
                unique.add(content)
            elif content in seen and content in unique:
                unique.remove(content)
    print(*unique)
