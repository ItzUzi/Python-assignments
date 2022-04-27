def task_1():
    inf = open('scores.txt', 'r')
    for line in inf:
        line = line.rstrip()
        print(line)
    inf.close()


def task_2_and_3():
    str_list = list()
    inf = open('scores.txt', 'r')
    for line in inf:
        str_list.append(line.split())   # splits string without whitespace
        for i in range(len(str_list)):
            for j in range(len(str_list[i])-1):
                try:
                    str_list[i][j+1] = int(str_list[i][j+1])    # try to give int value
                except ValueError:
                    try:
                        str_list[i][j+1] = round(float(str_list[i][j+1])) # try to give float value
                    except ValueError:
                        str_list[i][j+1] = 0    # else will give value of 0
    inf.close()

    outf = open('scoresAve.txt', 'w')
    for i in str_list:
        ave = 0
        file_write = i[0] + '\t'
        outf.write(file_write)
        for j in range(len(i)-1):
            outf.write(str(i[j+1]) + ' ')
            ave += i[j+1]
        outf.write(str(round(ave/3, 2)))
        outf.write('\n')
    outf.close()


def main():
    task_1()
    task_2_and_3()


if __name__ == '__main__':
    main()

"""
Adam	10  8  9
Ben	7  10   8
Cathy	9  9   7
David	6 5  8
Eve	8   9  6
Greg	8.5 8 2
Hami	8  a.5 10
Jami	1# 10 10
Terri	10  9 8
"""