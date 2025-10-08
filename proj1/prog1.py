# Simple Python program to add two numbers

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

i = 1
j = 1
# For loop till num1 is equal to num2
for i in range( 1, int(num2) ):
    if num1 < i:
        print("Current value:", i)
    i = i + j
    print("i is:", i)
    j = i + j
    print("j is:", j)
i = num1
j = num2
while i < j:
    i = i + 1
    print (i , " i in while loop")


# Display the result
print("The sum is:", i)