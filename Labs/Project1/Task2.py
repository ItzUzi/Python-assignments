import random
import math

def monte_carlo(random_seed, numDarts):
    inCircle = 0
    quarter = numDarts >> 2
    half = numDarts >> 1
    print("n is:", numDarts)
    print("Random seed is:", random_seed)
    random.seed(random_seed)
    for num in range(numDarts):
        x = random.random()
        y = random.random()
        distance = math.sqrt(x**2+y**2)
        if distance <= 1:
            inCircle += 1
        if num == quarter:
            pi = inCircle / quarter * 4
            print("Quarter done:",pi)       # shows first quarter of calculation
        if num == half:
            pi = inCircle / half * 4
            print("Half done:", pi)         # shows first half of calculation
    pi = inCircle / numDarts * 4
    print("Final Result:", pi)

monte_carlo(1, 60329831)
print()
monte_carlo(48321, 5000000)
print()
monte_carlo(62542, 100000000)

'''
Output:
n is: 60329831
Random seed is: 1
Quarter done: 3.141262726623388
Half done: 3.1414725352284267
Final Result: 3.1416590575233005

n is: 5000000
Random seed is: 48321
Quarter done: 3.1422752
Half done: 3.1407024
Final Result: 3.1414088

n is: 100000000
Random seed is: 62542
Quarter done: 3.1418992
Half done: 3.14173088
Final Result: 3.14157124
'''


'''
def second_loop():
    counter = 0
    inCircle = 0
    while True:
        counter+=1
        x = random.random()
        y = random.random()
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            inCircle += 1
        pi = inCircle / counter * 4
        if abs(pi - math.pi) < .000001:
            print(pi)
            print("counter:", counter)
            break
        
second_loop()
'''
