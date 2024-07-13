string= input()

#to check palindrome
isPal = string == string[::-1]
print(isPal)

if not isPal:
    revString = string[::-1]
    pal = string[:len(string)//2] + revString[len(string)//2:]
else:
    pal = string

print(pal)

