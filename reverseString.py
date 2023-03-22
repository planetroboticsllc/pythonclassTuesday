# python code for reversing a string
def reverseString(a):
    rev = ""
    counter = len(a) - 1
    while counter >= 0:
        rev = rev + a[counter]
        counter = counter - 1

    return rev

def isPalindrome(a):
    rev = reverseString(a)
    if rev == a:
        return True
    else:
        return False

name = input("enter name: ")
password = input("enter password: ")
#revString = reverseString(name)
#print(revString)

# write a code that says if the string is palindrome or
# if the string is not a palindrome
if isPalindrome(name):
    print("This is a palindrome!")
else:
    print("This is not a palindrome")
