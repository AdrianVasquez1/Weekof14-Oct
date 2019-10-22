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

# Compute the sum of the first 50 odd numbers

maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0

for number in range(1, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal))

# Compute the average if the first 100 odd numbers
total = 0
length = 0
for i in range(1, 200, 2):
    total += i
    length += 1

print(total / length)
# Write a function that returns the average of the first N numbers, where
#   N is a parameter
print ("calculate an average of first n natural numbers")
n = input("Enter Number ")
n = int (n)
average = 0
sum = 0

for num in range(0,n+1,1):
    sum = sum+num;
average = sum / n
print("Average of first ", n, "number is: ", average)
# Write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
# Each number in the Fibonacci sequence is the sum of the previous two numbers.
#   The first two numbers in the sequence are 1 and 1. Compute the 10th
# #   Fibonacci number.
FibArray = [0,1]
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib


print(fibonacci(10))
# Write a function to compute the Nth Fibonacci number, where N is a parameter.
#   You may assume that N will be greater than or equal to 3.
FibArray = [0,1]
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib


print(fibonacci(n))

# A Monte Carlo Simulation

import random

print(random.random())

# Boolean expressions
# > greater than
# >= greater than ir equal to
# < less than
# <= less than or equal to
# == the same as [ equal to ]
# != NOT equal to

dogWeight = 25
print(dogWeight != 25)
catWeight = 15

# compound Boolean operators
# and
# or
# not

print(dogWeight > 30 and catWeight > 20)
print(not catWeight < 20)

# Decision Making -- Selection Statements

a = 5
b = 10
c = 75

if a > b :
    c = 45
    if b > c:
        a = 25
    else:
        a = -25
else:
    c = 1050
    if b == a:
        c = 25

print(a, b, c)

d = 55
e = 72
f =44
ans = 0
if d > e:
    ans = 12
else:
    if d == e:
        ans = 50
    else:
        if f < d * e:
            ans =100
        else:
            ans = 75

print(ans)

def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi

print(montePi(10000))

import turtle

def showMontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-2,-2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(0, 1)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        t.goto(x, y)

        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")
        else:
            t.color("red")

        t.dot()

    pi = inCircle / numDarts * 4
    scn.exitonclick()
    return pi

showMontePi(1000)

# Your Task:
# Modify the simulations to plot points in the entire circle. You will have to
# adjust the calculated value of pi accordingly.