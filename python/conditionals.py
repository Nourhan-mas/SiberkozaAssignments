# If/ Else conditions are used to decide to do something based on something being true or false

x_nm  = 21
y_nm = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
#simple if 
#elif 
#if-else
'''
if x_nm > y_nm :
    print(f"{x_nm }is greater than {y_nm}") 

elif x_nm==y_nm : 
      print(f"{x_nm} is equal than {y_nm} ")

else : 
      print(f"{y_nm} is greater or equal than {x_nm}")
'''

#nested if 
'''
if x_nm > 2 :
    if x_nm <= 10 :
        print(f'{x_nm} is greater than 2 and less than or equal to 10 ')
'''

# Logical operators (and, or, not) - Used to combine conditional statements >> we will get the same outp of the previous line (nested if)

# and
if x_nm > 2 and x_nm <= 10 : 
     print(f'{x_nm} is greater than 2 and less than or equal to 10 ')

# or
if x_nm > 2 or x_nm <= 10 : 
     print(f'{x_nm} is greater than 2 and less than or equal to 10 ')

# not
if not (x_nm==y_nm): 
     print(f'{x_nm} is not equal to {y_nm} ')





# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

# in 
numbers_nm =[1,2,3,4,5]
if x_nm in numbers_nm:
    print(x_nm in numbers_nm) 

# not in 
numbers_nm =[1,2,3,4,5]
if x_nm not in numbers_nm:
    print(x_nm not in numbers_nm) 

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is 
if x_nm is y_nm : 
    print(x_nm is y_nm )

# is not
if x_nm is not y_nm : 
    print(x_nm is not y_nm )  
