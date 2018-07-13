name = raw_input("Enter the name of the file: ")
handle = open(name,"r")
text = handle.read()
words = text.split()
counts = dict()
for word in words:
	counts[word] = counts.get(word,0) + 1
bigword = None
bigcount = None
for key,value in counts:
	if ((bigcount == None) or (count > bigcount)):
		bigword = key
		bigcount = value
print bigword,bigcount
	
