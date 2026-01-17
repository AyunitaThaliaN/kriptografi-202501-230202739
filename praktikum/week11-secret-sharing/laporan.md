# Laporan Praktikum Kriptografi
Minggu ke-: 11
Topik: [Secret Sharing (Shamir's Secret Sharing)]  
Nama: [Ayunita Thalia Nugraheni]  
NIM: [230202739]  
Kelas: [5IKRB]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
1. Menjelaskan konsep Shamir Secret Sharing (SSS).
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3. Menganalisis keamanan skema distribusi rahasia.


---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

Dasar teori Secret Sharing (Shamir’s Secret Sharing) adalah metode kriptografi yang digunakan untuk membagi sebuah rahasia menjadi beberapa bagian (shares) sehingga rahasia tersebut hanya dapat direkonstruksi jika sejumlah minimal bagian tertentu digabungkan. Pada skema Shamir’s Secret Sharing, rahasia direpresentasikan sebagai konstanta dalam sebuah persamaan polinomial, kemudian dibagi menjadi n share, dengan syarat minimal k share (threshold) diperlukan untuk memperoleh kembali rahasia tersebut. Skema ini bersifat aman secara matematis, karena kurang dari k share tidak memberikan informasi apa pun tentang rahasia, sehingga banyak digunakan untuk pengamanan kunci kriptografi, sistem backup data sensitif, dan manajemen kunci terdistribusi.

Shamir’s Secret Sharing memungkinkan peningkatan keamanan dengan cara mendistribusikan kepercayaan kepada beberapa pihak, sehingga tidak ada satu pihak pun yang memegang seluruh rahasia. Dengan pendekatan threshold, sistem tetap aman meskipun sebagian share hilang atau jatuh ke pihak tidak berwenang, selama jumlah minimal share tidak terpenuhi. Konsep ini sangat efektif untuk mencegah single point of failure dan banyak diterapkan dalam pengelolaan kunci enkripsi, sistem keuangan, serta infrastruktur keamanan modern.
---

## 3. Alat dan Bahan
(- Python 3.10 
- Visual Studio Code /sebagai ide
- Git dan akun GitHub )  

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:

- Membuat struktur folder praktikum/week11-secret-sharing/src/.
- Menginstal library yang dibutuhkan menggunakan perintah pip install secretsharing.
- Membuat file secret_sharing.py dan mengimplementasikan fungsi untuk membagi rahasia menjadi 5 bagian dengan threshold 3.
- Menjalankan skrip untuk memverifikasi bahwa rahasia dapat pulih dengan 3 shares, namun gagal jika kurang dari itu.
- Mendokumentasikan hasil eksekusi dalam bentuk screenshot. )


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

![Hasil Eksekusi](screenshots/hasil pembagian dan rekonstruksi.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Apa keuntungan utama Shamir Secret Sharing dibanding membagikan salinan kunci secara langsung?

Jawab :
Keuntungan utama Shamir’s Secret Sharing dibandingkan membagikan salinan kunci secara langsung adalah keamanan dan kontrol akses yang lebih tinggi, karena rahasia tidak pernah disimpan atau diberikan dalam bentuk utuh kepada satu pihak. Dengan mekanisme threshold, rahasia hanya dapat dipulihkan jika jumlah minimal share terpenuhi, sehingga meskipun satu atau beberapa share bocor, rahasia tetap aman dan tidak dapat direkonstruksi. Selain itu, metode ini mengurangi risiko single point of failure dan memungkinkan distribusi kepercayaan ke banyak pihak tanpa mengorbankan kerahasiaan kunci.

- Pertanyaan 2: Apa peran threshold (k) dalam keamanan secret sharing?

Jawab :
Threshold (k) berperan sebagai batas minimum jumlah share yang harus digabungkan untuk dapat merekonstruksi rahasia dalam skema secret sharing. Nilai k menentukan tingkat keamanan sistem, karena kurang dari k share tidak memberikan informasi apa pun tentang rahasia, sehingga mencegah pihak tidak berwenang memperoleh kunci meskipun sebagian share bocor. Dengan demikian, threshold memungkinkan pengaturan keseimbangan antara keamanan dan ketersediaan, di mana rahasia tetap aman tetapi masih dapat dipulihkan meskipun beberapa share hilang.

- Pertanyaan 3: Berikan satu contoh skenario nyata di mana SSS sangat bermanfaat?

Jawab : 
Salah satu skenario nyata penggunaan Shamir’s Secret Sharing (SSS) adalah pada pengelolaan kunci enkripsi server perbankan. Kunci utama sistem dibagi menjadi beberapa share dan didistribusikan kepada beberapa pejabat berbeda, misalnya manajer IT, auditor, dan kepala keamanan. Sistem hanya dapat diakses kembali jika jumlah minimal share (threshold) digabungkan, sehingga meskipun satu orang tidak tersedia atau salah satu share bocor, kunci tetap aman dan tidak dapat disalahgunakan. Pendekatan ini mencegah penyalahgunaan wewenang serta meningkatkan keamanan dan keandalan sistem.
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

Shamir’s Secret Sharing merupakan metode kriptografi yang aman untuk melindungi rahasia dengan cara membaginya menjadi beberapa bagian, di mana hanya sejumlah minimal bagian tertentu (threshold) yang dapat digunakan untuk merekonstruksi rahasia tersebut. Pendekatan ini meningkatkan keamanan dengan menghindari penyimpanan rahasia secara utuh pada satu pihak, mengurangi risiko kebocoran dan single point of failure, serta banyak diterapkan dalam pengelolaan kunci dan sistem keamanan terdistribusi.
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
Author: Ayunita Thalia Nuhraheni <nitaayu857@gmail.com>
Date:   2025-01-16

    week11-secret-sharing )
```
