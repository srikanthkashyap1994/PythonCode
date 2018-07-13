class student:
    def __init__(self):
        print "Student Created"
        self.name = raw_input("What is the name of the student?")
        print "Hello",self.name,"Welcome to India!"
        self.total = 0
        self.average = 0
        self.maths = 0
        self.physics = 0
        self.chemistry = 0
    def totalmarks(self):
        self.total = int(self.maths) + int(self.physics) + int(self.chemistry)
        return self.total
    def avg(self):
        self.average = (int(self.maths) + int(self.physics) + int(self.chemistry))/ 3.0
        return float(self.average)

    def __del__(self):
        print "The student",self.name,"is no longer in the database!"

Srikanth = student()
Srikanth.maths = raw_input("Enter your percentage in Math: ")
Srikanth.physics = raw_input("Enter your percentage in Physics: ")
Srikanth.chemistry = raw_input("Enter your percentage in Chemistry: ")
#print "Your total marks are ",Srikanth.totalmarks()
print "And your average is ",Srikanth.avg()

Kashyap = student()
Kashyap.maths = raw_input("Enter your percentage in Math: ")
Kashyap.physics = raw_input("Enter your percentage in Physics: ")
Kashyap.chemistry = raw_input("Enter your percentage in Chemistry: ")
#print "Your total marks are ",Kashyap.totalmarks()
print "And your average is ",Kashyap.avg()
