# Starting off
print(22/7)
print(355/113)
import math

print(9801 / (2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polgonCircumference  =  numSides * sideS
    pi = polgonCircumference / 2
    return pi


print(archimedes(8))
print(archimedes(16))

for sides in range (8, 5020000, 48):
    print(sides, archimedes(sides))


# experiment with the loop above alongside the actual value of Pi. How many
# sides does it take to make the two close?

# Accumulators

acc = 0
for x in range(1, 6):
    acc = acc + x

print(acc)

# Compute the sum of the first 100 even numbers

maximum = int(input("Please enter maximum value : "))
total = 0

for number in range(2, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number

print("The sum of even numbers from 1 to {0} = {1}".format(number, total))
# Compute the sum of the first 50 odd numbers

maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0

for number in range(1, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal))

# Compute the average if the first 100 odd numbers
# Write a function that returns the average of the first N numbers, where
#   N is a parameter
# Write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter
# Each number in the Fibonacci sequence is the sum of the previous two numbers.
#   The first two numbers in the sequence are 1 and 1. Compute the 10th
#   Fibonacci number.
# Write a function to compute the Nth Fibonacci number, where N is a parameter.
#   You may assime that N will be greater than or equal to 3.
