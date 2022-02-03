import random


# 1
def q1():
    number = eval(input("Please enter a number: "))
    if number % 5 == 0:
        return None


# 2
def calculate_factorial(number):
    total = number
    for multiplier in range(1, number):
        total *= multiplier
    return total


# 3
def is_prime(toCheck):
    for divisor in range(2, toCheck):
        if toCheck % divisor == 0:
            return False
    return True


# 4
def is_larger_than_random(userGuess):
    return userGuess > random.randint(1, 1000)


# 5
userNumber = eval(input("Enter a number: "))
print(f"Factorial? {calculate_factorial(userNumber)}\nIs Prime? {is_prime(userNumber)}\nIs bigger? {is_larger_than_random(userNumber)}")
