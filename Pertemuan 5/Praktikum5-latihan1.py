# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    # Base case: ketika n = 0, kembalikan 1
    if n == 0: 
        return 1
    
    # Recursive case: kembalikan a dikalikan dengan pangkat(a, n - 1)
    return a * pangkat(a, n - 1)

print(pangkat(2, 4)) # Output: 16

# Penjelasan Alur Program:
# 1. Fungsi pangkat(a, n) dipanggil dengan a = 2 dan n = 4
# 2. Karena n != 0, maka masuk ke recursive case: 2 * pangkat(2, 3)
# 3. Proses ini berlanjut hingga n = 0, yang merupakan base case
# 4. Base case mengembalikan 1, kemudian hasil dikalikan mundur hingga n = 4
# 5. Hasil akhir adalah 16