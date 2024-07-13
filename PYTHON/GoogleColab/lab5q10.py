s = str(input("Enter any random string: "))
compressed = ""
count = 1

for i in range (len(s)-1):
    if s[i] == s[i +1]:
        count +=1
    else:
        compressed += s[i] + str(count)
        count = 1

if s:
    compressed += s[-1] + str(count)

print("The compressed string is: ",compressed)