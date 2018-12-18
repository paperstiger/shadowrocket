#!/usr/bin/env python
import os
import sys


def main():
    THE_FILE = 'Shadowrocket.conf'
    os.rename(THE_FILE, 'tmp.txt')
    os.system("wget https://raw.githubusercontent.com/lhie1/Rules/master/Shadowrocket.conf")
    if not sys.path.exists(THE_FILE):
        print('Fail to download, do nothing')
        os.rename('tmp.txt', THE_FILE)
        return
    with open(THE_FILE, 'r') as f:
        with open('tmp.txt', 'w') as g:
            for line in f:
                line = line.replace('PROXY', 'DIRECT')
                g.write(line)
    os.remove(THE_FILE)
    os.rename('tmp.txt', THE_FILE)


if __name__ == '__main__':
    main()

