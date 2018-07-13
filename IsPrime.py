#try:
#    n = raw_input("Enter a Number: ")
#except:
#    print "Enter a valid input!"
#    exit()
#num = int(n)
num_list = list()
for j in range(1,100):
    for i in range(2,((j/2)+1)):
        if (j % i == 0):
            #print "This is Not Prime"
            break
    else:
            continue
        num_list.append(j)
print num_list
