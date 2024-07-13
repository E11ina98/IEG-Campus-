# to represent binaries in python
# we use 0b
# why we use 0b
# so that computer reads one zero one
# instead of reading 1 hundred and one
# because one zero one is equals to RM5 not RM101
givenbinary = 0b101

# filepermission = 755
filepermission = 0b111101001     
print(filepermission) # auto convert binary to decimal and print it
# you can use built in function called bin to print it as binary
print(bin(filepermission))
number = 97409
print(bin(number))

# filepermission holds a binary number and I am interested
# only in some bits not all
# for example i am interested only in permission belongs to the group
# which means i am interested in 4, 5, 6 bits only
# Feature Engineering
mask = 0b000111000  
# original            111 101 001       
# mask                000 111 000
# result              000 101 000
# the & operator is used for extracting the bits we are 
# interested
# let us shift to left 3 times
# result              000 000 101        >> 3

print(bin((filepermission & mask) >> 3))
print((filepermission & mask) >> 3)


# I want to set 4, 5, 6 bits to 1
# the other bits remain as it is then we use OR operator
# original            111 010 101       |
# mask                000 111 000
# result              111 111 101
filepermission = 0b111010101
mask = 0b000111000
print(bin(filepermission | mask))
# Using or operator you cannot set the bits to 0


# xor operator
#       and       or    xor
# 1 1    1        1     0
# 1 0    0        1     1
# 0 1    0        1     1
# 0 0    0        0     0

content = 0b10101010    # J
key = 0b00111100        # s
# I am going to encrypt J using s
# To decrpyt you must know s
encryptedcontent = content ^ key
print("Original content  ", bin(content))
print("Encrypted content ", bin(encryptedcontent))

decryptedcontent = encryptedcontent ^ key
print("Original content  ", bin(content))
print("Decrypted content ", bin(decryptedcontent))

# 1s compliment = flip the bits from 1 to 0 or 0 to 1
givennumber = 5         #  101
print(bin(~givennumber)) # 1 10  -6
print(~givennumber)
# get the 1s compliment and add 1
print(bin(~givennumber + 1))
print(~givennumber + 1)

print(-givennumber)   # unary negative
print(+givennumber)   # unary positive

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,  A,  B,  C,  D,  E,  F, 10, 11, 12, 13
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

hexadecimalnumber = 0xF
print(hexadecimalnumber)
print(hex(hexadecimalnumber))

# 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20
# 0, 1, 2, 3, 4, 5, 6, 7,  8,  9, 10, 11, 12, 13, 14, 15, 16

octalnumber = 0o10
print(octalnumber)
print(oct(octalnumber))








