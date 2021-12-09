import random


def average(amount, left, right):
    total = 0
    temp = 0
    for i in range(amount):
        temp=random.randrange(left, right)
        print(temp)
        total += temp

    print("total =", total)
    return total/amount

avg=average(10, 1, 100)

print("Average =", avg)


