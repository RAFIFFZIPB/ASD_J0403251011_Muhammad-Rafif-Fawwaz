# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Materi Rekursif  : Faktorial
# Recursive case => 3! = 3 x 2 x 1
# Base case => 0! = 1 berhenti ketika n = 0
# ==========================================================

def faktorial(n):
    # Base case: berhenti ketika n = 0
    if n == 0:
        return 1
    
    # Recursive case: masalah diperkecil menjadi faktorial(n-1)
    return n * faktorial(n - 1)
print(faktorial(5)) # Output: 120

# Penjelasan Kode:
# 1. Fungsi faktorial(n) dipanggil dengan n = 5
# 2. Karena n != 0, maka masuk ke recursive case: 5 * faktorial(4)
# 3. Proses ini berlanjut hingga n = 0, yang merupakan base case
# 4. Base case mengembalikan 1, kemudian hasil dikalikan mundur hingga n = 5
# 5. Hasil akhir adalah 120