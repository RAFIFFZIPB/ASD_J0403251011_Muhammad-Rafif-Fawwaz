# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
    # Base case: berhenti ketika n = 0
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n)

    # Recursive case: memanggil countdown dengan n dikurangi 1
    countdown(n - 1)
    
    print("Keluar:", n)

countdown(3)

# Penjelasan Mengapa Output "Keluar" muncul terbalik :
"""
Output "Keluar" muncul terbalik karena sifat rekursi yang menggunakan stack.
Ketika fungsi countdown dipanggil, setiap pemanggilan baru ditambahkan ke stack.
Setelah mencapai base case (n = 0), fungsi mulai kembali ke pemanggilan sebelumnya,
sehingga "Keluar" dicetak dalam urutan terbalik dari saat "Masuk" dicetak.
"""