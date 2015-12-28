# mutating a list created with repetition
# initializing a variable with values
myList = [1,2,3,4]
# repetition
A = [myList]*3
myList[2] = 45
# output required
print(A)
print(myList[2])
print(myList[1:3])