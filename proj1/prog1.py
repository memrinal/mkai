# This program demonstrates number manipulation using both Fibonacci-like sequence and linear increment
# It combines two different approaches:
# 1. A for loop that generates a sequence similar to Fibonacci but with modified rules
# 2. A while loop that performs simple linear increment

# Get input numbers from user
num1 = float(input("Enter first number: "))  # First number - used as a threshold in the for loop
num2 = float(input("Enter second number: "))  # Second number - used as loop limit and final target

# Initialize variables for the Fibonacci-like sequence
i = 1  # First number in sequence
j = 1  # Second number in sequence

# This for loop generates a modified Fibonacci-like sequence where:
# - i gets incremented by j
# - j gets updated to the sum of previous i and j
# - Values are printed when they exceed num1
for i in range(1, int(num2)):
    if num1 < i:
        print("Current value:", i)  # Print values that exceed the first input number
    i = i + j    # Update i by adding j
    print("i is:", i)
    j = i + j    # Update j by adding new i
    print("j is:", j)   # This creates a rapidly growing sequence
# Reset variables for the linear increment phase
i = num1  # Start from the first input number
j = num2  # Use second input number as target

# Simple linear increment loop
# Counts up from num1 to num2 one by one
while i < j:
    i = i + 1
    print(i, " i in while loop")

# Display final result
# Note: The final value of i will be equal to num2
print("The sum is:", i)