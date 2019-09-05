#Start by getting the input for the sequence
# The program will add the first 3 numbers and then always the 3 numbers after that
# this will be done until the the number of the sequence.


n = int(input("Enter the length of the sequence: ")) # Do not change this line

A = 1 
B = 2 
C = 3 

count = 0 

while count < n - 3: 
    if count < 1: 
        print (A)
        print(B)
        print(C)
    count += 1
    D = A + B + C
    A = B
    B = C
    C = D
    print(D)