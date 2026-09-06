# a file.txt contain some word we have to replace them in **
words = ["bad","ganda","donkey"]

with open("file.txt") as a:
    content = a.read()

for word in words:
    content = content.replace(word,"**")

with open("file.txt","w") as c:
    c.write(content)