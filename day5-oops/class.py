#blue print
class Person:
    def disp():
        print('person details')
    def show():
        print('another fucntion')
#object
p=Person
p1=Person
p.disp()
p.show()
p1.show()
p1.disp()





# name, age
# self memberor variable of current class 
# constructor


#encapsulation  - binding data and function
# in object
class Person:
   def __init__(self,name,age):
       self.name=name
       self.age=age
   def show(self):
        print(self.name, self.age)
   def addage(self,x):
       print(self.name)
       print(self.age+x)

p=Person('Ram',30)
p.show()
p.addage(5)


class Student:
    def __init__(self,id,name,email):     # constructor
        self.id=id
        self.name=name
        self.email=email
    def printData(self):   #BL some logic
        print(self.id,self.name,self.email)

s1=Student(101,'ram','ram@gmail.com')
s2=Student(102,'raj','raj@gmail.com')
s3=Student(103,'kiran','kiran@gmail.com')

s1.printData()
s2.printData()
s3.printData()




