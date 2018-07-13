import re
myf = open("mail.txt")
lst = myf.readlines()
domains = dict()
for l in lst:
    l = l.strip()
    a = re.search("^s.*",l)
    domains[a] = domains.get(a,0) + 1
for x,y in domains.items():
    print x,y
print len(domains)




#a = re.search("^s.*")
