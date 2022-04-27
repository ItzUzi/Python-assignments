#Author: Uziel Gaeta
#Assignment: Lab2.Task_2
#Completed (or last revision): 2/2/2022

def main():
    # Asks User for info (name, age, company, salary)
    name = input("Please enter your name: ")    
    age = int(input("Please enter your age: "))
    company = input("Enter the company you wish to work: ")
    month_salary = int(input("Enter your monthly salary uou wish to earn in dollars: "))
    
    #Prints an empty line
    print()
    
    # Prints out formatted string 
    print("My name is %s, my age is %d" % (name, age)) 
    print("I hope to work for %s and earn %d a year" % (company, (month_salary*12)))


if __name__ == '__main__':
    main()

    
'''
PS C:\Users\uziel\Documents\School\Spring 2022\CS 2520\Labs\Lab2> & C:/Users/uziel/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/uziel/Documents/School/Spring 2022/CS 2520/Labs/Lab2/Task_2.py"
Please enter your name: Uziel Gaeta
Please enter your age: 19
Enter the company you wish to work: Amazon
Enter your monthly salary uou wish to earn in dollars: 12000

My name is Uziel Gaeta, my age is 19
I hope to work for Amazon and earn 144000 a year


PS C:\Users\uziel\Documents\School\Spring 2022\CS 2520\Labs\Lab2> & C:/Users/uziel/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/uziel/Documents/School/Spring 2022/CS 2520/Labs/Lab2/Task_2.py"
Please enter your name: Alice Wonderland
Please enter your age: 20
Enter the company you wish to work: Google
Enter your monthly salary uou wish to earn in dollars: 8000

My name is Alice Wonderland, my age is 20
I hope to work for Google and earn 96000 a year
'''