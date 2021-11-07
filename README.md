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
![Gambar 4](ss/ss2.png)