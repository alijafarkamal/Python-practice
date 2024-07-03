# import sys
# sys.stdout.write("GeeksforGeeks ")
# sys.stdout.write("is best website for coding!")
#import the below module and see what happens 
# import antigravity 
# Python program showing how to use string modulo operator(%)

# print("Geeks : %2d, Portal : %5.2f" % (1, 05.333)) 
# print("Total students : %3d, Boys : %2d" % (240, 120))   # print integer value
# print("%7.3o" % (25))   # print octal value
# print("%10.3E" % (356.08977))   # print exponential value


# tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}
# tab = {'geeks': 2342, 'for': 92432,'geek': 20942}
# using format() in dictionary
# print('Geeks: {0[geeks]:d}; For: {0[for]:d}; ' 'Geeks: {0[geek]:d}'.format(tab))
# data = dict(fun ="GeeksForGeeks", adj ="Portal")
# print("I love {fun} computer {adj}".format(**data))


# cstr = "I love geeksforgeeks"

# # Printing the center aligned string with fillchr
# print("Center aligned string with fillchr: ")
# print(cstr.center(34, '#'))

# # Printing the left aligned string with "-" padding
# print("The left aligned string is : ")
# print(cstr.ljust(40, '-'))

# # Printing the right aligned string with "-" padding
# print("The right aligned string is : ")
# print(cstr.rjust(40, '-'))


# Python program showing
# a use of raw_input()

# num = int(input("Enter a number: "))
# print(num, " ", type(num))

          
# floatNum = float(input("Enter a decimal number: "))
# print(floatNum, " ", type(floatNum))

# Python program showing how to
# multiple input using split

# taking two inputs at a time
# x, y = input("Enter two values: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)

# taking three inputs at a time
# x, y, z = input("Enter three values: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)

# taking two inputs at a time
# a, b = input("Enter two values: ").split()
# print("First number is {} and second number is {}".format(a, b))

# taking multiple inputs at a time 
# and type casting using list() function

# num = list(map(int,input("Enter multiple values: ").split()))
# print("List of students: ", num)      
#Example with integers
# a, b, c = map(int, input("Enter three integers separated by spaces: ").split())
# print("Sum:", a + b + c)

# #Example with floats:
# x, y = map(float, input("Enter two floats separated by a space: ").split())
# print("Product:", x * y)

# #Example with strings:
# name, age = input("Enter your name and age separated by a space: ").split()
# print("Hello,", name + "! You are", age, "years old.")
        

# Python program showing
# how to take multiple input
# using List comprehension

# taking two input at a time
# x,y = [int(x) for x in input("Enter two values: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)
# # taking three input at a time
# x, y, z = [int(x) for x in input("Enter three values: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)
# print("Third Number is: ", z)

# # taking two inputs at a time
# x, y = [int(x) for x in input("Enter two values: ").split()]
# print("First number is {} and second number is {}".format(x, y))

# # taking multiple inputs at a time 
# x = [int(x) for x in input("Enter multiple values: ").split(",")]
# print("Number of list is: ", x) 
# import array as arr
# a = arr.array('i',[1,2,3])
# for i in range(0,3):
#     print(a[i],end=" ")
# print()
# b = arr.array('d', [2.5, 3.2, 3.3])
# print("\nThe new created array is : ", end=" ")
# for i in range(0, 3):
#     print(b[i], end=" ")


# import array as arr
# a = arr.array('i', [1, 2, 3])
# print("Array before insertion : ", end=" ")
# for i in range(0, 3):
#     print(a[i], end=" ")
# print()
# a.append(5)
# print("Array after insertion : ", end=" ")
# for i in (a):
#     print(a[i], end=" ")
# print()
# b = arr.array('d', [2.5, 3.2, 3.3])
# print("Array before insertion : ", end=" ")
# for i in range(0, 3):
#     print(b[i], end=" ")
# print()
# b.append(4.4)
# print("Array after insertion : ", end=" ")
# for i in (b):
#     print(i, end=" ")
# print()
# import array
# arr = array.array('i', [1, 2, 3, 1, 5])
# print("The new created array is : ", end="")
# for i in range(0, 5):
#     print(arr[i], end=" ")

# print("\r")
# print("The popped element is : ", end="")
# print(arr.pop(2))
# print("The array after popping is : ", end="")
# for i in range(0, 4):
#     print(arr[i], end=" ")

# print("\r")
# arr.pop(2)
# print("The array after removing is : ", end="")
# for i in range(0, 3):
#     print(arr[i], end=" ")


# import array as arr
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a = arr.array('i', l)
# print("Initial Array: ")
# for i in (a):
#     print(i, end=" ")
# Sliced_array = a[3:8]
# print("\nSlicing elements in a range 3-8: ")
# print(Sliced_array)
# Sliced_array = Sliced_array[2:]
# print("\nElements sliced from 5th "
#       "element till the end: ")
# print(Sliced_array)
# Sliced_array = a[:]
# print("\nPrinting all elements using slice operation: ")
# print(Sliced_array)


# import array
# arr = array.array('i', [1, 2, 3, 1, 2, 5])
# print("The new created array is : ", end="")
# for i in range(0, 6):
#     print(arr[i], end=" ")
# print("\r")
# print("The index of 1st occurrence of 2 is : ", end="")
# print(arr.index(2))
# print("The index of 1st occurrence of 1 is : ", end="")
# print(arr.index(1))


# import array
# my_array = array.array('i', [1, 2, 3, 4, 2, 5, 2])
# print("Number of occurrences of 2:", my_array.count(2))
# import array as arr 
# a = arr.array('i', [1, 2, 3,4,5])
# print("The before array extend  : ", end =" ")
# for i in range (0, 5): 
  
#     print (a[i], end =" ") 
    
# print()
# a.extend([6,7,8,9,10])
# print("\nThe array after extend :",end=" ")




# for i in range(0,10):  
  
#     print(a[i],end=" ") 
    
# print()



