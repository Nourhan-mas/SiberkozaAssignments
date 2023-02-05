# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#creat dic 
person_nm ={
    "first_name":"joe",
    "last_name":"nour",
    "age":19
}
print(person_nm,type(person_nm)) 

#use a constructor 
#person_nm1=dict(first_name="sara",last_name="willy")
#print(person_nm1,type(person_nm1))

#get value 
print(person_nm["first_name"])
print(person_nm.get("last_name"))

#add value 
person_nm['phone']= '100-100-1000'
print(person_nm)

#get dic keys 
print(person_nm.keys())

#get dic items
print(person_nm.items())

#copy dic 
person_nm1=person_nm.copy()
person_nm1['city']='Ramallah'
print(person_nm1)

#remove an item > two ways 
del(person_nm["age"])
person_nm.pop('phone')
print(person_nm)

#clear a dic
person_nm.clear()
print(person_nm)

#get lenght 
print(len(person_nm1))

# list of dic 
people = [
    {"name":"mary","age":20},
    {"name":"losy","age":15} 
    ]
print(people)
print(people[0]["name"])




# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
