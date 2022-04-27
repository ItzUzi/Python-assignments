def prob1():
    for i in range(4):
        print(i, end = ' ')
print()
'''
0 1 2 3 None
'''

def fun(x = 1, y = 2):
    x = x =y
    y += 1
    return x * y

fun(3, 2)
fun(x=3, y=2)
fun(y=2, x=3)