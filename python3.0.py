# Explicit function
# def digitSum(n):
#     dsum = 0
#     for ele in str(n):
#         dsum += int(ele)
#     return dsum
# # Initializing list
# List = [367, 111, 562, 945, 6726, 873]

# # Using the function on odd elements of the list
# newList = [digitSum(i) for i in List if i & 1]

# # Displaying new list
# print(newList)
# Python program to illustrate short hand if-else
# i = 10
# print(False) if i < 15 else print(True)
# simple match case statement
# def runMatch():
#     num = int(input("Enter a number between 1 and 3: "))
#     # match case
#     match num:
#         # pattern 1
#         case 1:
#             print("One")
#         # pattern 2
#         case 2:
#             print("Two")
#         # pattern 3
#         case 3:
#             print("Three")
#         # default pattern
#         case _:
#             print("Number not between 1 and 3")
# runMatch()
# python match case with OR operator

# def runMatch():
#     num = int(input("Enter a number between 1 and 6: "))  
#     # match case
#     match num:
#         # pattern 1
#         case 1 | 2:
#             print("One or Two")
#         # pattern 2
#         case 3 | 4:
#             print("Three or Four")
#         # pattern 3
#         case 5 | 6:
#             print("Five or Six")
#         # default pattern
#         case _:
#             print("Number not between 1 and 6")   
# runMatch()


# python match case with if condition
# def runMatch():
#     num = int(input("Enter a number: "))
    
#     # match case
#     match num:
#         # pattern 1
#         case num if num > 0:
#             print("Positive")
#         # pattern 2
#         case num if num < 0:
#             print("Negative")
#         # default pattern
#         case _:
#             print("Zero")
            
# runMatch()


# match case to check a character in a string
# def runMatch():
#     myStr = "Hello World"
#     # match case
#     match (myStr[6]):
#         case "w":
#             print("Case 1 matches")
#         case "W":
#             print("Case 2 matches")
#         case _:
#             print("Character not in the string")
            
# runMatch()


# python match case with list
# def runMatch(mystr):
    
#     # match case
#     match mystr:
#         # pattern 1
#         case ["a"]:
#             print("a")
#         # pattern 2
#         case ["a", *b]:
#             print(f"a and {b}")
#         # pattern 3
#         case [*a, "e"] | (*a, "e"):
#             print(f"{a} and e")
#         # default pattern
#         case _:
#             print("No data")
            
# runMatch([])
# runMatch(["a"])
# runMatch(["a", "b"])
# runMatch(["b", "c", "d", "e"])
# match case with python classes
# import dataclass module
# from dataclasses import dataclass
# #Class 1
# @dataclass
# class Person:
#     name: str
#     age: int
#     salary: int

# # class 2
# @dataclass
# class Programmer:
#     name: str
#     language: str
#     framework: str

# def runMatch(instance):
#     # match case
#     match instance:
#         # pattern 1
#         case Programmer("Om", language="Python", framework="Django"):
#             print(f"Name: Om, Language:Python, Framework:Django")
#         # pattern 2
#         case Programmer("Rishabh", "C++"):
#             print("Name:Rishabh, Language:C++")
#         # pattern 3
#         case Person("Vishal", age=5, salary=100):
#             print("Name:Vishal")
#         # pattern 4
#         case Programmer(name, language, framework):
#             print(f"Name:{name}, Language:{language}, Framework:{framework}")
#         # pattern 5
#         case Person():
#             print("He is just a person !")
#         # default case
#         case _:
#             print("This person is nothiing!")

# programmer1 = Programmer("Om", "Python", "Django")
# programmer2 = Programmer("Rishabh", "C++", None)
# programmer3 = Programmer("Sankalp", "Javascript", "React")
# person1 = Person("Vishal", 5, 100)
# runMatch(programmer1)
# runMatch(programmer2)
# runMatch(person1)
# runMatch(programmer3)

# class GFG:
#     def __init__(self,name,company):
#         self.name = name
#         self.company = company
#     def show(self):
#         print("Hello my name is " + self.name+" and I" +
#               " work in "+self.company+".")
# obj = GFG("John", "GeeksForGeeks")
# obj.show()

# class GFG:
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company
#     def __str__(self):
#         return f"My name is {self.name} and I work in {self.company}."
# my_obj = GFG("John", "GeeksForGeeks")
# print(my_obj)

# class Dog:

#     # Class Variable
#     animal = 'dog'

#     # The init method or constructor
#     def __init__(self, breed):

#         # Instance Variable
#         self.breed = breed

#     # Adds an instance variable
#     def setColor(self, color):
#         self.color = color

#     # Retrieves instance variable
#     def getColor(self):
#         return self.color


# # Driver Code
# Rodger = Dog("pug")
# Rodger.setColor("brown")
# print(Rodger.getColor())



# class India():
# 	def capital(self):
# 		print("New Delhi is the capital of India.")
# 	def language(self):
# 		print("Hindi is the most widely spoken language of India.")
# 	def type(self):
# 		print("India is a developing country.")
# class USA():
# 	def capital(self):
# 		print("Washington, D.C. is the capital of USA.")
# 	def language(self):
# 		print("English is the primary language of USA.")
# 	def type(self):
# 		print("USA is a developed country.")
# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind,obj_usa):
# 	country.capital()
# 	country.language()
# 	country.type()
# class Animal:
# 	def speak(self):
# 		raise NotImplementedError("Subclass must implement this method")
# class Dog(Animal):
# 	def speak(self):
# 		return "Woof!"
# class Cat(Animal):
# 	def speak(self):
# 		return "Meow!"
# # Create a list of Animal objects
# animals = [Dog(),Cat()]
# # Call the speak method on each object
# for animal in animals:
# 	print(animal.speak())
