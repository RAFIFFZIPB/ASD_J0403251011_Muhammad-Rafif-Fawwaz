# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Contoh Backtracking 1: Kombinasi biner (n)
# ==========================================================

def biner(n, hasil=""):
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # Choose + Explore: tambah '0'
    biner(n, hasil + "0")
    # Choose + Explore: tambah '1'
    biner(n, hasil + "1")

biner(3)

# Penjelasan Kode:
# 1. Fungsi biner(n, hasil) dipanggil dengan n = 3 dan hasil = ""
# 2. Setiap pemanggilan akan mencoba menambahkan '0' atau '1' ke string hasil
# 3. Proses ini terus berulang sampai panjang string hasil sama dengan n
# 4. Jika panjang string sudah mencapai n, string tersebut dicetak (contoh: "000", "001", dll.)
# 5. Setelah dicetak, fungsi kembali ke pemanggilan sebelumnya dan mencoba pilihan lain ('1')
# 6. Langkah ini terus berulang hingga semua kombinasi biner sebanyak n digit tercetak