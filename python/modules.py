# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules


# core modules 

import datetime 
from datetime import date # if we use this then no need to put datetime with the following line
'''today = datetime.date.today() '''
import time
from time import time 

# import custom module 
import validator 
from validator import validate_email 

# pip modules >> usually u have installing it , write this in the terminal 'pip3 install camelcase '
# from camelcase import CamelCase 

today = date.today()
timeStamp = time()
print(today)
print(timeStamp) 

'''
c = CamelCase()
print(c.hump('hello there world')) 
'''

email ='lala@lala.com'
if validate_email(email):
    print("email is valid")
else : 
    print("email is undefined ")