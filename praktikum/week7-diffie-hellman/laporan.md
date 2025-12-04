# Laporan Praktikum Kriptografi
Minggu ke-: 7 
Topik: [Diffie Helman]  
Nama: [Ayunita Thalia Nugraheni]  
NIM: [230202739]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).



## 2. Dasar Teori
Diffie-Hellman adalah metode kriptografi untuk bertukar kunci rahasia secara aman melalui jaringan publik tanpa mengirimkan kunci secara langsung. Metode ini bekerja dengan memanfaatkan perhitungan matematika berbasis perpangkatan modulo sehingga dua pihak dapat menghasilkan kunci rahasia yang sama. Diffie-Hellman banyak digunakan dalam sistem keamanan komunikasi seperti HTTPS dan VPN.


## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- 


## 4. Langkah Percobaan
-Membuat project baru dan repository Git, serta membuat file program, misalnya diffie_hellman.py.
-Mendefinisikan dua parameter publik yang akan disepakati oleh Alice dan Bob, yaitu: • Bilangan prima besar (p). • Basis atau generator (g).
-Membuat fungsi atau bagian program untuk Alice dan Bob: • Masing-masing pihak memilih bilangan rahasia (a \text{ dan } b) (kunci privat). •Masing-masing pihak menghitung kunci publik mereka, A = g^a \pmod{p} dan B = g^b \pmod{p}.
-Mensimulasikan pertukaran kunci publik A dan B
-Masing-masing pihak menghitung kunci rahasia bersama 
K: • Alice menghitung K_A = B^a \pmod{p}. • Bob menghitung K_B = A^b \pmod{p}.
-Memverifikasi bahwa K_A dan K_B adalah sama (kunci rahasia bersama telah berhasil didirikan).
-Menjalankan program dengan perintah, misalnya, python diffie_hellman.py.

## 5. Source Code
# --- Parameter Publik (Disepakati) ---
P = 23 # Bilangan prima
G = 5  # Generator

# --- Pihak Alice ---
def alice_turn():
    # Kunci Rahasia Alice (a)
    a_private = 6
    print(f"Alice memilih kunci rahasia (a): {a_private}")
    
    # Hitung Kunci Publik Alice (A)
    # A = G^a mod P
    A_public = pow(G, a_private, P)
    print(f"Kunci Publik Alice (A): {G}^{a_private} mod {P} = {A_public}")
    return a_private, A_public

# --- Pihak Bob ---
def bob_turn():
    # Kunci Rahasia Bob (b)
    b_private = 15
    print(f"Bob memilih kunci rahasia (b): {b_private}")

    # Hitung Kunci Publik Bob (B)
    # B = G^b mod P
    B_public = pow(G, b_private, P)
    print(f"Kunci Publik Bob (B): {G}^{b_private} mod {P} = {B_public}")
    return b_private, B_public

# --- Pertukaran Kunci dan Hasil Akhir ---
def exchange_and_calculate(A, B, a, b):
    print("\n--- Pertukaran Kunci Publik (A dan B) ---")
    
    # Alice menghitung kunci rahasia bersama (K_A)
    # K_A = B^a mod P
    K_A = pow(B, a, P)
    print(f"Alice menghitung Kunci Bersama (K_A): {B}^{a} mod {P} = {K_A}")

    # Bob menghitung kunci rahasia bersama (K_B)
    # K_B = A^b mod P
    K_B = pow(A, b, P)
    print(f"Bob menghitung Kunci Bersama (K_B): {A}^{b} mod {P} = {K_B}")

    print("\n--- Verifikasi ---")
    if K_A == K_B:
        print(f"Kedua kunci bersama sama! Kunci Rahasia Bersama: {K_A}")
    else:
        print("Gagal! Kedua kunci tidak sama.")

# --- Eksekusi Program Utama ---
if __name__ == "__main__":
    print(f"Parameter Publik: P={P}, G={G}")
    
    a_private, A_public = alice_turn()
    b_private, B_public = bob_turn()
    
    exchange_and_calculate(A_public, B_public, a_private, b_private)
---

## 6. Hasil dan Pembahasan
Hasil pengujian program menunjukkan bahwa proses Diffie-Hellman berjalan dengan baik dan sesuai dengan yang diharapkan. Pada tahap pembentukan kunci publik, Alice berhasil menghasilkan nilai A = 8 dan Bob menghasilkan nilai B = 19. Selanjutnya, pada tahap pembentukan kunci rahasia, Alice menghitung K_A = B^a mod p dan Bob menghitung K_B = A^b mod p. Hasil perhitungan menunjukkan bahwa kedua nilai kunci rahasia tersebut sama, yaitu 2. Kesamaan ini membuktikan bahwa proses pertukaran kunci melalui jaringan yang tidak aman tetap berhasil menghasilkan kunci yang sama. Keamanan kunci tersebut dijamin karena sangat sulit untuk menentukan kunci privat dari nilai publik yang ada akibat kompleksitas perhitungan logaritma diskrit.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/HASIL.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?
Diffie-Hellman memungkinkan pertukaran kunci di saluran publik karena proses pembentukan kunci rahasianya didasarkan pada operasi matematika yang sangat sulit dibalik, yaitu masalah logaritma diskrit. Meskipun nilai publik seperti p, g, A, dan B dapat diketahui oleh siapa pun, kunci privat a dan b tetap tidak dapat dengan mudah dihitung. Dengan begitu, kedua pihak tetap dapat menghasilkan kunci rahasia yang sama secara aman melalui perhitungan K = B^a mod p dan K = A^b mod p, meskipun proses pertukaran datanya dilakukan di jaringan terbuka.
- Pertanyaan 2: Apa kelemahan utama protokol Diffie-Hellman murni?
Kelemahan utama protokol Diffie-Hellman murni adalah rentan terhadap serangan Man-in-the-Middle (MITM) karena protokol ini tidak memiliki mekanisme autentikasi, sehingga penyerang dapat menyamar sebagai pihak yang berkomunikasi dan menyisipkan kunci palsu tanpa terdeteksi.
- Pertanyaan 3: Bagaimana cara mencegah serangan MITM pada protokol ini?
Serangan Man-in-the-Middle (MITM) pada Diffie-Hellman dapat dicegah dengan menambahkan mekanisme autentikasi, seperti:
-Menggunakan sertifikat digital (TLS/SSL) untuk memverifikasi identitas pihak yang berkomunikasi.
-Menggunakan tanda tangan digital (Digital Signature) pada pertukaran kunci.
-Menggunakan Pre-Shared Key (PSK) yang sudah disepakati sebelumnya.
Dengan autentikasi ini, penyusup tidak bisa menyamar sebagai Alice atau Bob.


## 8. Kesimpulan
Diffie-Hellman merupakan metode pertukaran kunci yang memungkinkan dua pihak membentuk kunci rahasia yang sama melalui jaringan publik secara aman dengan memanfaatkan kesulitan perhitungan logaritma diskrit. Meskipun efektif untuk membentuk kunci bersama, protokol ini tetap memerlukan mekanisme autentikasi tambahan agar terhindar dari serangan Man-in-the-Middle.


## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
commit week7-diffie-hellman
Author: Nama Mahasiswa <email>
Date:   2025-12-4

    week7-diffie-helman
```
