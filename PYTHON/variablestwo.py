# so far we learn how to assign a single value to a 
# single variable and we also learn how to assign
# multiple values to mutliple variables
fruit = "apple"
fruit01, fruit02 = "apple", "orange"

fruits = ["apple", "orange", "mango", "banana", "grapes"]

# indexing and selection
print(fruits) # ["apple", "orange", "mango", "banana", "grapes"]
print(fruits[0]) # apple
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4]) # grapes

# how many items we have in the list
# you can get it using the function len
print("Number of Items:", len(fruits)) # 5

# what is the maximum index
print("Maximum Index:", len(fruits) - 1)

# Can we have negative index
print(fruits[-1]) # the last item which is grapes
print(fruits[-2]) # last but before item banana
print(fruits[-3])
print(fruits[-4])
print(fruits[-5])
# Maximum index in negative is same as number of items

# In python we have something called Range
# start_index:end_index
# this process is also call slicing
print(fruits[1:3]) # 3 is excluded
print(fruits[1:4])
print(fruits[:4]) # since start index is not mention
# it will start from zero 0 (index) [beginning]
print(fruits[0:]) # since end index is not mention
# it will go until to the last item
print(fruits[:])

fruits = ["apple", "rambutan", "orange", "durian", "mango", "papaya", "banana", "grapes"]
# The range can also have 3rd argument, which is step up argument
print(fruits[0:8])
print(fruits[0:8:2])
print(fruits[0:8:3])

# start index must be less than end index
print(fruits[-5:-1]) # grapes did not come out because -1 is not included
print(fruits[-1:-5]) # start index is greater than end index []
# the reason is default step up value is 1
print(fruits[-1:-5:-1]) # it reverse the list already
# to reverse the entire list
print(fruits[::-1])

