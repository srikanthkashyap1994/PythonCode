num = int(raw_input("Enter a number: "))
for i in range(1,20):
    if (num % (10**i) == num):
        digits = i
        break
print "Number of digits:",digits

all_digits = list()
for j in range(1,i):
    all_digits.append((num/10**(i-j))%10)
print all_digits
l = len(all_digits)
all_digits.reverse()
for i in range(0,len(all_digits)):
    print (all_digits[i])*(10**i)
