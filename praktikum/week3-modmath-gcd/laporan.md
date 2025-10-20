# Laporan Praktikum Kriptografi
Minggu ke-: 3 
Topik: [Modular Matha (Aritmetika Modular, GCD,Bilangan Prima,Logaritma Diskrit)]  
Nama: [Ayunita Thalia Nugraheni]  
NIM: [230202739]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Logaritma diskrit adalah konsep matematika yang mencari berapa kali suatu bilangan harus dikalikan dengan dirinya sendiri untuk menghasilkan bilangan lain dalam sistem tertentu. Nilainya sulit dihitung, terutama pada bilangan besar, sehingga sering digunakan dalam kriptografi.

Kesulitannya membuat logaritma diskrit menjadi dasar keamanan sistem seperti Diffie-Hellman dan ElGamal, karena mudah dihitung satu arah tetapi hampir mustahil dibalik, sehingga efektif melindungi data dan kunci rahasia.
---

## 3. Alat dan Bahan
- Python   
- Visual Studio Code   
- Git dan akun GitHub  
---

## 4. Langkah Percobaan  
1. Membuat struktur folder praktikum/week3-modmath-gcd/src/ dan file modular_math.py.
2. Tambahkan fungsi-fungsi aritmetika modular seperti mod_add, mod_sub, mod_mul, dan mod_exp.
3. Mengimplementasikan algoritma Euclidean buat nyari nilai GCD.
4. Mengimplementasikan dengan Extended Euclidean Algorithm (egcd) dan bikin juga fungsi invers modular (modinv).
5. Tambahkan simulasi sederhana logaritma diskrit (discrete_log) untuk nyari nilai pangkat dalam sistem modular.
6. Jalankan programnya (python src/modular_math.py) buat menguji semua fungsi yang udah dibuat.
7. Terakhir, screenshot hasil eksekusi dan simpan di folder screenshots/ sebagai bukti hasil praktikum.

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

![Hasil Eksekusi](Screenshots/Eksekusi.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
- Pertanyaan 1: Apa peran aritmatika modular dalam kriptografi modern?
  
  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

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
