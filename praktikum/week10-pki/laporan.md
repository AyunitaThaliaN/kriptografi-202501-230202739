# Laporan Praktikum Kriptografi
Minggu ke-: 10 
Topik: [Public Key Infrastructure (PKI&Certificare Authority)]  
Nama: [Ayunita Thalia Nugraheni]  
NIM: [230202739]  
Kelas: [5IKRB]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1. Membuat sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).
---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

Public Key Infrastructure (PKI)

- Public Key Infrastructure (PKI) adalah sistem keamanan berbasis kriptografi kunci publik yang digunakan untuk menjamin kerahasiaan, keaslian, integritas, dan non-repudiation dalam komunikasi digital. PKI memanfaatkan sepasang kunci kriptografi, yaitu public key (kunci publik) dan private key (kunci privat). Public key digunakan untuk enkripsi dan verifikasi tanda tangan digital, sedangkan private key digunakan untuk dekripsi dan pembuatan tanda tangan digital.

- Certificate Authority (CA)

Certificate Authority (CA) adalah lembaga terpercaya dalam PKI yang bertugas menerbitkan, memverifikasi, dan mengelola sertifikat digital. Sertifikat digital berfungsi sebagai identitas elektronik yang menghubungkan public key dengan pemiliknya, seperti individu, organisasi, atau server. Dengan adanya CA, pengguna dapat memastikan bahwa pihak yang berkomunikasi benar-benar valid dan dapat dipercaya.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- pip install cryptography pyopenssl


---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat folder struktur praktikum, termasuk praktikum/week10-pki/src/.
2. Menginstal library yang dibutuhkan: pip install cryptography pyopenssl.
3. Membuat file src/pki_cert.py dan menyalin kode program yang disediakan.
4. Menjalankan program dengan perintah python src/pki_cert.py.
5. Memastikan dua file output berhasil dibuat di direktori: private.key dan cert.pem.
6. Mengambil screenshot hasil eksekusi program.)
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

- Pertanyaan 1: Apa fungsi utama Certificate Authority (CA)?

Jawab :
- Memastikan bahwa public key benar-benar milik pihak yang sah

- Membangun kepercayaan (trust) dalam komunikasi digital

- Mencegah pemalsuan identitas dan serangan man-in-the-middle

- Mendukung keamanan komunikasi seperti HTTPS, email aman, dan tanda tangan digital

- Pertanyaan 2: Mengapa self-signed certificate tidak cukup untuk sistem produksi?

Jawab :
Self-signed certificate tidak cukup untuk sistem produksi karena sertifikat ini ditandatangani oleh pemiliknya sendiri tanpa verifikasi dari Certificate Authority (CA) yang terpercaya, sehingga tidak diakui oleh browser dan sistem operasi dan menimbulkan peringatan keamanan bagi pengguna. Selain itu, self-signed certificate tidak menjamin keaslian identitas server dan rentan terhadap serangan man-in-the-middle karena tidak ada pihak ketiga yang memvalidasi identitas tersebut. Kondisi ini dapat menurunkan kepercayaan pengguna dan tidak memenuhi standar keamanan yang umumnya diwajibkan pada sistem produksi, sehingga lebih cocok digunakan hanya pada lingkungan pengujian atau pengembangan.

- Pertanyaa 3: Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?

Jawab :
PKI mencegah serangan Man-in-the-Middle (MITM) dalam komunikasi TLS/HTTPS dengan memastikan keaslian identitas server melalui sertifikat digital yang diterbitkan oleh Certificate Authority (CA) terpercaya. Saat klien (misalnya browser) terhubung ke server, sertifikat server akan diverifikasi dengan public key CA yang sudah tersimpan di sistem klien. Jika sertifikat valid, klien yakin bahwa public key tersebut benar milik server tujuan, sehingga kunci sesi TLS dapat dibentuk secara aman dan dienkripsi. Proses ini mencegah penyerang menyamar sebagai server atau memodifikasi komunikasi karena mereka tidak memiliki private key yang sah dan tidak dapat memalsukan sertifikat yang dipercaya oleh klien.

)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

Public Key Infrastructure (PKI) dan Certificate Authority (CA) merupakan fondasi utama keamanan komunikasi digital yang berfungsi menjamin keaslian identitas, kerahasiaan, dan integritas data melalui penggunaan kriptografi kunci publik. CA bertindak sebagai pihak terpercaya yang menerbitkan dan memverifikasi sertifikat digital, sehingga mencegah penyamaran identitas dan serangan seperti man-in-the-middle. Dengan adanya PKI dan CA, komunikasi seperti TLS/HTTPS, email aman, dan transaksi online dapat berlangsung secara aman dan terpercaya.
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

    week10-pki
```
