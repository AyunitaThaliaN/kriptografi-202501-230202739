# Laporan Praktikum Kriptografi
Minggu ke-: 1  
Topik: Sejarah Kriptografi & Prinsip CIA 
Nama: Ayunita Thalia Nugraheni 
NIM: 230202739 
Kelas: 5IKRB 

---

## 1. Tujuan
1.Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern,
2.Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar,
3.Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern,
4.Menyiapkan repositori GitHub sebagai media kerja praktikum,

---

## 2. Dasar Teori
Cipher klasik adalah metode kriptografi sebelum era komputer yang bekerja pada huruf atau kelompok huruf melalui substitusi (penggantian huruf) atau transposisi (perubahan posisi huruf). Contohnya Caesar Cipher, yang menggeser setiap huruf sejauh posisi tertentu. Karena kesederhanaannya dan bergantung pada kerahasiaan algoritma, cipher klasik kini dianggap tidak aman dan mudah dipecahkan.

Dasar matematis cipher klasik adalah aritmetika modular atau “aritmetika jam”, yang menjaga hasil enkripsi tetap dalam rentang alfabet (misalnya 26 huruf Latin). Misalnya, huruf ‘Y’ digeser 3 posisi menghasilkan (24+3) mod 26 = 1, yaitu huruf ‘B’.

---

## 3. Alat dan Bahan
- Laptop/Komputer 
- Visual Studio Code
- Akun Github yang aktif 

---

## 4. Langkah Percobaan
- Melakukan fork. 
- Mengubah nama repositori hasil fork.
- Melakukan clone repositori yang sudah diubah namanya ke komputer lokal.
- Membuat struktur folder baru di dalam repositori lokal.
- Di dalam folder tersebut, dibuat file `laporan.md` dan sebuah folder `screenshots/`.
- Menulis ringkasan mengenai sejarah kriptografi dan prinsip CIA di dalam file `laporan.md`.
- Menjawab pertanyaan quiz yang diberikan di dalam file `laporan.md`.
- Mengambil screenshot sebagai bukti penyiapan repositori dan menyimpannya di folder `screenshots/`.
- Menambahkan (add), melakukan commit (commit), dan mengirim (push) perubahan ke repositori GitHub dengan pesan commit `week1-intro-cia`.
---

## 5. Source Code
Praktikum minggu ini tidak ada agenda coding. Fokus kita sepenuhnya adalah pada penyiapan lingkungan kerja dan penyusunan laporan praktikum. Pastikan semua perangkat lunak yang dibutuhkan sudah siap digunakan.
---

## 6. Hasil dan Pembahasan
Praktikum kali ini berjalan lancar. Repositori GitHub sebagai lingkungan kerja telah berhasil disiapkan—mulai dari proses fork, clone, hingga penyesuaian struktur. Di samping itu, laporan awal yang merangkum materi dan jawaban kuis juga telah selesai disusun sesuai dengan panduan yang diberikan.

Bukti Schreenshoot dari penyiapan repositori: 
![repo setup](/praktikum/week1-intro-cia/Screenshot/repo_setup.png)
![initial commit](/praktikum/week1-intro-cia/Screenshot/initial_commit.png)

---

## 7. Jawaban Pertanyaan
1. Siapakah tokoh yang dianggap sebagai bapak kriptografi modern?
Claude Shannon, ilmuwan yang meletakkan dasar teori informasi dan kriptografi modern melalui karya monumentalnya berjudul “Communication Theory of Secrecy Systems” (1949). Dalam karyanya, Shannon menjelaskan prinsip-prinsip matematis yang menjadi fondasi kriptografi modern.

2. Sebutkan algoritma kunci publik yang populer digunakan saat ini? 
RSA (Rivest–Shamir–Adleman),ECC (Elliptic Curve Cryptography),Diffie–Hellman,DSA (Digital Signature Algorithm,ElGamal

3. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
Perbedaan utamanya terletak pada basis operasi dan prinsip keamanan.
kriptografi klasik bergantung pada (kerahasiaan algoritma dan manipulasi huruf), sedangkan
kriptografi modern bergantung pada keamanan matematis dan penggunaan kunci digital.

---

## 8. Kesimpulan
Praktikum ini memberikan pemahaman yang kuat tentang perkembangan kriptografi dari masa klasik hingga era modern, sekaligus mengenalkan konsep dasar keamanan informasi seperti CIA Triad (Confidentiality, Integrity, Availability). Selain itu, penggunaan Git dan GitHub sebagai lingkungan kerja juga telah berhasil dikonfigurasi dengan baik untuk mendukung dan mempermudah pelaksanaan praktikum berikutnya.
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
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
