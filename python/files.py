# Python has functions for creating, reading, updating, and deleting files.

#open a file 
myfile_nm = open('myfile_nm.txt', 'w') 

#get some informations 
print('name :', myfile_nm.name)
print('is closed :', myfile_nm.closed)
print('opening mode :', myfile_nm.mode)

# write to file 
myfile_nm.write ('I love python') 
myfile_nm.write (' and javascript') 
myfile_nm.close()

#append to file 
myfile_nm = open('myfile_nm.txt', 'a') 
myfile_nm.write('I also like PHP')
myfile_nm.close()

# read from a file 
myfile_nm = open('myfile_nm.txt', 'r+')
text_nm = myfile_nm.read(100)
print(text_nm) 