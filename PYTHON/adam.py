num = int(input("Enter the number: "))   #153

#find square of input
square_input= num**2        #23409
print ("Square of input number:" ,square_input)

#find reverse of input
reverse = 0
             #0             #3             
reverse = (reverse * 10) + num % 10  #3
num = num // 10     #15
                #30        #5
reverse = (reverse * 10) + num % 10  #35
num = num // 10     #1
            #350            1
reverse = (reverse * 10) + num % 10  
num= num // 10     #0

print("Reverse of the input number:" ,reverse)

# find square of reverse
square_reverse= reverse **2
print("Square of the reverse number:",square_reverse)  

#Reverse the square of the reversed number
reversed_square_reverse=0
                     
reversed_square_reverse = (reversed_square_reverse * 10) + square_reverse % 10 
square_reverse = square_reverse // 10     
              
reversed_square_reversee = (reversed_square_reverse * 10) + square_reverse % 10  
square_reverse =square_reverse // 10     
           
reversed_square_reverse = (reversed_square_reverse * 10) + square_reverse % 10  
square_reverse= square_reverse // 10     
print("Reverse of the square reverse:",reversed_square_reverse)

#check adam number
if (square_input == reversed_square_reverse):
    print("Adam number")
else:
    print("not Adam number")






