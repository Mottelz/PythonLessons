# print("Loop 1")
# for i in range(10):
#     print(i)
#
# print("Loop 1.5")
# for i in range(-10):
#     print(i)
#
# print("Loop 2")
# for i in range(1, 10):
#     print(i)
#
# print("Loop 2.5")
# for i in range(10, 1):
#     print(i)
#
# print("Loop 3")
# for i in range(1, 10, 2):
#     print(i)
#
# print("Loop 3.5")
# for i in range(10, 1, -1):
#     print(i)
#
#

# students = ["Alfred", "Bart", "Carl", "Doris"]
# for s in students:
#     print(s)
#

# age = 15
# r = 0
# while age + r < 18:
#     print("keep waiting")
#     r += 1
# print(f"You need to wait {r} more years to vote.")

import random
history = []
while True:
    n = random.randint(1, 1000)
    print(history)
    if n in history:
        exit()
    else:
        history.append(n)
