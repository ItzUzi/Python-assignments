#Author: Uziel Gaeta
#Assignment: Lab2.Task_1
#Completed (or last revision): 2/2/2022

def task1():
    age1 = 18
    age2 = 19
    age3 = 22
    age4 = 23
    age5 = 30
    age6 = 17
    avg_age = ((age1 + age2 + age3 + age4 + age5 + age6) / 6)
    print("average age is:", avg_age)

def task2():
    print("2 to the 120th power is:", (2**120))

def task3():
    print("1/3 of 15 is: ", ((1/3) * 15))
    
def task4():
    str1 = "hi"
    str2 = "bye"
    fnl_str = str1 + str2
    print(fnl_str)
    
def task5():
    str1 = "hello"
    fnl_str = str1 * 3
    print(fnl_str)
    
def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    
if __name__ == '__main__':
    main()
