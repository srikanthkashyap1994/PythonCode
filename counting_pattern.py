counts = dict()
line = raw_input("Enter a string of text: ")
words = line.split()
for word in words:
	counts[word] = counts.get(word,0) + 1
print 'Counts',counts	
