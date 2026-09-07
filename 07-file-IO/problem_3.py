# WAP a program to rename a file 

with open("file.txt") as a:
    b =a.read()

with open("rename.txt","w") as c:
    c.write(b)

''' 
in this above program we create a duplicate file 
and gives the other name to that to delete 
the old file we haev to use other libraries
'''