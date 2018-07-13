import re
hand = open("file.txt")
for line in hand:
	line = line.strip()
	if re.search('^From:',line):
		print line
		

		
		
^X.*:
^X.*:
^X-\S: 
\S is non blank character
^X-\S+: atleast one blank character before the colon
[0-9]+


\S+@\S+ gives non blank characters without spaces
y = findall('^From (\S+@\S+)',x)
y = findall('^From .*@([^ ]*)',lin)
print y

	