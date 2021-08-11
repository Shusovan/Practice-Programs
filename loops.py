#...for loops...
arr = [1,6,2,7,9,3]
for i in arr:        #...declaring a for loop
    print("i")

arr = [1,2,3,4]
for i in arr:
    print("hello")

#...if else statement...
arr = [1,2,3,4,5]
for i in arr:
    if i % 2 == 0:      #...declaring if statement
        print(f'{i} is Even')
    else:               #...declaring else statement
        print(f'{i} is Odd')

#sum of a list
n = int(input("Enter list elements: "))
arr = list(map(int,input().split()))[:n]
s = 0
for i in range(n):
    s = s + arr[i]
print(s)

#tuple unpacking
list_tup = [('John','Rambo'),('Leonardo','Decaprio')]
for i,j in list_tup:
    print(i)

#using for loop in dictionary
new_dict = {'Name':'John','Age':20}
for i in new_dict.items():           #...for printing only key use key() and values use values()
    print(i)

#while loop
n = 0
while n<=5:
    print(n)
    n=n+1

#spliting a string
msg = "world"
index_count = 0
for char in msg:
    print(f'{char} is at index {index_count}')
    index_count = index_count + 1

#enumerate and tuple unpacking
msg = "hello"
for i,j in enumerate(msg):
    print(i)

#zip function
list_1 = ['John','Leonardo']
list_2 = [75,55]
for i in zip(list_1,list_2):
    print(i)

#*args and **kwargs
def args(*args):
    for i in args:
        print(i)
args("John","Rambo")

def kwargs(**kwargs):
    for i,j in kwargs.items():
        print ("%s -> %s" %(i,j))
kwargs(Name="John",Age=75)
