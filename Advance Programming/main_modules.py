'''
All python scripts are modules and collection modules are package
pip is used to install packages
'''


def Demo():
    a = int(input('Enter a 1st number'))
    b = int(input('Enter 2nd number'))
    s = 0
    s = a + b
    return s
print(Demo())


print("I will run")
print(f'{__name__}')
def Solve():
    print("Python is best")

if __name__ == "__main__":      #...this cannot be imported as it is running from main file
    Solve()                     #...__name__ == main_module while importing
                                #...__name__ == "__main__" while running directly from main file