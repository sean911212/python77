a = int(input())
k = 0
if a % 2 == 1:
    for i in range(1, a + 1, 2):
        print(" " * ((a - 1) // 2 - k), end="")
        print("*" * i)
        k += 1
    k = 1
    for i in range(a - 2, 0, -2):
        print(" " * k, end="")
        print("*" * i)
        k += 1
else:
    for i in range(1, a + 1, 1):
        print(" " * (a - 1 - k), end="")
        for j in range(i):
            print("* ",end="")
        print()
        k += 1
    k = 1
    for i in range(a - 1, 0, -1):
        print(" " * k, end="")
        for j in range(i):
            print("* ",end="")
        print()
        k += 1