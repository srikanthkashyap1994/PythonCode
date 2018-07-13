import urllib
fhand = urllib.urlopen('http://10.64.254.107:8082/PS_REQUEST/?action=viewEnterprise')
for line in fhand:
    print line.strip()
