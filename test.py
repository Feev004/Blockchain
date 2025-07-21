num = int(input("Enter a number: "))
p = 0
while num > 0:
    p = num % 2
    print("prime number" if p == 1 else "not prime number")
    num = int(input("Enter a number(Exit = 0): "))