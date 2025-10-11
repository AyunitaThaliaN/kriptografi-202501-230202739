# Laporan Praktikum Kriptografi
Minggu ke-: 1 
Topik: CIA_intro.md  
Nama: Ayunita 
NIM: 230202739  
Kelas: 5IKRB  


Soal 1. Ringkasan Sejarah Kriptografi cryptography
•	Babak Klasik (Zaman Dulu): Awalnya, kriptografi itu seperti mainan teka-teki huruf. Ada Caesar Cipher yang cuma menggeser-geser urutan alfabet—sangat gampang ditebak. Lalu ada Vigenère Cipher yang lebih canggih karena pakai kata kunci, jadi lebih sulit dipecahkan. Puncaknya adalah mesin Enigma di Perang Dunia II, sebuah alat mekanis rumit yang akhirnya berhasil dijinakkan oleh Alan Turing. Intinya, di era ini keamanan bergantung pada kerahasiaan metodenya.
•	Babak Modern (Era Komputer): Sejak ada komputer, kriptografi beralih dari seni menjadi ilmu matematika. Prinsipnya berubah: metodenya boleh terbuka, yang penting kuncinya rahasia.
o	Kriptografi Simetris (AES): Pakai satu kunci yang sama untuk mengunci dan membuka data. Mirip kunci rumah biasa. AES adalah standarnya sekarang, dipakai untuk mengamankan hampir semuanya, dari file di laptop sampai koneksi Wi-Fi.
o	Kriptografi Asimetris (RSA): Ini terobosannya. Ada dua kunci: kunci publik (seperti gembok yang bisa dibagikan ke semua orang) dan kunci privat (kunci untuk membuka gembok itu, yang hanya kamu miliki). RSA adalah teknologi di balik ikon gembok (HTTPS) di browsermu.
•	Babak Kontemporer (Era Internet & Desentralisasi): Sekarang, kriptografi digunakan untuk membangun kepercayaan di dunia digital tanpa perlu ada "pihak ketiga" atau otoritas pusat. Contoh terbesarnya adalah Blockchain dan Cryptocurrency. Teknologi ini menggunakan fungsi hash (untuk membuat sidik jari digital yang unik dan tak bisa diubah) dan tanda tangan digital (menggunakan kunci privat untuk membuktikan kepemilikan aset) agar semua transaksi aman dan terverifikasi tanpa perlu bank.

Soal 2. Prinsip Keamanan Informasi (CIA Triad)
1.	Confidentiality (Kerahasiaan): Intinya, yang tidak berhak, tidak boleh tahu isinya. Informasi sensitif harus dijaga agar tidak bocor.
o	Contoh: Fitur end-to-end encryption di WhatsApp. Hanya pengirim dan penerima yang bisa membaca pesan. Pihak WhatsApp sendiri pun tidak bisa mengintip.
2.	Integrity (Integritas): Artinya, data harus tetap asli dan tidak diubah-ubah oleh orang yang tidak berwenang. Ini soal keutuhan dan keaslian.
o	Contoh: Saat mengunduh aplikasi, sering ada kode checksum atau hash. Jika kode dari file yang kita unduh cocok dengan yang tertera di situs resminya, berarti file itu aman dan tidak disusupi apa pun di tengah jalan.
3.	Availability (Ketersediaan): Maksudnya, sistem dan data harus bisa diakses saat dibutuhkan oleh pengguna yang sah. Sistem tidak boleh mati atau terganggu.
o	Contoh: Situs web perbankan harus online 24/7. Mereka menggunakan server cadangan di banyak tempat. Jika satu server mati, server lain akan langsung mengambil alih, sehingga nasabah tetap bisa bertransaksi kapan saja.

 Jawaban Soal Quiz
1.  Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
 Tokoh yang dianggap sebagai bapak kriptografi modern adalah Claude Shannon. Melalui makalahnya yang monumental pada tahun 1949, "Communication Theory of Secrecy Systems," ia meletakkan fondasi matematis dan teoretis untuk kriptografi, mengubahnya dari sekadar seni menjadi sebuah ilmu pasti.
2. Sebutkan algoritma kunci publik yang populer digunakan saat ini
•	RSA (Rivest-Shamir-Adleman): Digunakan secara luas untuk enkripsi dan tanda tangan digital, terutama dalam protokol keamanan web seperti TLS/SSL.
•	ECC (Elliptic Curve Cryptography): Menawarkan tingkat keamanan yang sama dengan RSA tetapi dengan ukuran kunci yang jauh lebih kecil, membuatnya sangat efisien untuk perangkat dengan sumber daya terbatas seperti smartphone.
•	Diffie-Hellman Key Exchange: Sebuah metode untuk dua pihak yang tidak saling kenal untuk secara aman menyepakati kunci rahasia bersama melalui saluran komunikasi yang tidak aman.
•	DSA (Digital Signature Algorithm): Standar yang digunakan oleh pemerintah AS untuk membuat tanda tangan digital.
3.Apa perbedaan utama antara kriptografi klasik dan kriptografi modern ?
 Perbedaan utama anatara kriptografi klasik dan kriptografi modern terletak pada basis keamanan,kompleksitas, dan prinsip dasarnya. 
a.	Kriptografi klasik berfokus pada manipulasi karakter dan Bahasa menggunakan metode substitusi dan transposisi, dengan proses yang relatif sederhana dan dapat dilakukan secara manual. Keamanannya bergantung pada kerahasiaan algoritma yang digunakan.

b.	Kriptografi modern didasarkan pada matematika kompleks serta manipulasi data biner (bit), dan memerlukan komputer untuk melakukan perhitungan yang rumit. Prinsip keamanannya bergantung pada kerahasiaan kunci sesuai Prinsip Kerckhoffs, bukan pada algoritmanya. Selain itu, kriptografi modern memperkenalkan penggunaan kunci simetris seperti AES dan kunci asimetris/publik seperti RSA dan ECC, yang membuat sistemnya lebih aman dan efisien dibandingkan kriptografi klasik.




