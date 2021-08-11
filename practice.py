#the three cup monte game in python
from random import shuffle

def three_cup_monte():
    cups = ["","0",""]       #...list of cups
    shuffle(cups)            #...shuffling the cups
    guess = int(input("Enter any choice between 0, 1 and 2 : "))
    if cups[guess] == "0":   #...if the guess is correct, the 'if' statement executes
        return "Correct"
    else:                    #...if the guess is wrong, the 'else' statement is executed
        return "Wrong"
print(three_cup_monte())     #...calling the function

#list comprehension
def comp():
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if "a" in x]
    return newlist
print(comp())

#reverse a string
def rev():
    s = input()
    l = len(s)
    string = s[l::-1]
    return string
print(rev())

#count number of word in sentance
def number_of_words():
    s = input()
    res = len(s.split())
    return res
print(number_of_words())

#minimum and maximum in array
n = int(input())
a = list(map(int, input().split()))[:n]
mini = a[0]
for i in range(n):
    if a[i] < mini:
        mini = a[i]
maxi = a[0]
for i in range(n):
    if a[i] > maxi:
        maxi = a[i]
print(mini, end=' ')
print(maxi)

#Kth min and max of array
n = int(input())
k = int(input())
m = list(map(int, input().split()))[:n]
m.sort()
for i in range(k):
    print(m[i],end=' ')

#Leap Year
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap year")

#union of two array
m = int(input())
n = int(input())
arr1 = list(map(int, input().split()))[:m]
arr2 = list(map(int, input().split()))[:n]
i,j = 0,0
while i < m and j < n:
    if arr1[i] < arr2[j]:
        print(arr1[i],end=' ')
        i += 1
    elif arr2[j] < arr1[i]:
        print(arr2[j],end=' ')
        j += 1
    else:
        print(arr2[j],end=' ')
        j += 1
        i += 1
while i < m:
    print(arr1[i],end=' ')
    i += 1
while j < n:
    print(arr2[j],end=' ')
    j += 1

#intersection of two arrays
m = int(input())
n = int(input())
arr1 = list(map(int, input().split()))[:m]
arr2 = list(map(int, input().split()))[:n]
i,j = 0,0
while i < m and j < n:
    if arr1[i] < arr2[j]:
        i += 1
    elif arr2[j] < arr1[i]:
        j += 1
    else:
        print(arr2[j],end=' ')
        j += 1
        i += 1

#duplicates characters of string
s = input()
n = len(s)
for i in range(n):
    for j in range(i+1,n):
        if s[i] == s[j]:
            print(s[i],end=' ')

#common of any array
n1 = int(input())
a1 = list(map(int,input().split()))[:n1]
a2 = list(map(int,input().split()))[:n1]
a3 = list(map(int,input().split()))[:n1]
'''converting the list to set'''
s1 = set(a1)   
s2 = set(a2)
s3 = set(a3)
'''set has attribute intersection'''
set1 = s1.intersection(s2)   
result = set1.intersection(s3)
print(list(result))

#vowels or consonants
s = input()
vowels = 0
consonents = 0
for i in range(len(s)):
    ch = s[i]
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowels += 1
        else:
            consonents += 1 
print("vovels", vowels)
print("consonents", consonents)

