# num = int(input("Enter a number: "))
# p = 0
# while num > 0:
#     p = num % 2
#     num = num // 2
#     for i in range(2, num):
#         if num % i == 0:
#             # p = 1
#             break
#     print("P :", p, end=' ')
#     print("num : ", num, end=' ')
#     # print("prime number" if p == 1 else "not prime number")
#     num = int(input("Enter a number(Exit = 0): "))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
while num > 0:
    p = num % 2
    num = num // 2
    print("Prime :", p, end=' ')
    print("Num :", num, end=' ')
    print()
    print("->", "Prime number" if is_prime(num) else "Not prime number")
    num = int(input("Enter a number (0 to exit): "))
