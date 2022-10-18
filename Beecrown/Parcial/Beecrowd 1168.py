panel = (6,2,5,5,4,5,6,3,7,6)
numero = int(input())

for i in range(numero):
    total = 0
    valor = input()
    for v in valor:
        total += panel[int(v)]
    print("%d leds" %int(total))