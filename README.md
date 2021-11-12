# Tugaske7
## Latihan 1 (Lab 1)
### Menentukan bilangan terbesar dari dua bilangan
Pertama input a dan b sebagai integer, kenapa integer? karena nanti a dan b menjadi bilangan satuan bukan bilangan koma, jika bilangan koma maka menggunakan float. Lalu masukan maks = 0, maks sebagai nilai tertinggi.<p>
Lalu masukkan "if" dan "else" statement menjadi if a lebih besar (">") dari b dengan maks = a, lalu masukkan lagi else maks = b, kenapa pakai else? karena kalau ternyata b lebih besar dari a maka program akan otomatis menggunakan kode else.<p>
Terakhir masukkan output [print("terbesar: ", maks)] kenapa ada maks dibelakang output? agar nanti outputnya menampilkan bilangan terbesar dari kedua bilangan tersebut.<p>
![Gambar 1](ss/ss1.png)

## Latihan 2 (Lab 1)
### Menentukan urutan bilangan dari yang terkecil hingga terbesar
Pertama adalah masukan data = [], lalu for i in range(6): (semua i didalam range akan dilooping atau diulang sebanyak 6 kali).<p>
Lalu setelah itu input x sebagai integer, selanjutnya ketik data.append (fungsi append adalah menambahkan nilai array pada urutan akhir, jadi fungsi data.append(x) adalah menambahkan nilai array x ke akhir pada data).<p>
Lalu ketik list.sort(data) agar dapat otomatis mengurutkan bilangan terkecil hingga terbesar yang ada didalam data. Terakhir masukan output urutan bilangan dari yang terkecil dengan mengetik print("Urutan bilangan dari yang terkecil: ",data) memasukan data kedalam output agar nanti output akan otomatis menampilkan hasil dari data.<p>
![Gambar 2](ss/ss1.png)

## Latihan 1 (Lab 2)
### Membuat perulangan bertingkat (Nested Loop)
Pertama adalah masukkan list_angka seperti gambar dibawah ini, lalu ketik (for angka in list angka:) agar "angka" ini menjadi "list_angka", lalu ketik lagi "for i in angka:) sama seperti dai agar "i" ini menjadi "angka".<p>
Lalu ketik print(i, end='') agar apa yang didalam i bisa mengganti karakter terakhir bawaan yang dicetak dilayar. Terakhir ketik print().<p>
![Gambar 3](ss/ss2.png)

## Latihan 2 (Lab 2)
### Menampilkan n bilangan acak yang lebih dari 0,5
Pertama ketik import random agar nanti n nilainya acak, lalu input n sebagai integer.<p>
Lalu ketik "for i in range(n:)" agar i mengulangi atau loop sebanyak n. Setelah itu ketik "while 1:" agar mengulangi atau melooping terus menerus sampai suatu kondisi ternyata tidak dipenuhi, lalu ketin "n = random.random" agar n suatu bilangan acak , selanjutnya ketik "if n < 0.5" agar n tidak lebih dari 0.5 setelah itu ketik "break" untuk menghentikan jalannya proses statement pada while, terakhir ketik "print(n)" untuk menampilkan hasil n.<p>
![Gambar 4](ss/ss2.png)<p>

# Labspy02 (Modul 2)
## Menentukan bilangan terbesar dari 3 buah bilangan
Pertama masukan atau inputkan a, b, dan c sebagai integer, lalu masukkan maks = 0.<p>
Lalu masukkan "if a > b:" maka "maks = a" selanjutnya ketik else: maks = b, kenapa pakai else? karena kalau ternyata b lebih besar dari a maka program akan otomatis menggunakan kode else. Lalu tambahkan "if c > maks" maka "maks = c" agar jika a dan b lebih kecil maka c lebih besar diantara a dan b. Terakhir ketik "print("Bilangan yang terbesar adalah: ", maks)" untuk menampilkan bilangan yang terbesar diantara ketiga bilangan tersebut.
![Gambar 5](ss/ss3.png)<p>
Dan ini Flowchartnya<p>
![Gambar 6](ss/ss4.png)<p>

# Labspy03 (Modul 3)
## Latihan 1
### Menampilkan n bilangan acak yang lebih dari 0,5
Pertama ketik import random agar nanti n nilainya acak, lalu input n sebagai integer.<p>
Lalu ketik "for i in range(n:)" agar i mengulangi atau loop sebanyak n. Setelah itu ketik "while 1:" agar mengulangi atau melooping terus menerus sampai suatu kondisi ternyata tidak dipenuhi, lalu ketin "n = random.random" agar n suatu bilangan acak , selanjutnya ketik "if n < 0.5" agar n tidak lebih dari 0.5 setelah itu ketik "break" untuk menghentikan jalannya proses statement pada while, terakhir ketik "print(n)" untuk menampilkan hasil n.<p>
![Gambar 7](ss/ss5.png)<p>

## Latihan 2
### Menentukan bilangan terbesar dari buah n data yang diinputkan
Pertama inputkan maks sebagai 0 "maks = 0" lalu ketik "for i in range(6)" agar i didalam range akan mengulangi atau loop sebanyak 6 kali, setelah itu inputkan x sebagai integer.<p>
lalu ketik "if x > maks:" dan "maks = x" yang berarto jika x lebih besar dari maks maka maks itu sama dengan x. Setekah itu ketik "print("Bilangan terbesar adalah: ", maks) agar menampilkan hasil dari maks atau bilangan terbesar.<p>
![Gambar 8](ss/ss6.png)<p>

## Program 1
### Menentukan laba perbulan dan laba total
Ada 2 cara yaitu:<p>
#### Pertama
Yang pertama adalah menginputkan m atau modal sebagai integer, lalu inputkan l1 = 0 l1 sebagai laba bulan pertama. Setelah itu ketik "for i in range(1):" agar i didalam range akan mengulang atau looping sebanyak 1 kali, lalu masukan "l1 = m*0" itu rumus menentukan laba perbulan dan 0 itu laba pada bulan pertama yang mengikuti soalnya. Terakhir ketik "print("Laba bukan ke- 1 sebesar: ", l1) agar menampilkan hasil dari laba bulan pertama atau l1. Lakukan sama seperti itu sampai laba total. Contohnya ada dibawah ini:<p>
![Gambar 9](ss/ss7.png)<p>
![Gambar 10](ss/ss8.png)<p>
#### Kedua
Yang pertama dilakukan adalah menginputkan m atau modal sebagai integer, lalu inputkan juga l1 sampai dengan lt sama dengan 0 (l1 sampai dengan lt itu untuk rumus laba perbulan dan laba total).<p>
Lalu ketik "for i range(1):" agar i didalam range mengulangi atau looping sebanyak 1 kali, setelah itu inputkan l1 = m*0 (m sebagai modal yang tadi kita inputkan dan 0 itu laba dibulan itu dan juga 0 itu bisa diganti sesuai apa yang disebutkan disoal) lakukan itu sampai dengan lt.<p>
Terakhir adalah ketik print("Laba bulan ke 1 sebesar: ", l1) lakukan itu sampai dengan lt seperti gambar dibawah ini.<p>
![Gambar 11](ss/ss9.png)<p>