# Lab 2 
## Latihan 1
print("==== Latihan 1 ====")
a = int(input("Masukkan a:"))
b = int(input("Masukkan b:"))

maks = 0

print(a, b)
if a > b:
    maks = a
else:
    maks = b

print("terbesar: ", maks)

## Latihan 2
print("==== Latihan 2 ====")
data = []
for i in range(6):
    x = int(input("Masukkan Bilangan: "))
    data.append(x)
list.sort(data)
print("Urutan bilangan dari yang terkecil: ",data)

# Lab 3
## Latihan 1
print("==== Latihan 1 ====")
list_angka = ['0 1 2 3 4 5 6 7 8 9', '1 2 3 4 5 6 7 8 9 10', '2 3 4 5 6 7 8 9 10 11', 
'3 4 5 6 7 8 9 10 11 12', '4 5 6 7 8 9 10 11 12 13', '5 6 7 8 9 10 11 12 13 14', 
'6 7 8 9 10 11 12 13 14 15', '7 8 9 10 11 12 13 14 15 16', '8 9 10 11 12 13 14 15 16 17', 
'9 10 11 12 13 14 15 16 17 18']
for angka in list_angka:
    for i in angka:
        print(i, end='') 
    print()

## Latihan 2
print("==== Latihan 2 ====")
import random
n = int(input("Masukkan Jumlah n = "))
for i in range(n):
    while 1:
        n = random.random()
        if n < 0.5:
            break
    print(n)