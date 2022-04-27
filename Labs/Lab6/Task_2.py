def main():
    # instantiates list L
    L = [1, 4, 9, 4, 7, 2, 2, 9]
    S = set(L)
    print("The length of set S is: {}".format(len(S)))

    # uses reversed() function to reverse L fo FS
    FS = frozenset(reversed(L))
    print("The number of elements in FS is: {}".format(len(FS)))

    # checks if all items in S are in FS
    for item in S:
        if item not in FS:
            print("Set S and set FS are not equal")
            break
        # checks if all items in FS are in S
        for obj in FS:
            if obj not in S:
                print("Set S and set FS are not equal")
    else:
        print("Set S and set FS are equal")

    S1 = {6, 7, 8}

    # Creates a Union set to find the union between S1 and S
    union_set = S.copy()
    # Creates an intersection set to find the intersection between S1 and S
    intersection_set = set()
    for item in S1:
        if item not in union_set:
            union_set.add(item)
        else:
            intersection_set.add(item)
    print("The union of S1 and S is: {}".format(union_set))
    print("The intersection of S1 and S is {}".format(intersection_set))

    # creates all difference variation sets
    S2 = {4, 5, 6, 7, 8, 9}
    difference_set_FS = set()
    difference_set_S2 = set()
    symmetric_difference = set()

    # finds difference of FS - S
    # finds symmetric difference between FS and S
    for item in FS:
        if item not in S2:
            difference_set_FS.add(item)
            symmetric_difference.add(item)
    # finds difference of S - FS
    # finds symmetric difference between FS and S
    for item in S2:
        if item not in FS:
            difference_set_S2.add(item)
            symmetric_difference.add(item)

    print("The difference of FS and S2 is: {}".format(difference_set_FS))
    print("The difference of S2 and FS is: {}".format(difference_set_S2))
    print("The symmetric difference of FS and S2 is: {}".format(symmetric_difference))


if __name__ == '__main__':
    main()

'''
Output:

The length of set S is: 5
The number of elements in FS is: 5
Set S and set FS are equal
The union of S1 and S is: {1, 2, 4, 6, 7, 8, 9}
The intersection of S1 and S is {7}
The difference of FS and S2 is: {1, 2}
The difference of S2 and FS is: {8, 5, 6}
The symmetric difference of FS and S2 is: {1, 2, 5, 6, 8}
'''
