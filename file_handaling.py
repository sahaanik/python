#file handling

file = open("demo.txt","r")

file1 = open("demo1.txt",'w')

file1.write("this is a new file")

print(file.read())
print(file1.read())

modes a=append, r=read, w=write

print(file.close())
