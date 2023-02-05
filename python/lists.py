# A List is a collection which is ordered and changeable. Allows duplicate members.

#creat a list 

num_nm = [1,2,3,4,5]
fruits_nm = ['apple','banana','grapes','berry']

#use a constructor

#num_nm1 = list((1,2,3,4,5))
#print(num_nm , num_nm1)

#get a value 
print(fruits_nm[1])

#get lenght 
print(len(fruits_nm))

#append to list 
fruits_nm.append('pears')
print(fruits_nm)

#remove from a list 
fruits_nm.remove('banana')
print(fruits_nm)

#insert into position 

fruits_nm.insert(3,'strawberry')
print(fruits_nm)

#remove with pop 
fruits_nm.pop(2)

#reverse list 
fruits_nm.reverse() 
print(fruits_nm) 

#sort list 
fruits_nm.sort()

#reverse sort 
fruits_nm.sort(reverse=True)

#change values 
fruits_nm[1]='orange'




"""
and of course we will consider new fruits.nm is the base in every single time or we can simply remove " print(fruits_nm)" 
 from every line except the method u want 

"""

 