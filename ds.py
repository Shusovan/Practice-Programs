#...datatypes...
'''
Nummeric - contains integer values
String - contaings sequence of characters
float - contain decimal values
boolean - it states true or false
lists - ordered sequence of objects, mutable
dictionary - key,value pair
sets - unordered collection of datatypes
tuple - immutable
'''

#string concatenation
str_1 = 'John'
str_2 = 'Rambo'
print(str_1+str_2)

#string indexing 
str_1 = "John Rambo"
print(str_1[5])

#string slicing
str_1 = "John Rambo"
print(str_1[5:])
print(str_1[0:9:2])

#uppercase and lowercase
str_1 = "John"
print(str_1.upper())
print(str_1.lower())

#...Lists...
#lists are mutable

arr_1= [1,2,3,"John"]   #...list can contain multi-datatype elements
print(arr_1)

arr = [4,2,3,1,8]   #...declaring a list
len(arr)            #...gives the length of the list

#list indexing
print(arr[2])   
print(arr[-1:])   #...to access the last element of list

#list slicing
print(arr[0:4])
print(arr[0::2])   #...three paramerters [start:stop:step] is used to step by 1 or more than 1

#adding element to list
arr = [4,2,3,1,8]
arr.append(10)   #...append() adds an element o the end of the list

list_1 = [1,2,3]
list_2 = [4,5,6]
list_1.extend(list_2)   #...the extend() function adds a list of element to the end of another list

arr = [4,2,3,1,8]
arr.insert(1,10)   #...this insert(position,element) function adds an element to a given position in list

#list concatenation
list_1 = [1,2,3]
list_2 = [4,5,6]
print(list_1 + list_2)

#removing elemennts
arr = [4,2,3,1,8] 
arr.remove(4)   #...remove(element) removes an element from list
arr.pop()       #...pop() removes element fron the end of list
arr.pop(1)      #...pop(index) removes element by index

#sorting a list using sort() function
arr = [4,2,3,1,8] 
arr.sort()   
print(arr)   

#sorting without sort function
#sorting without sorting algo
n = int(input())
a = list(map(int, input().split()))[:n]
for i in range(n):
    for j in range(i+1,n):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
print(a)

#reversing a list using reverse() function
arr = [4,2,3,1,8] 
arr.reverse()   
print(arr)

#reversing a list withut function
n = int(input())
m = list(map(int, input().split()))[:n]
print(m[::-1])


#...Tuple...
#tuples are immutable
new_tuple = (1,2,3)      #...declaring a tuple

#indexing
print(new_tuple[0])

#slicing
print(new_tuple[0:])

#count number of duplicates
tuple_1 = (1,2,1,1,3,1,'john','rambo')   #...mixed element in tuple
tuple_1.count(1)

#finding index of a number
tuple_1.index(3)
tuple_1.index(1)   #...for 1 it will show the first occurence index


#...Sets...
#sets only contain unique elements in ordered manner
set_1 = {3,7,9,9,1}   #...declaring a set
set_1.add(10)         #...adding element to set

#find the unique element in a list
list_x = [1,7,2,1,0,1]
set(list_x)


#...Dictionary...
new_dict = {"name":"Leonardo","age":45}   #...dictionary = {key:value}
print(new_dict["name"])                   #...printing the value

new_dict['gender'] = "male"               #...this key and value is added at the end of dictionary

new_dict.keys()                           #...this function is used to print the keys

new_dict.values()                         #...this function is used to print the values

new_dict.items()                          #...for printing all the key-value pairs

dict_new = {"Student":"John","Marks":[80,90,100]}   #...adding multiples values
dict_new['Marks']