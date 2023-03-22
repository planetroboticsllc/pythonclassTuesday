# ask user names of 3 fruits: fruit1, fruit2, fruit3
# then create a list of 3 fruits
# then print list of fruits using join function, with ,
# mango, apple, banana
# create a function with input as list
# the function will print list with ,
def printList(strList):
    toPrint = ", ".join(strList)
    print(toPrint)

a = input("Enter fruit1: ")
b = input("Enter fruit2: ")
c = input("Enter fruit3: ")
fruitList = [a, b, c]
printList(fruitList)
printList(["Hello", "world"])

