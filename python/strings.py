# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name_nm = "nour"
age_nm = 19 

#concatenate > the first way to casting 

#print('my name_nm is'+ name_nm + 'and I am ' + str(age_nm))

# String Formatting

# Arguments by positions > the second way 

#print('my name_nm is {name_nm} and I am {age_nm}'.format(name_nm = name_nm, age_nm = age_nm)) 

# String Methods
s_nm = 'hello all' 

#capitalize string > printing some strings in undirect way 
print(s_nm.capitalize())

# make all uppercase 
print(s_nm.upper())

# make all lowercase 
print(s_nm.lower())

# swap case 
print(s_nm.swapcase())

# get lenght 
print(len(s_nm))

# replace 
print(s_nm.replace('all','world'))

#count 
sub = 'h'
print(s_nm.count(sub)) 

#starts with 
print(s_nm.startswith('hello'))

#ends with 
print(s_nm.endswith('l'))

#split into a list 
print(s_nm.split())

#find position
print(s_nm.find('a'))

#is all alphanumeric
print(s_nm.isalpha())

#is all numeric 
print(s_nm.isnumeric())

