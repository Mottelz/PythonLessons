# How to get a random number
import random
x = random.randint(1, 10)

# How to figure out if a number is prime
toCheck = 5
isPrime = True
for divisor in range(2, toCheck):
    if toCheck % divisor == 0:
        isPrime = False
        break
print(isPrime)
