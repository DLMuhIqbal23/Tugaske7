print("==== Latihan 1 ====")
a = int(input("Masukkan a:"))
b = int(input("Masukkan b:"))
c = int(input("Masukkan c:"))
maks = 0

if a > b:
    maks = a
else:
    maks = b

if c > maks:
    maks = c
print("Bilangan yang terbesar adalah: ", maks)
