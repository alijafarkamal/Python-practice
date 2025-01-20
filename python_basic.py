# def sum_array(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum += arr[i]
#     summa = 0
#     for item in arr:
#         summa += item
#     return summa


# print(sum_array([1, 2, 3, 4]))  # Output: 10
# def factorial(num):
#     factorial_result = num-1
#     for i in range(num-1):
#         num = num*factorial_result
#         factorial_result -= 1
#         # if(factorial_result==0):
#         #     break

#     return num


# print(factorial(5))  # Output: 120

# def find_max(arr):
#     max_number = arr[0]
#     for item in arr:
#         if(item>=max_number):
#             max_number = item
#     return max_number
# print(find_max([1, 3, 2, 5, 4]))  # Output: 5

# def transpose_matrix(matrix):
#     for row in matrix:
#         for col in row:
#             print(col, sep= ',')
#         print('\n')
def transpose_matrix(arr):
    rows = len(arr)
    cols = len(arr[0])
    transposed = [[None]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = arr[i][j]
    return transposed
    # for row in arr:
        # print(*row)
        # print(' '.join(str(element) for element in row))
    # for i,row in enumerate(arr):
    #     for j,element in enumerate(row):
    #         if(j>i):
    #             temp = element
    #             element = arr[j][i]
    #             arr[j][i] = temp
    # return arr
    #         print(element.index)
    #         print(element, end=',')
    #     print()  

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(transpose_matrix(matrix) ) # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# def fibonacci(num):
#     numbers = [None]*num
#     numbers[0] = 0
#     numbers [1] = 1
#     for i in range(num-2):
#         numbers[i+2] = numbers[i+1] + numbers[i]
#     return numbers
# print(fibonacci(10))  # Output: [0, 1, 1, 2, 3]

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Other even numbers are not primes 
    # Check for factors from 3 up to the square root of n
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False 
    return True

# print(is_prime(15))  # Output: True
def reverse_elements(arr):
    reverse_index = len(arr)-1
    for i in range(int(len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[reverse_index]
        arr[reverse_index] = temp
        reverse_index -= 1
    return arr

#print(reverse_elements([1,2,3,4,5]))

def is_palindrome(arr):
    palin_checker  = len(arr)-1
    for i in range(int(len(arr)/2)):
        if(arr[i]!=arr[palin_checker]):
            return False    
        palin_checker -= 1
    return True
# print(is_palindrome([5,4,3,4,5]))

def print_prime(num):
    arr = [None]*num
    num_generator = 5
    arr[0] = 2
    arr[1] = 3
    index = 2
    prime = False
    while index<=num-1:
        for i in range(3,int(num_generator**0.5)+2,2):
            print(num_generator)
            if num_generator%i==0:
                prime = False
                break
            else:
                prime = True
        if(prime):
            arr[index] = num_generator
            index+= 1
        num_generator += 2
    return arr
# print(print_prime(10))
def count_vowels(sentance):
    count = 0
    vowel_container = 'aeiouAEIOU'

    for item in sentance:
        # if(vowel_container.__contains__(item)):
        if item in vowel_container:
        # if(item=='a' or item=='e' or item=='i' or item=='o' or item=='u'
        # or item=='A' or item=='E' or item=='I' or item=='O' or item=='U'):
            count += 1
    return count
# print(count_vowels('Hello world'))


class car:
    make = ''
    model = ''
    year = 0
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f'Car making is {self.make}')
        print(f'Car model is {self.model}')
        print(f'Car year is {self.year}')


Toyota = car('y21','classic','1997')
# Toyota.display_info()

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")


class car(Vehicle):
    def __init__(self,make,model,numwheels):
        super().__init__(make,model)
        self.numwheels = numwheels
    def display_info(self):
        super().display_info()
        print(self.numwheels)


vehicle1 = Vehicle("Toyota", "Camry")
vehicle1.display_info()  # Output: Make: Toyota, Model: Camry

car1 = car("Honda", "Accord", 4)
car1.display_info()    

