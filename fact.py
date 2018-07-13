def factorial(number):
	if (number < 0):
		print "Dude! Be positive!"
		return 0
		
	elif (number == 0):
		print 1
		return 1
	elif(number == 1):
		print 1 
		return 1 
	else:
		fact = 1 
		for i in range(1,int(number)+1):
			fact = fact * i
		print fact
		return fact

		
n = int(raw_input("Enter a number: "))
factorial(n)
	
	