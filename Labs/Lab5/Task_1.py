def main():
    str1 = input('Enter string 1: ')
    str2 = input('Enter string 2: ')
    str3 = input('Enter string 3: ')

    lrg_char1 = max(str1)
    lrg_char2 = max(str2)
    lrg_char3 = max(str3)

    lrg_str = max(str1, str2, str3)

    print('Largest char in string 1 is: {}'.format(lrg_char1))
    print('Largest char in string 2 is: {}'.format(lrg_char2))
    print('Largest char in string 3 is: {}'.format(lrg_char3))
    print('The largest string is: {}'.format(lrg_str))

    conc_string = str1 + '#' + str2 + '#' + str3

    print('Concatenated string is: {}'.format(conc_string))


if __name__ == '__main__':
    main()
