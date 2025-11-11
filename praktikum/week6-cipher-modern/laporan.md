# Laporan Praktikum Kriptografi
Minggu ke-: 6  
Topik: [Cipher Modern (DES, AES, RSA)]  
Nama: [Ayunita Thalia Nugraheni]  
NIM: [230202739]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Mengimplementasikan algoritma DES untuk blok data sederhana.
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.
---

## 2. Dasar Teori
Kriptografi modern berakar pada tiga pilar utama: DES (Data Encryption Standard) adalah block cipher simetris berbasis struktur Feistel yang bekerja pada blok 64-bit dengan kunci 56-bit, namun kini dianggap usang karena kuncinya terlalu pendek. Penggantinya adalah AES (Advanced Encryption Standard), yang juga simetris tetapi menggunakan desain Substitution-Permutation Network (SPN), bekerja pada blok 128-bit dengan panjang kunci 128, 192, atau 256 bit, menawarkan keamanan dan efisiensi yang jauh lebih unggul. Sementara itu, RSA adalah cipher asimetris (kunci publik) yang digunakan untuk pertukaran kunci dan tanda tangan digital; keamanannya bergantung pada kesulitan faktorisasi bilangan prima yang sangat besar ($N = p \cdot q$), di mana satu kunci digunakan untuk enkripsi (publik) dan kunci pasangannya untuk dekripsi (privat).

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
1.Persiapan Lingkungan: Membuat folder struktur yang diminta (praktikum/week6-cipher-modern/src/, screenshots/, dan laporan.md).
2.Instalasi Pustaka: Menjalankan perintah pip install pycryptodome.
3.Implementasi DES (Simulasi): Membuat file src/des.py untuk mensimulasikan enkripsi dan dekripsi DES mode ECB menggunakan kunci 64-bit.
4.Implementasi AES-128 (Wajib): Membuat file src/aes.py untuk mengimplementasikan AES dengan kunci 128-bit menggunakan mode EAX (yang menyertakan autentikasi).
5.Implementasi RSA (Wajib): Membuat file src/rsa.py untuk mengimplementasikan pembangkitan kunci RSA 2048-bit, diikuti dengan enkripsi menggunakan kunci publik dan dekripsi menggunakan kunci privat.
6.Pengujian Program: Menjalankan masing-masing program (misalnya, python src/aes.py dan python src/rsa.py) dan memverifikasi bahwa decrypted text sesuai dengan plaintext.
7.Mengambil screenshot hasil eksekusi dan menyusun laporan ini.
---

## 5. Source Code


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
- Pertanyaan 1: Apa perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan?
Jawab : Perbedaan mendasar antara ketiga cipher tersebut terletak pada jenis kunci dan mekanisme keamanannya. DES dan AES adalah cipher simetris (symmetric), yang berarti mereka menggunakan kunci yang sama (kunci rahasia) baik untuk enkripsi maupun dekripsi; perbedaannya, DES (kunci 56-bit) rentan dan usang, sedangkan AES (kunci 128/192/256-bit) sangat kuat dan efisien. Sebaliknya, RSA adalah cipher asimetris (asymmetric atau kunci publik), yang menggunakan pasangan dua kunci yang berbeda—satu untuk enkripsi (kunci publik) dan satu untuk dekripsi (kunci privat)—di mana keamanannya didasarkan pada kesulitan matematis dalam faktorisasi bilangan prima yang sangat besar. 
- Pertanyaan 2: Mengapa AES lebih banyak digunakan dibanding DES di era modern?
Jawab : AES jauh lebih banyak digunakan daripada DES di era modern terutama karena keamanan dan efisiensi superior yang ditawarkannya. Secara keamanan, DES hanya menggunakan panjang kunci 56-bit, yang membuatnya rentan terhadap serangan brute force dengan mudah menggunakan komputasi modern. Sebaliknya, AES mendukung kunci yang jauh lebih panjang (128, 192, atau 256-bit), menjadikannya tahan terhadap serangan tersebut. Selain itu, AES dirancang menggunakan struktur Substitution-Permutation Network yang lebih modern dan cepat, sehingga tidak hanya lebih aman tetapi juga lebih efisien dalam hal kecepatan dan implementasi, baik pada hardware maupun software, menjadikannya standar enkripsi global saat ini.
- Pertanyaan 3: Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya?
Jawab : RSA dikategorikan sebagai algoritma asimetris karena ia menggunakan pasangan dua kunci yang berbeda dan saling terkait secara matematis: Kunci Publik untuk enkripsi dan Kunci Privat untuk dekripsi atau penandatanganan, menghilangkan kebutuhan untuk berbagi kunci rahasia. Proses pembangkitan kuncinya diawali dengan memilih dua bilangan prima besar (p dan q), yang kemudian dikalikan untuk mendapatkan modulus (N=p⋅q). Selanjutnya, digunakan fungsi Euler's totient (ϕ(N)) untuk mencari eksponen publik (e) yang koprima, dan eksponen privat (d) yang merupakan invers perkalian dari e(modϕ(N)). Akhirnya, kunci publik terdiri dari pasangan (N,e) yang dibagikan, sementara kunci privat terdiri dari (N,d) yang harus dijaga kerahasiaannya.
)
---

## 8. Kesimpulan
Kriptografi modern kini didominasi oleh dua kategori: cipher simetris dan cipher asimetris. Dalam kategori simetris, meskipun DES sudah ditinggalkan karena kunci 56-bit-nya rentan, AES telah menjadi standar global karena kuncinya yang lebih panjang (hingga 256-bit) dan desain yang efisien, menjadikannya ideal untuk enkripsi data massal yang cepat dan aman. Sementara itu, RSA mewakili kategori asimetris, menggunakan pasangan kunci publik dan privat di mana keamanannya didasarkan pada kesulitan faktorisasi bilangan prima, dan fungsinya vital untuk pertukaran kunci rahasia secara aman serta untuk otentikasi melalui tanda tangan digital.
---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
 
```
commit abc12345
Author: Ayunita Thalia Nugraheni <nitaayu857@gmail.com>
Date:   2025-11-11

    week6-cryptosystem: implementasi Caesar Cipher dan laporan 
```
