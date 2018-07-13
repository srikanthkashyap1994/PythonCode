myfile = open("PDRs.txt")
for line in myfile:
	a = line.find("_tim::")
	b = line[a+1:]
	c = b.find("]")
	d = b[:c]
	e = d.find("::")
	f = d[e+2:]
	f = int(f)
	print f
	
	
myfile.close()
	
	