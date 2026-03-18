#What is Function?
#A function is a block of code that runs only when it is called.

#Why use function?
#1.Avoid repeating code
# make progrma clean & organized 
#easy to debug and reuse

#example:
# def greet():
#     print('hello world')
# greet()

# #Function with parameter
# #used to pass values
def greet(name):
    print('hello',{name})
greet('krisha')

def add(a,b):
    return a + b
result = add(2,3)
print(result)

#Task:1
#Create a calculator
def calc(a, b):
    print("Add:", a + b)
    print("Sub:", a - b)
    print("Mul:", a * b)
    print("Div:", a / b)

calc(10, 5)

# #Task:2
# #create a function to chech if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(5)

def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

number = int(input("Enter a number: "))
check_even_odd(number)

#Task:3
#create a function to find the factorial
num = int(input("Enter a number: "))

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

print("Factorial:", factorial(num))

#Task:4
#create function to find maximum of three numbers
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
a=float(input("enter a: "))
b=float(input("enter b: "))
c=float(input("enter c: "))
print(find_max(a,b,c))

#Task:5
#Create a funtion to check if a string is palindrom 
input='madam'
def is_palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

text = input("Enter a string: ")
is_palindrome(text)

#Task:6
#create a function to calculate the area of circle 
def area_circle(r):
    return 3.14 * r * r

r= float(input("Enter radius: "))

print("Area:", area_circle(r))