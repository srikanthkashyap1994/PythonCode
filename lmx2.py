import urllib
import xml.etree.ElementTree as ET

url = ' http://python-data.dr-chuck.net/comments_354913.xml'
u = urllib.urlopen(url).read()
#print u
tree = ET.fromstring(u)
lst = tree.findall('comments/comment/count')
#print len(lst)
total = 0
for l in lst:
    total = total + int(l.text)
print total
#print tree
#print type(tree)
#print tree.find('count')
#coun = tree.findall('.//count')
#print coun[0].find('count').text
#print type(coun[0])
