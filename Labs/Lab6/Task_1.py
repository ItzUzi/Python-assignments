def updateDict(d, x):
    d[x] = "new value"

# 1) no because a key has to be immutable and a list is not immutable


def main():

    # 2)
    print("\nPart 2")
    favouriteFoods = {"Peg": "burgers", "Cy": "hotdogs", "Bob": "apple pie"}
    fav_food_list = list()
    for item in favouriteFoods.items():
        fav_food_list.append(item)
    print(fav_food_list)

    # 3)
    print("\nPart 3")
    fruit = {1: 'apples', 2: 'bananas', 3: 'pears', 4: 'grapes'}
    print("for item in fruit:")
    for item in fruit:
        print(item)  # prints all the keys
    print("for item in fruit.items()")
    for item in fruit.items():
        print(item)  # prints all keys and corresponding values as tuples
    print("for item in fruit.keys()")
    for item in fruit.keys():  # prints all the keys
        print(item)
    print("for item in fruit.values()")
    for item in fruit.values():  # prints all the values
        print(item)

    # 4) The db does change after the update
    print("\nPart 4")
    db = {'ted': 'xxx', 'jan': 123, 'kay': '13yy'}
    updateDict(db, 'jan')
    print(db)


if __name__ == '__main__':
    main()

'''
Output:

Part 2
[('Peg', 'burgers'), ('Cy', 'hotdogs'), ('Bob', 'apple pie')]

Part 3
for item in fruit:
1
2
3
4
for item in fruit.items()
(1, 'apples')
(2, 'bananas')
(3, 'pears')
(4, 'grapes')
for item in fruit.keys()
1
2
3
4
for item in fruit.values()
apples
bananas
pears
grapes

Part 4
{'ted': 'xxx', 'jan': 'new value', 'kay': '13yy'}
'''
