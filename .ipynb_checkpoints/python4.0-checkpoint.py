# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


# class Person(object):

# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name

# 	# To get name
# 	def getName(self):
# 		return self.name

# 	# To check if this person is an employee
# 	def isEmployee(self):
# 		return False


# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):

# 	# Here we return true
# 	def isEmployee(self):
# 		return True


# # Driver code
# emp = Person("Geek1") # An Object of Person
# print(emp.getName(), emp.isEmployee())

# emp = Employee("Geek2") # An Object of Employee
# print(emp.getName(), emp.isEmployee())


# parent class
# class Person():
#     def __init__(self, name, age):
# 	    self.name = name
# 	    self.age = age
#     def display(self):
# 	    print(self.name, self.age)
# # child class
# class Student(Person):
#     def __init__(self, name, age):
# 	    self.sName = name
# 	    self.sAge = age
# 	# inheriting the properties of parent class
# 	super().__init__("Rahul", age)
#     def displayInfo(self):
#     	print(self.sName, self.sAge)

# obj = Student("Mayank", 23)
# obj.display()
# obj.displayInfo()

# parent class
# class Person():
# def __init__(self, name, age):
# 	self.name = name
# 	self.age = age

# def display(self):
# 	print(self.name, self.age)

# # child class
# class Student(Person):
# def __init__(self, name, age, dob):
# 	self.sName = name
# 	self.sAge = age
# 	self.dob = dob
# 	# inheriting the properties of parent class
# 	super().__init__("Rahul", age)

# def displayInfo(self):
# 	print(self.sName, self.sAge, self.dob)

# obj = Student("Mayank", 23, "16-03-2000")
# obj.display()
# obj.displayInfo()

# Python example to show the working of multiple
# inheritance

# class Base1(object):
#     def __init__(self):
#         self.str1 = "Geek1"
#         print("Base1")
# class Base2(object):
# 	def __init__(self):
# 		self.str2 = "Geek2"
# 		print("Base2")
# class Derived(Base1,Base2):
# 	def __init__(self):
# 		# Calling constructors of Base1
# 		# and Base2 classes
# 		Base1.__init__(self)
# 		Base2.__init__(self)
# 		print("Derived")
# 	def printStrs(self):
# 		print(self.str1, self.str2)
# ob = Derived()
# ob.printStrs()


# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"

# class Base(object):

# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name

# 	# To get name
# 	def getName(self):
# 		return self.name


# # Inherited or Sub class (Note Person in bracket)
# class Child(Base):

# 	# Constructor
# 	def __init__(self, name, age):
# 		Base.__init__(self, name)
# 		self.age = age

# 	# To get name
# 	def getAge(self):
# 		return self.age

# # Inherited or Sub class (Note Person in bracket)


# class GrandChild(Child):

# 	# Constructor
# 	def __init__(self, name, age, address):
# 		Child.__init__(self, name, age)
# 		self.address = address

# 	# To get address
# 	def getAddress(self):
# 		return self.address


# # Driver code
# g = GrandChild("Geek1", 23, "Noida")
# print(g.getName(), g.getAge(), g.getAddress())


# Python program to demonstrate private members
# of the parent class

# class C(object):
# 	def __init__(self):
# 		self.c = 21
# 		# d is private instance variable
# 		self.d = 42


# class D(C):
# 	def __init__(self):
# 		self.e = 84
# 		print(self.d)
# 		C.__init__(self)

# object1 = D()

# # produces an error as d is private instance variable
# print(object1.c)
# print(object1.__d)
# Python program showing
# abstract base class work

# from abc import ABC#, abstractmethod
# class Polygon(ABC):
#     # @abstractmethod
#     def noofsides(self):
#         pass
# class Triangle(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 3 sides")
# class Pentagon(Polygon):

#     # overriding abstract method
#     def noofsides(self):
#         print("I have 5 sides")


# class Hexagon(Polygon):

#     # overriding abstract method
#     def noofsides(self):
#         print("I have 6 sides")


# class Quadrilateral(Polygon):

#     # overriding abstract method
#     def noofsides(self):
#         print("I have 4 sides")


# # Driver code
# R = Triangle()
# R.noofsides()

# K = Quadrilateral()
# K.noofsides()

# R = Pentagon()
# R.noofsides()

# K = Hexagon()
# K.noofsides()

# Python program showing
# implementation of abstract
# class through subclassing
# import abc

# class parent:       
#     def geeks(self):
#         pass
# class child(parent):
#     def geeks(self):
#         print("child class")
# # Driver code
# print( issubclass(child, parent))
# print( isinstance(child(), parent))


# Python program showing
# abstract properties

# import abc
# from abc import ABC, abstractmethod


# class parent(ABC):
#     @abc.abstractproperty
#     def geeks(self):
#         return "parent class"
# class child(parent):
#     @property
#     def geeks(self):
#         return "child class"
# try:
#     r = parent()
#     print(r.geeks)
# except Exception as err:
#     print(err)
# r = child()
# print(r.geeks)



# Python program to 
# demonstrate protected members 

# Creating a base class 
# class Base: 
# 	def __init__(self): 
# 		# Protected member 
# 		self._a = 2
# # Creating a derived class 
# class Derived(Base): 
# 	def __init__(self): 
# 		# Calling constructor of 
# 		# Base class 
# 		Base.__init__(self) 
# 		print("Calling protected member of base class: ", 
# 			self._a) 

# 		# Modify the protected variable: 
# 		self._a = 3
# 		print("Calling modified protected member outside class: ", 
# 			self._a) 


# obj1 = Derived() 

# obj2 = Base() 

# Calling protected member 
# Can be accessed but should not be done due to convention 
# print("Accessing protected member of obj1: ", obj1._a) 

# # Accessing the protected variable outside 
# print("Accessing protected member of obj2: ", obj2._a) 
# Python program to 
# demonstrate private members 

# Creating a Base class 


# class Base: 
# 	def __init__(self): 
# 		self.a = "GeeksforGeeks"
# 		self.__c = "GeeksforGeeks"

# # Creating a derived class 
# class Derived(Base): 
# 	def __init__(self): 

# 		# Calling constructor of 
# 		# Base class 
# 		Base.__init__(self) 
# 		print("Calling private member of base class: ") 
# 		print(self.__c) 


# # Driver code 
# obj1 = Base() 
# print(obj1.a) 

# Uncommenting print(obj1.c) will 
# raise an AttributeError 

# Uncommenting obj2 = Derived() will 
# also raise an AttributeError as 
# private member of base class 
# is called inside derived class 
# Prints all letters except 'e' and 's' 
# i = 0
# a = 'geeksforgeeks'
# while i < len(a): 
# 	if a[i] == 'e' or a[i] == 's': 
# 		i += 1
# 		continue
		
# 	print('Current Letter :', a[i]) 
# 	i += 1


# Python program to demonstrate 
# while-else loop 

i = 0
while i < 4: 
	i += 1
	print(i) 
else: # Executed because no break in for 
	print("No Break\n") 
i = 0
while i < 4: 
	i += 1
	print(i) 
else: # Not executed as there is a break 
	print("No Break") 
