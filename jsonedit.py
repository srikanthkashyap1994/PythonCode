import json
myf = open("file.txt","r+")
data = myf.read()
js = json.loads(data)
myf2 = open("newfile.json","r+")
myf2.write(data)
print data
data2 = myf2.read().strip()
js2 = json.loads(data2)
js2["ENTERPRISE_ID"] = 786
js2["CUG_ID"] = 7777
j = json.dumps(js2)
myf2.write(j)
print js2
myf.close()
myf2.close()
