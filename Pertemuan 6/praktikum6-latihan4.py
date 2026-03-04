# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 4 : Memahami Kode Program (Merge Sort)
# ==========================================================

def merge_sort(data):
    # Base case: jika panjang data kurang dari atau sama dengan 1, kembalikan data
    if len(data) <= 1:
        return data

    # Divide: bagi data menjadi dua bagian
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # Recursive call: panggil merge_sort secara rekursif untuk kedua bagian
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


# Soal:
# 1. Apa yang dimaksud dengan base case?
# 2. Mengapa fungsi memanggil dirinya sendiri?
# 3. Apa tujuan fungsi merge()?

# Jawaban Soal:
# 1. Base case adalah kondisi di mana fungsi berhenti melakukan pemanggilan rekursif, biasanya ketika data sudah cukup kecil atau sederhana untuk diproses langsung.
# 2. Fungsi memanggil dirinya sendiri untuk memecah masalah menjadi bagian yang lebih kecil, sehingga dapat diselesaikan dengan cara yang sama (divide and conquer).
# 3. Tujuan fungsi merge() adalah untuk menggabungkan dua list yang sudah terurut menjadi satu list yang juga terurut.