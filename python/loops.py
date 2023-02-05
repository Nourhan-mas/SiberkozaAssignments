# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_nm = ['nour','ali','sara','rami']

#simple for loop 
'''
for person_nm in people_nm :
    print(f'current person_nm: {person_nm }')
'''
#break
'''
for person_nm in people_nm :
    if person_nm == 'sara':
     break
    print(f'current person_nm: {person_nm }')
'''
# continue

for person_nm in people_nm :
    if person_nm == 'sara':
     continue
    print(f'current person_nm: {person_nm }')

# range >> same as the previous but in another way  
"""
for i in range(len(people_nm)) : 
    print(people_nm[i])

for i in range(0,11):
    print(f'number:{i} ')    
"""

# While loops execute a set of statements as long as a condition is true.

count = 0 
while count <= 10 :
    print(f'count :{count} ')
    count += 1
    