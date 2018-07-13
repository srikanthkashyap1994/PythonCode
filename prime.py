num = int(raw_input("Enter a Number: "))
for i in range(2,num):
    if (num % i == 0):
        print "This is Not Prime"
        exit()
    else:
        continue
print "This is Prime"
