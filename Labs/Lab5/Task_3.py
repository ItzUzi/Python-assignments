import random


def task_1():
    '''
    Asks for input from user and selects the largest of the
    3 strings inputted from the user
    :return: list of 3 strings inputted by user
    '''
    str1 = input('Enter string 1: ')
    str2 = input('Enter string 2: ')
    str3 = input('Enter string 3: ')

    # Gets largest character in string using max()
    lrg_char1 = max(str1)
    lrg_char2 = max(str2)
    lrg_char3 = max(str3)

    # Gets largest string using max()
    lrg_str = max(str1, str2, str3)

    print('Largest char in string 1 is: {}'.format(lrg_char1))
    print('Largest char in string 2 is: {}'.format(lrg_char2))
    print('Largest char in string 3 is: {}'.format(lrg_char3))
    print('The largest string is: {}'.format(lrg_str))

    # concatenates all 3 strings
    conc_string = str1 + '#' + str2 + '#' + str3

    print('Concatenated string is: {}'.format(conc_string))

    return str1, str2, str3


def task_2():
    '''
    Asks user to add float values onto a list
    Does special operations on list based on amount
    of elements list has
    :return: list of both user generated list and randomly generated list
    '''

    # Takes user input and creates a list of floats
    list1 = []
    while True:
        usr_input = float(input("Enter 0 to quit or enter a float: "))
        if usr_input == 0:
            break
        else:
            list1.append(usr_input)

    # Randomly generated int between 1-10 inclusive
    # is the length of the randomly generated float list
    num = random.randint(1, 10)
    list2 = []
    for i in range(num):
        list2.append(round(random.uniform(0, 100), 1))

    complete_list = [list1, list2]
    print("List1: {}".format(list1))
    print("List2: {}".format(list2))
    print("Appended list:", end=" ")

    # Checks which list is longer
    # if list 1 longer, add all elements from list2 to end of list1
    if len(list1) > len(list2):
        for num in list2:
            list1.append(num)
        print(list1)
    else:
        # else, insert all elements from list1 into odd indexes in list2
        index = 1
        for i in list1:
            list2.insert(index, i)
            index += 2
        print(list2)
    return complete_list


def task_3():
    # Creates tuples of strings returned from task1
    str_list = task_1()
    tup_str1 = tuple(str_list[0])
    tup_str2 = tuple(str_list[1])
    tup_str3 = tuple(str_list[2])

    print(tup_str1)
    print(tup_str2)
    print(tup_str3)

    # makes list of vowels in order to check amount of vowels per tuple
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vwl_count1 = 0
    vwl_count2 = 0
    vwl_count3 = 0

    # counts all instances of vowels within tuples
    for char in tup_str1:
        if char in vowels:
            vwl_count1 += 1
    for char in tup_str2:
        if char in vowels:
            vwl_count2 += 1
    for char in tup_str3:
        if char in vowels:
            vwl_count3 += 1

    total_vwl = vwl_count1 + vwl_count2 + vwl_count3
    print('Total vowels in strings is: %d' % total_vwl)

    both_lists = task_2()
    list1 = both_lists[0]
    list2 = both_lists[1]

    # combines list by adding every value
    if len(list1) < len(list2):
        for i in range(len(list1)):
            list2[i] += list1[i]
        tupled_list = tuple(list2)
    else:
        for i in range(len(list2)):
            list1[i] += list2[i]
        tupled_list = tuple(list1)

    print("tupled_list: {}".format(tupled_list))


def main():
    task_3()


if __name__ == '__main__':
    main()

'''
Output:

Enter string 1: Hello
Enter string 2: WOrd
Enter string 3: WOrld
Largest char in string 1 is: o
Largest char in string 2 is: r
Largest char in string 3 is: r
The largest string is: WOrld
Concatenated string is: Hello#WOrd#WOrld
('H', 'e', 'l', 'l', 'o')
('W', 'O', 'r', 'd')
('W', 'O', 'r', 'l', 'd')
Total vowels in strings is: 4
Enter 0 to quit or enter a float: 1.1
Enter 0 to quit or enter a float: 0
List1: [1.1]
List2: [96.8, 65.3, 0.7]
Appended list: [96.8, 1.1, 65.3, 0.7]
tupled_list: (97.89999999999999, 1.1, 65.3, 0.7)

Enter string 1: Dog
Enter string 2: Cat
Enter string 3: Bird
Largest char in string 1 is: o
Largest char in string 2 is: t
Largest char in string 3 is: r
The largest string is: Dog
Concatenated string is: Dog#Cat#Bird
('D', 'o', 'g')
('C', 'a', 't')
('B', 'i', 'r', 'd')
Total vowels in strings is: 3
Enter 0 to quit or enter a float: 1.2
Enter 0 to quit or enter a float: 5.7
Enter 0 to quit or enter a float: 1.3
Enter 0 to quit or enter a float: 8.6
Enter 0 to quit or enter a float: 3.5
Enter 0 to quit or enter a float: 9.5
Enter 0 to quit or enter a float: 1.2
Enter 0 to quit or enter a float: 6.5
Enter 0 to quit or enter a float: 4.3
Enter 0 to quit or enter a float: 7.4
Enter 0 to quit or enter a float: 23.4
Enter 0 to quit or enter a float: 0
List1: [1.2, 5.7, 1.3, 8.6, 3.5, 9.5, 1.2, 6.5, 4.3, 7.4, 23.4]
List2: [14.2, 22.1, 65.9, 79.1, 40.6]
Appended list: [1.2, 5.7, 1.3, 8.6, 3.5, 9.5, 1.2, 6.5, 4.3, 7.4, 23.4, 14.2, 22.1, 65.9, 79.1, 40.6]
tupled_list: (15.399999999999999, 27.8, 67.2, 87.69999999999999, 44.1, 9.5, 1.2, 6.5, 4.3, 7.4, 23.4, 14.2, 22.1, 65.9, 79.1, 40.6)
'''