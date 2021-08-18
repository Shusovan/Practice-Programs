'''
We can import the whole module or we can import a part of it
'''

import main_modules         #...importing whole from main_module
main_modules.Solve()         #...calling the function

from main_modules import Demo           #...importing only the function
Demo()                                  #..calling the function


