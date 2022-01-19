age = eval(input("How old are you? "))
legalAge = 18

if age >= legalAge:
    print("Up can vote!")
elif legalAge - age < 3:
    print("Sorry, but you can vote in the next election.")
else:
    print("You can't vote yet.")


n = eval(input("Enter a number: "))

if n % 2 == 0 and n % 3 == 0:
    print(f"{n} is even and divisible by 3")
else:
    print(f"{n} is odd")


