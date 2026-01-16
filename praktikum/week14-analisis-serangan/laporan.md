# Laporan Praktikum Kriptografi
Minggu ke-: 14 
Topik: [Analisis Serangan Kriptografi]  
Nama: [Ayunita Thalia Nugraheni]  
NIM: [230202739]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori
Analisis serangan kriptografi merupakan kajian yang mempelajari berbagai teknik serangan yang dapat digunakan untuk melemahkan atau menembus sistem kriptografi, baik pada tingkat algoritma, protokol, maupun implementasinya. Tujuan utama dari analisis ini adalah untuk menilai sejauh mana suatu sistem kriptografi mampu melindungi kerahasiaan, integritas, dan keaslian data dari upaya penyerangan. Analisis dilakukan dengan asumsi bahwa penyerang mengetahui algoritma yang digunakan (prinsip Kerckhoffs), tetapi tidak mengetahui kunci rahasia.

Jenis serangan kriptografi sangat beragam, mulai dari serangan matematis dan statistik hingga serangan berbasis implementasi. Contohnya adalah brute force attack yang mencoba semua kemungkinan kunci, known-plaintext dan chosen-plaintext attack yang memanfaatkan pasangan teks asli dan teks sandi, serta ciphertext-only attack yang hanya mengandalkan teks sandi. Selain itu, terdapat side-channel attack yang mengeksploitasi informasi fisik seperti waktu komputasi, konsumsi daya, atau radiasi elektromagnetik untuk memperoleh kunci rahasia.

Melalui analisis serangan kriptografi, kelemahan sistem dapat diidentifikasi sejak dini sehingga dapat dilakukan perbaikan, seperti pemilihan algoritma yang lebih kuat, penggunaan panjang kunci yang memadai, serta penerapan teknik pengamanan tambahan. Dengan demikian, analisis serangan kriptografi menjadi bagian penting dalam perancangan dan evaluasi sistem keamanan informasi agar tetap andal terhadap ancaman yang terus berkembang.

---

## 3. Alat dan Bahan
(- Python 3.x 
- Python 3.11 
- Visual Studio Code 
- Git dan akun GitHub  
- Library tambahan (haslib dan time))

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

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
- Pertanyaan 1: 
Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?

Jawab :
Banyak sistem lama masih rentan terhadap brute force atau dictionary attack karena menggunakan algoritma kriptografi yang sudah usang, panjang kunci yang pendek, serta mekanisme penyimpanan kata sandi yang lemah, seperti hash tanpa salt. Selain itu, sistem lama sering tidak dilengkapi dengan pembatasan percobaan login, rate limiting, atau mekanisme deteksi serangan, sehingga penyerang dapat mencoba banyak kombinasi kata sandi tanpa hambatan. Kurangnya pembaruan keamanan dan ketergantungan pada desain lama membuat sistem tersebut lebih mudah dieksploitasi dibandingkan sistem modern.


- Pertanyaan 2: Apa bedanya kelemahan algoritma dengan kelemahan implementasi?

Jawab :
Perbedaan antara kelemahan algoritma dan kelemahan implementasi terletak pada sumber masalah keamanannya. Kelemahan algoritma berasal dari desain matematis atau konsep dasar algoritma kriptografi itu sendiri, sehingga meskipun diimplementasikan dengan benar, algoritma tersebut tetap dapat ditembus atau tidak lagi aman (misalnya algoritma lama yang sudah terbukti lemah). Sementara itu, kelemahan implementasi muncul akibat kesalahan dalam penerapan algoritma yang sebenarnya aman, seperti pengelolaan kunci yang buruk, penggunaan parameter yang salah, atau kebocoran informasi melalui side-channel, sehingga membuka celah keamanan meskipun algoritmanya kuat.

- Pertanyaan 3: 
Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?


Jawab :
Organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan dengan menerapkan algoritma dan protokol kriptografi yang telah terstandarisasi dan direkomendasikan oleh komunitas keamanan, serta secara rutin melakukan pembaruan dan evaluasi keamanan. Selain itu, organisasi perlu menerapkan praktik manajemen kunci yang baik, melakukan audit dan pengujian keamanan secara berkala, serta memantau perkembangan ancaman dan kemajuan teknologi seperti komputasi kuantum. Dengan pendekatan proaktif ini, sistem kriptografi dapat disesuaikan dan diperkuat secara berkelanjutan agar tetap andal menghadapi ancaman yang terus berkembang.
)
---

## 8. Kesimpulan
((Berdasarkan hasil analisis, dapat disimpulkan bahwa serangan kriptografi sering terjadi akibat penggunaan algoritma lemah dan implementasi yang tidak aman. Kasus serangan brute force pada hash MD5 menunjukkan pentingnya pemilihan algoritma kriptografi yang tepat dan penerapan mekanisme keamanan tambahan. Dengan mengganti algoritma lama dan memperbaiki konfigurasi sistem, tingkat keamanan informasi dapat ditingkatkan secara signifikan. )

)

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
Author: Ayunita Thalia Nugraheni<nitaayu857@gmail.com>
Date:   2025-01-16

    week14-analisis-serangan)
```
