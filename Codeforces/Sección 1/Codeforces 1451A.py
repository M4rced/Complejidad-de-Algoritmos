t = int(input())
for i in range(0, t):
    numero = int(input())
    if numero == 1:
        print(0)
    elif numero == 2:
        print(1)
    elif numero == 3:
        print(2)
    elif numero == 9:
        print(3)
    else:
        if numero % 2 == 0:
            print(2)
        else:
            print(3)

