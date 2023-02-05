# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# simple normalization 

#x.no = 5            # int
#name_ = 'nour'    # string 
# y.no = 5.5          # float 
#is_no = True      # boolean 

# we turn them into comments cuz we can't normalize them twice 

# muliple assignment

x_nma , name_nma , y_nma, is_nma = (5,'Nourhan', 5.5 , True)

print("x_nma") 

# basic math
z= x_nma + y_nma 

#casting

x_nma = str(x_nma)
y_nma = int(y_nma)

#it will print the new type of x_nma 

print(type(x_nma)) 



