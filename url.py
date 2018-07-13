import urllib
import re
from BeautifulSoup import *
b = list()

html = urllib.urlopen("http://python-data.dr-chuck.net/comments_354916.html").read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    a = 'Contents:',tag.contents[0]
    #print a[1]
    b.append(int(a[1]))
print sum(b)


        #print 'Attrs:',tag.attrs
