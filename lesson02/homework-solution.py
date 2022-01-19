n = eval(input("Enter a number: "))
out = ""

if n % 5 == 0 and n % 3 == 0:
    out = "Fee"
elif n % 3 == 0:
    out = "Fi"
elif n % 5 == 0:
    out = "Fo"
else:
    out = "Fum"

print(out)
