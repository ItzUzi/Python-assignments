import random


def main():
    list1 = []

    while True:
        usr_input = float(input("Enter 0 to quit or enter a float: "))
        if usr_input == 0:
            break
        else:
            list1.append(usr_input)

    num = random.randint(1, 10)
    list2 = []
    for i in range(num):
        list2.append(round(random.uniform(0, 100), 2))

    if len(list1) > len(list2):
        for obj in list2:
            list1.append(obj)
        for obj in list1:
            print(obj, end=", ")
    else:
        index = 1
        for i in list1:
            list2.insert(index, i)
            index += 2
        for obj in list2:
            print(obj, end=", ")


if __name__ == '__main__':
    main()
