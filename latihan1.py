import random
n = int(input("Masukkan nilai N: "))
for i in range(5):
    while 1:
        n = random.random()
        if n < 0.5:
            break
    print(n)