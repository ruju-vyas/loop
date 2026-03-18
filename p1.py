#Types of for loops
#1.for loop 
#used when we know how many times we want to repeat

#Syntax
# for variable in sequence:
#     #code

#2.While loop 
#used when we repeat until a condition become false

#Syntax
# while condition:
#     #code

#example
# i=1
# while i==3:
#     break
# print(i)

#loop control statement

#1.break
#stops the loop immediately
#example
# for i in range(1,6):
#     if i==3:
#         break
#     print(i)

# #continue
# #skips current iteration

# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)

# #3.pass
# #does nothing (placeholder)
# for i in range(5):
#     pass


#Task:1
# print 1 to 5 using for loop

for i in range(1,11):
    print(i)

# #Task:2
# #print a number from 1 to 20
for i in range(1,21):
    if(i %2==0):
        print(i)  

for i in range(1,21,2):
        print(i)

#Task:3
#print odd number from 1 to 10

for i in range(1,16,2):
        print(i)

#Task:4
#print each character of the string
text='pyhton'

for i in text:
        print(i)

# #Task:5
# #print all items in the list
data=['data','science','AI']
for i in data:
        print(i)

#Task:6
# Find the sum of numbers from 1 to 10c
a = 0
for i in range(1, 11):
    a += i

print(a)

# #Task:7
# #print multiplication table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

#Task:8
#count how many vowels are in string
text='Hello World'


vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)


#Task:9
#print numbers in reverse order from 10 to 1
for i in range(10, 0, -1):
    print(i)

#Task:10
#print squre of number from 1 to 5
for i in range(1, 6):
    print( i * i)