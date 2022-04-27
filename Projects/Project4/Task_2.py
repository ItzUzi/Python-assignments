from pandas import Series, DataFrame
import pandas as pd


def main():
    fn = input("Enter file name: ")
    try:
        inf = open(fn, 'r')
    except FileNotFoundError:   # if file not found, will exit program
        print("File not found, file name was entered incorrectly.")
        exit()

    data = list()
    for line in inf:
        line = line.rstrip()    # takes out \n
        try:
            data.append(float(line))    # value is skipped if its not a float
        except ValueError:
            pass
    inf.close()

    for i in range(len(data)):
        data[i] *= 100
    # Creates dictionary for easy storing of variables
    data_dict = dict()
    data = Series(data)
    data_dict['max'] = round(data.max(), 3)
    data_dict['min'] = round(data.min(), 3)
    data_dict['mean'] = round(data.mean(), 3)
    data_dict['median'] = data.median()
    data_dict['mode'] = data.mode()[0]
    data_dict['std deviation'] = round(data.std(), 3)

    outf = open("ocean_temp_data.txt", 'w')
    for i in data_dict.keys():
        outf.write(i + ": " + str(data_dict[i]) + '\n')
    outf.close()



if __name__ == '__main__':
    main()
