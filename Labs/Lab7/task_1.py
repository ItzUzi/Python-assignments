def q_1():
    """
    Prints all lines of the text doc, 'mydata.txt'
    """

    inf = open('mydata.txt', 'r')
    for line in inf:
        print(line)
    inf.close()


def q_2():
    """
    There is an extra blank line because the last element in
    each line is \n
    """

    '''
    Prints each line in text doc, 'mydata.txt' without extra
    new line
    '''

    inf = open('mydata.txt', 'r')
    for line in inf:
        line = line.rstrip('\n')
        print(line)
    inf.close()

'''
Q3:
If you try to open a file to read it and it doesnt exist,
the program terminates and throws an error

If you try to write on a file that doesnt exist, then it
creates a new file with the same name and you can write on it

If you try to write on a file that already exists, then it replaces
everything in the file with what you're gonna write
'''


def q_4():
    """
    Creates a new file 'newRainfall.txt' with rainfall being measured
    in cm instead of inches
    Data taken from rainfall.txt
    """
    inf = open('rainfall.txt', 'r')
    inches = list()
    names = list()
    for line in inf:
        string = line.split(' ')
        names.append(string[0])
        inches.append(float(string[1]))
    inf.close()

    outf = open('newRainfall.txt', 'w')
    for i in range(len(names)):
        cm = str(round((inches[i] * 5.54), 2))
        outf.write(names[i] + ' ' + cm + '\n')
    outf.close()

    inf = open('newRainfall.txt', 'r')
    for line in inf:
        line = line.rstrip('\n')
        print(line)
    inf.close()


def q_5():
    """
    writes the files 'data1.txt' and 'data2.txt' using 2 different methods
    prints out contents in order to compare them
    """
    # write strings one by one, i.e. write(str)
    fp = open("data1.txt", 'w')
    fp.write("hello\t")
    fp.write("how are you")
    fp.write("\n")
    fp.write("thank you ")
    fp.write("bye\n")
    fp.close()

    # writelines(): write a sequence, i.e. a list or a tuple into a file
    fp = open("data2.txt", 'w')
    fp.writelines(["hello\t", "how are you", "\n", "thank you ", "bye\n"])
    fp.close()

    print("\ndata1:")
    fp = open("data1.txt", 'r')
    for line in fp:
        print(line)
    fp.close()

    print("\ndata2:")
    fp = open("data2.txt", 'r')
    for line in fp:
        print(line)
    fp.close()


def main():
    # q_1()
    print("Task_2", end='\n\n')
    q_2()
    print("\nTask_4", end='\n\n')
    q_4()
    print("\nTask_5", end="\n\n")
    q_5()


if __name__ == '__main__':
    main()

"""
Output:
Task_2

We can't touch
But we still reach out
We hunker down
But we still rise up

Task_4

Akron 142.99
Albia 208.58
Algona 170.02
Allison 186.37
Alton 151.96
AmesW 188.75
AmesSE 188.08
Anamosa 195.73
Ankeny 184.93
Atlantic 192.63
Audubon 186.2
Beaconsfield 195.4
Bedford 201.38
BellePlaine 198.39
Bellevue 190.3
Blcokton 200.99
Bloomfield 210.63
Boone 201.1
Brighton 186.09
Britt 174.73
Buckeye 186.48
BurlingtonKBUR 210.19
Burlington 204.65
Carroll 184.65
Cascade 185.48
Daly 211.74
Delmar 156.23

Task_5


data1:
hello	how are you

thank you bye


data2:
hello	how are you

thank you bye
"""