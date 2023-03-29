# python file for strings
name = input("Enter your name: ")
#"Ajit" -> name[0] "A", name[1] "j", name[2] "i", name[3] "t"
#print(name[0])
#print(name[1])
#print(name[2])
#print(len(name))
counter = 0
while counter < len(name):
    print(name[counter])
    counter = counter + 1

# join function
strList = ["Hello", name, "You are great at coding"]
#mylist = [1, 4, 6, 9]
#print(f"Hello {name}")
toPrint = " ".join(strList)
print(toPrint)





