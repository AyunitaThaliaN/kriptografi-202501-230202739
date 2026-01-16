# Laporan Praktikum Kriptografi
Minggu ke-: 13  
Topik: [TinyChain – Proof of Work (PoW)]  
Nama: [Ayunita Thalia Nugraheni]  
NIM: [230202739]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Menjelaskan peran hash function dalam blockchain.
2. Melakukan simulasi sederhana Proof of Work (PoW).
3. Menganalisis keamanan cryptocurrency berbasis kriptografi..)

---

## 2. Dasar Teori
Dasar teori TinyChain – Proof of Work (PoW) menjelaskan bahwa TinyChain merupakan contoh sederhana penerapan teknologi blockchain yang menggunakan mekanisme konsensus Proof of Work untuk memvalidasi transaksi dan menambahkan blok baru ke dalam rantai. Dalam PoW, setiap node (miner) harus menyelesaikan permasalahan kriptografi berupa pencarian nilai nonce yang menghasilkan hash sesuai tingkat kesulitan tertentu. Proses ini membutuhkan daya komputasi, sehingga mencegah manipulasi data karena perubahan pada satu blok akan mengharuskan perhitungan ulang seluruh blok berikutnya. Dengan mekanisme tersebut, TinyChain–PoW mampu menjamin integritas data, transparansi, dan keamanan sistem blockchain meskipun dijalankan dalam skala sederhana atau simulatif.


---

## 3. Alat dan Bahan
(- Python 3.11 
- Visual Studio Code 
- Git dan akun GitHub  
- Library tambahan (hashlib dan time) )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:

1.Membuat file src_tinychain.py di folder praktikum/week13-tinychain/src/.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah python caesar_cipher.py.)
---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Menjelaskan peran hash function dalam blockchain?

Jawab :
Hash function memiliki peran penting dalam blockchain sebagai mekanisme untuk menjaga integritas, keamanan, dan keterkaitan antarblok. Setiap blok dalam blockchain memiliki nilai hash yang dihasilkan dari data transaksi di dalamnya, sehingga perubahan sekecil apa pun pada data akan menghasilkan hash yang berbeda. Selain itu, hash dari blok sebelumnya disertakan dalam blok berikutnya, membentuk rantai yang saling terhubung dan membuat data sulit dimanipulasi. Dalam mekanisme seperti Proof of Work, hash function juga digunakan untuk memvalidasi blok melalui proses pencarian nonce, sehingga memastikan bahwa penambahan blok baru memerlukan usaha komputasi dan meningkatkan keamanan sistem blockchain.

- Pertanyaan 2:  
Melakukan simulasi sederhana Proof of Work (PoW).

Jawab :
Simulasi sederhana Proof of Work (PoW) dilakukan dengan cara menggabungkan data blok dengan sebuah nilai acak yang disebut nonce, kemudian memprosesnya menggunakan fungsi hash kriptografi seperti SHA-256 hingga menghasilkan hash yang memenuhi tingkat kesulitan tertentu, misalnya diawali dengan sejumlah nol. Proses ini dilakukan secara berulang dengan mencoba berbagai nilai nonce sampai ditemukan hash yang sesuai, sehingga menunjukkan bahwa penambahan blok baru memerlukan usaha komputasi. Mekanisme ini meniru cara kerja PoW dalam blockchain, di mana kesulitan komputasi berfungsi untuk menjaga keamanan, mencegah manipulasi data, dan memastikan integritas rantai blok.

- Pertanyaan 3: 
Menganalisis keamanan cryptocurrency berbasis kriptografi?

Jawab:
Keamanan cryptocurrency berbasis kriptografi bergantung pada penerapan algoritma kriptografi yang menjamin kerahasiaan, integritas, dan keaslian transaksi. Kriptografi kunci publik digunakan untuk mengamankan kepemilikan aset melalui pasangan public key dan private key, di mana private key berfungsi sebagai bukti kepemilikan yang tidak boleh diketahui pihak lain. Selain itu, fungsi hash kriptografi memastikan bahwa setiap transaksi dan blok tidak dapat diubah tanpa terdeteksi, karena perubahan kecil pada data akan menghasilkan hash yang berbeda secara signifikan. Di sisi lain, mekanisme konsensus seperti Proof of Work atau Proof of Stake memperkuat keamanan jaringan dengan mencegah pihak tertentu menguasai sistem secara sepihak. Namun, keamanan ini juga menghadapi tantangan, seperti risiko pencurian private key, serangan 51%, dan kelemahan implementasi perangkat lunak. Oleh karena itu, meskipun kriptografi menyediakan fondasi keamanan yang kuat bagi cryptocurrency, perlindungan menyeluruh tetap memerlukan praktik pengelolaan kunci yang baik, desain protokol yang matang, dan kesadaran pengguna terhadap risiko keamanan.


)
---

## 8. Kesimpulan
TinyChain dengan mekanisme Proof of Work (PoW) menunjukkan bagaimana teknologi blockchain menjaga keamanan dan integritas data melalui proses komputasi dalam pencarian nonce yang valid. Dengan memanfaatkan fungsi hash kriptografi dan tingkat kesulitan tertentu, PoW mencegah manipulasi data serta memastikan bahwa setiap blok yang ditambahkan telah melalui proses verifikasi yang sah. Meskipun bersifat sederhana, TinyChain–PoW mampu menggambarkan konsep dasar blockchain, transparansi, dan keamanan sistem terdistribusi.
---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Ayunita Thalia Nugraheni <nitaayu857@gmail.com>
Date:   2025-01-16

   week13-tinychain)
```
