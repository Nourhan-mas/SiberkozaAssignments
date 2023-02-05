# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#creat tuple 
fruits_nm = ("apple","orange","grapes")
#fruits_nm1 = tuple(("apple","orange","grapes"))
#print(fruits_nm ,fruits_nm1)

fruits_nm2 = ("apple")
print(fruits_nm2,type(fruits_nm2))

#get value 
print(fruits_nm[2])

# we can't change values like this >> fruits.nm[1]="orange" 

#delete a tuple 

del fruits_nm2 
#print(fruits_nm2)

#get length 
print(len(fruits_nm))





# A Set is a collection which is unordered and unindexed. No duplicate members.

fruit_setnm ={"apple","orange","grapes"}

#check if an item is in th set 
print("apple"in fruit_setnm)

#add to set 
fruit_setnm.add("grape")
#print(fruit_setnm)

#remove from a set 
fruit_setnm.remove("grape")

#clear set > it gonna be an {empty} set 
fruit_setnm.clear()
print(fruit_setnm)

#delete a set > means gonna be undefined 
del fruit_setnm 
print(fruit_setnm)



# we can't insert any item that already there like this >> add duplicate : fruit_setnm.add("apple")