#name: Uziel Gaeta
#Lab 3

#problem 1
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)

'''
Enter a number: 34
Enter a number: 12
Enter a number: 104
104

Enter a number: 32
Enter a number: 321
Enter a number: 43
321

Prints out the largest number inputed by the user
'''

#problem 2
count = int(input("please enter the number of items purchased: "))
total = int(input("please enter the total cost: "))
print("Average =", 0 if count == 0 else total/count)

'''
please enter the number of items purchased: 20
please enter the total cost: 60
Average = 3.0


please enter the number of items purchased: 0
please enter the total cost: 0
Average = 0
'''

#Problem 3
## a
i = 1
while i < 10:
    print(i, end = " ")
    i = i + 2
    if i == 5:
        i = 9
'''
1 3 9
'''

## b
for j in range(1,10,2):
    print(j, end = " ")
    if j == 5:
        j = 9

'''
1 3 5 7 9
'''

#Problem 4
## a
sum = 0
for j in range(1,21,1):
    sum = sum + j
print("Sum:", sum)
'''
Sum: 210
'''

## b
#while 1:
#    print("infinitive while loop")
'''
infinitive while loop
infinitive while loop
infinitive while loop
...
'''

## c
number = int(input("Enter a number to check Prime or Not: "))
i = 2; count = 0
while i <= (number / 2):
    if number % i == 0:
        count += 1
        break
    i += 1
if count == 0:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
    
'''
Enter a number to check Prime or Not: 37
37 is a prime number

Enter a number to check Prime or Not: 35
35 is not a prime number
'''