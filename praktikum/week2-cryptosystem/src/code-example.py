import random
import string

class SubstitusiCipher:
    def __init__(self, kunci=None):
        """
        Inisialisasi cipher dengan kunci substitusi.
        Jika kunci tidak diberikan, generate kunci acak.
        """
        self.alfabet = string.ascii_lowercase
        
        if kunci:
            self.kunci = kunci.lower()
        else:
            # Generate kunci acak dengan mengacak alfabet
            kunci_list = list(self.alfabet)
            random.shuffle(kunci_list)
            self.kunci = ''.join(kunci_list)
        
        # Buat mapping untuk enkripsi dan dekripsi
        self.enkripsi_map = str.maketrans(self.alfabet, self.kunci)
        self.dekripsi_map = str.maketrans(self.kunci, self.alfabet)
    
    def enkripsi(self, plaintext):
        """
        Enkripsi teks menggunakan kunci substitusi.
        """
        hasil = []
        for char in plaintext:
            if char.lower() in self.alfabet:
                # Pertahankan case (huruf besar/kecil)
                if char.isupper():
                    hasil.append(char.lower().translate(self.enkripsi_map).upper())
                else:
                    hasil.append(char.translate(self.enkripsi_map))
            else:
                # Karakter non-alfabet tetap sama
                hasil.append(char)
        return ''.join(hasil)
    
    def dekripsi(self, ciphertext):
        """
        Dekripsi teks terenkripsi menggunakan kunci substitusi.
        """
        hasil = []
        for char in ciphertext:
            if char.lower() in self.alfabet:
                # Pertahankan case (huruf besar/kecil)
                if char.isupper():
                    hasil.append(char.lower().translate(self.dekripsi_map).upper())
                else:
                    hasil.append(char.translate(self.dekripsi_map))
            else:
                # Karakter non-alfabet tetap sama
                hasil.append(char)
        return ''.join(hasil)
    
    def tampilkan_kunci(self):
        """
        Tampilkan mapping kunci substitusi.
        """
        print("\n=== KUNCI SUBSTITUSI ===")
        print(f"Alfabet: {self.alfabet.upper()}")
        print(f"Kunci  : {self.kunci.upper()}")
        print("========================\n")


def main():
    print("=" * 50)
    print("SIMULASI ENKRIPSI & DEKRIPSI SUBSTITUSI CIPHER")
    print("=" * 50)
    
    # Menu pilihan
    print("\n1. Gunakan kunci acak (otomatis)")
    print("2. Masukkan kunci sendiri")
    pilihan = input("\nPilih opsi (1/2): ").strip()
    
    if pilihan == "2":
        print("\nKunci harus berisi 26 huruf unik (a-z)")
        kunci_input = input("Masukkan kunci: ").strip()
        
        # Validasi kunci
        if len(kunci_input) != 26 or len(set(kunci_input.lower())) != 26:
            print("Kunci tidak valid! Menggunakan kunci acak...")
            cipher = SubstitusiCipher()
        else:
            cipher = SubstitusiCipher(kunci_input)
    else:
        cipher = SubstitusiCipher()
    
    cipher.tampilkan_kunci()
    
    # Input teks
    plaintext = input("Masukkan teks yang akan dienkripsi: ")
    
    # Enkripsi
    ciphertext = cipher.enkripsi(plaintext)
    print(f"\nTeks Terenkripsi: {ciphertext}")
    
    # Dekripsi
    teks_dekripsi = cipher.dekripsi(ciphertext)
    print(f"Teks Terdekripsi: {teks_dekripsi}")
    
    # Verifikasi
    print(f"\nVerifikasi: {'✓ Berhasil' if plaintext == teks_dekripsi else '✗ Gagal'}")
    
    # Contoh dengan teks berbeda
    print("\n" + "=" * 50)
    print("CONTOH TAMBAHAN")
    print("=" * 50)
    
    contoh_teks = [
        "Hello World!",
        "Keamanan Data 2025",
        "Python Programming"
    ]
    
    for teks in contoh_teks:
        enkripsi = cipher.enkripsi(teks)
        dekripsi = cipher.dekripsi(enkripsi)
        print(f"\nOriginal : {teks}")
        print(f"Enkripsi : {enkripsi}")
        print(f"Dekripsi : {dekripsi}")


if __name__ == "__main__":
    main()