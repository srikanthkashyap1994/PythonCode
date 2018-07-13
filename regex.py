import re
b = list()
myf = open("actual.txt")
for line in myf:
    line = line.strip()
    a = re.findall("[0-9]+",line)
    if (len(a) == 0):
        continue
    b.append(a)
for j in range(len(b)):
    for i in range(len(b[j])):
        b[j][i] = int(b[j][i])
z = list()
for k in b:
    z.append(sum(k))
print sum(z)
