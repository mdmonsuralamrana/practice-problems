# input 2 integer number and sum them

firstNumber = int(input("Enter first Number:  "))
secondNumber = int(input("Enter second Number: "))
sum = firstNumber + secondNumber

print("Total of them: ", sum)

# factorial of number

number = int(input("Enter a number: "))
factorial = 1 
if number < 0:
    print("Factorial does not exist for negative number")
elif number == 0 :
    print("Factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial*i
        print("The factorial of number ", number, "is", factorial)

# output [The factorial of number  9 is 362880]


# read 3 numbers from keyboard and print the biggest number 
    #if ask for smallest, then every > will be < only. 

num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))
num3 = int(input("Enter the third Number: "))

if (num1>num2) and (num1>num3):
    print("First Number is biggest")
elif (num2> num1) and (num2>num3):
    print("Second Number is biggest")
else:
    print("Third Number is biggest")


# input 3 length for make an triangle

import math
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

if ((a+b)>c and (b+c)>a and (a+c)>b):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the triangle is: ", area)
else:
    print("triangle is not possible")


#input a number and check it odd or even using if-else

n = int(input("Enter the value for n: "))
if (n%2) == 0 :
    print("The number is even")
else:
    print("The number is odd")


#input a year and check it leap year or not!

year = int(input("Enter a year: "))

if ((year%100 == 0) and (year%400 ==0) or (year%4 == 0)):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")