'''
Memory Management
Python performs memory optimisation
The objects are stored in the heap memory
The methods and variables are stored in stack memory contiguously
When a reference becomes 0 (called dead object) the garbage collector removes the object from the memory
Algorithm used for garbage collector is Reference Counting  
'''

# an empty list takes 56 bytes of memory and 8 butes for each integer value
import sys
x = 100
y = x                       # x and y refers to same memory location
print(id(x))                # id is a built-in function that returns a unique identity for a specified object
print(sys.sizeof(x))        #...sizeof function gives size of an object
if id(x) == id(y):
    print("Both refer to same object")

# o/p - 140719564051200

# empty string contains 49 bytes of memory, 1 byte for each character 
name = "Shusovan"
print(id(name))
print(sys.sizeof(name))        #...gives size of an object

# o/p - 2722503981808

'''
GIL - Global Interpreter Lock
It allows only one thread to work at a time

Due to GIL, Python provides a better way to deal with thread-safe memory management

Python has something that no other language has that is a reference counter, 
it helps to find the total number of reference made internally and when the 
reference becomes zero, the object is released from memory.
'''

# Time taken by CPU
 
import time
from threading import Thread
count = 50000000
def countdown(n):
    while n>0:
        n -= 1
  
start = time.time()
countdown(count)
end = time.time()
  
print('Time taken in seconds -', end - start)

