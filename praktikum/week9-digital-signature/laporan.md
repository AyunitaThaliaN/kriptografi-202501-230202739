# Laporan Praktikum Kriptografi
Minggu ke-: 9 
Topik: [Digital Signature (RSA/DSA)]  
Nama: [Ayunita Thalia  Nugraheni]  
NIM: [230202739]  
Kelas: []  5IKRB

---

## 1. Tujuan
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2. Memverifikasi keaslian tanda tangan digital.
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.


---

## 2. Dasar Teori
Digital Signature merupakan teknik kriptografi yang berfungsi untuk menjamin keaslian, keutuhan, dan keabsahan suatu data atau pesan digital. Mekanisme ini bekerja dengan memanfaatkan kriptografi kunci publik, di mana pengirim menandatangani pesan menggunakan kunci privat dan penerima memverifikasinya menggunakan kunci publik. Pada algoritma RSA tanda tangan digital dibuat dengan mengenkripsi nilai hash pesan menggunakan kunci privat, sedangkan pada DSA, tanda tangan dihasilkan dalam bentuk pasangan nilai matematis yang diverifikasi dengan kunci publik. Kedua algoritma tersebut banyak digunakan dalam sistem keamanan digital seperti sertifikat digital, transaksi elektronik, dan komunikasi aman.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file digital_signature.py di folder praktikum/week9-digital_siganture/src/.
2. Menyalin kode program dari panduan praktikum.
3.Menjalankan program dengan perintah python digital_signature.py.)

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
- Pertanyaan 1: Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?
Perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA terletak pada tujuannya. Enkripsi RSA digunakan untuk menjaga kerahasiaan data dengan mengenkripsi pesan menggunakan kunci publik penerima sehingga hanya kunci privat penerima yang dapat membukanya, sedangkan tanda tangan digital RSA bertujuan untuk menjamin keaslian, keutuhan, dan non-repudiation pesan dengan cara menandatangani pesan menggunakan kunci privat pengirim dan diverifikasi menggunakan kunci publik pengirim.

- Pertanyaan 2: Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?
Tanda tangan digital menjamin integritas dan otentikasi pesan karena tanda tangan dibuat dari hash pesan yang dienkripsi menggunakan kunci privat pengirim. Jika isi pesan diubah, nilai hash akan berubah sehingga verifikasi tanda tangan gagal, yang menandakan integritas pesan tidak terjaga. Selain itu, karena hanya pengirim yang memiliki kunci privat tersebut, keberhasilan verifikasi menggunakan kunci publik membuktikan bahwa pesan benar-benar berasal dari pengirim yang sah, sehingga otentikasi dapat dipastikan.

- Pertanyaan 3 : Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?
Certificate Authority (CA) berperan sebagai pihak tepercaya yang memverifikasi identitas pemilik kunci publik dan menerbitkan sertifikat digital yang mengaitkan identitas tersebut dengan kunci publiknya. Dalam sistem tanda tangan digital modern, CA memastikan bahwa kunci publik yang digunakan untuk verifikasi benar-benar milik pihak yang sah, sehingga mencegah pemalsuan identitas dan serangan man-in-the-middle. Dengan adanya CA, proses verifikasi tanda tangan digital dapat dilakukan secara aman dan terpercaya.

 
)
---

## 8. Kesimpulan
Digital Signature berbasis algoritma RSA dan DSA berperan penting dalam menjamin keamanan komunikasi digital dengan memastikan keaslian pengirim, keutuhan pesan, dan non-repudiation. Pada RSA, tanda tangan digital dibuat dengan mengenkripsi nilai hash pesan menggunakan kunci privat pengirim, sedangkan pada DSA tanda tangan dihasilkan melalui perhitungan matematis yang menghasilkan pasangan nilai `(r, s)` yang diverifikasi menggunakan kunci publik. Mekanisme ini memastikan bahwa setiap perubahan sekecil apa pun pada pesan akan menyebabkan kegagalan verifikasi.

Perbedaan utama antara RSA dan DSA terletak pada fleksibilitas dan efisiensi penggunaannya. RSA dapat digunakan baik untuk enkripsi maupun tanda tangan digital sehingga lebih umum diterapkan pada berbagai sistem keamanan, sementara DSA dirancang khusus untuk proses penandatanganan yang lebih cepat dan efisien, namun sangat bergantung pada kualitas bilangan acak yang digunakan. Pemilihan algoritma biasanya disesuaikan dengan kebutuhan sistem dan tingkat keamanan yang diinginkan.

Dalam penerapan modern, keberadaan Certificate Authority (CA) sangat krusial karena berfungsi memverifikasi identitas pemilik kunci publik melalui sertifikat digital. Dengan dukungan CA, sistem tanda tangan digital RSA dan DSA dapat digunakan secara tepercaya dalam berbagai layanan penting seperti transaksi perbankan, e-commerce, tanda tangan dokumen elektronik, dan komunikasi aman berbasis internet.

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
Author: Ayunita Thaia Nugraheni <nitaayu857@gmail.com>
Date:   2025-12-30

    week9-cryptosystem:Digital Signature (RSA/DSA) 
```
