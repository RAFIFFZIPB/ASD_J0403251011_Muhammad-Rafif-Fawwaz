# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Materi Rekursif  : Call Stack
#  Tracing bilangan (masuk-keluar)
# input : 3
# masuk 1 - 2 - 3
# keluar
# ==========================================================

def hitung(n):
    # Base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n) # fase stacking
    hitung(n - 1) # pemanggilan rekursif
    print("Keluar:", n) # fase unwinding

hitung(3)

# Penjelasan Kode:
# 1. hitung(3) dipanggil pertama kali
# 2. Selama n != 0, fungsi mencetak "Masuk: n" lalu memanggil dirinya sendiri dengan n-1
# 3. Proses terus berulang sampai n = 0 (base case), lalu mencetak "Selesai"
# 4. Setelah "Selesai", fungsi kembali ke pemanggilan sebelumnya dan mencetak "Keluar: n"
# 5. Hal ini terus berlanjut sampai semua pemanggilan selesai dan mencetak "Keluar" dari 1 hingga 3