
'''
# a
sum = 0
for j in range(1,21,1):
    sum = sum + j
print("Sum:", sum)
'''

'''
# b
while 1:
    print("infinitive while loop")
'''

# c
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