def fart():
    print("excuse me")
    print("i farted")


def repeat(msg, n):
    for i in range(n):
        print(msg)


def two_three_check(n):
    return n % 2 == n % 3 == 0


for i in range(50, 112):
    if two_three_check(i):
        print(i)
