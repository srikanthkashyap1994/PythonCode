# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
df = 'http://python-data.dr-chuck.net/known_by_Fikret.html'

html = urllib.urlopen(' http://python-data.dr-chuck.net/known_by_Ricards.html  ').read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
count = 0
for tag in tags:
    if(count == 18):
        break
    a = tag.get('href', None)
    print a
    count = count + 1
html = urllib.urlopen(a).read()
soup = BeautifulSoup(html)
tags = soup('a')
count = 0
for tag in tags:
    if(count == 18):
        break
    a = tag.get('href',None)
    print a
    count = count + 1
html = urllib.urlopen(a).read()
soup = BeautifulSoup(html)
tags = soup('a')
count = 0
for tag in tags:
    if(count == 18):
        break
    a = tag.get('href',None)
    print a
    count = count + 1
html = urllib.urlopen(a).read()
soup = BeautifulSoup(html)
tags = soup('a')
count = 0
for tag in tags:
    if(count == 18):
        break
    a = tag.get('href',None)
    print a
    count = count + 1
html = urllib.urlopen(a).read()
soup = BeautifulSoup(html)
tags = soup('a')
count = 0
for tag in tags:
    if(count == 18):
        break
    a = tag.get('href',None)
    print a
    count = count + 1
html = urllib.urlopen(a).read()
soup = BeautifulSoup(html)
tags = soup('a')
count = 0
for tag in tags:
    if(count == 18):
        break
    a = tag.get('href',None)
    print a
    count = count + 1
html = urllib.urlopen(a).read()
soup = BeautifulSoup(html)
tags = soup('a')
count = 0
for tag in tags:
    if(count == 18):
        break
    a = tag.get('href',None)
    print a
    count = count + 1
