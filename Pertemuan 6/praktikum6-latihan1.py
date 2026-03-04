# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 1 : Memahami Kode Program (Insertion Sort)
# ==========================================================

def insertion_sort(data):
    # Loop mulai dari data kedua (index array ke 1)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

    # Geser elemen data[0..i-1], yang lebih besar dari key, ke satu posisi di depan posisi saat ini
    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1

    # Sisipkan key pada posisi yang benar
    data[j + 1] = key

    return data

# Soal:
# 1. Mengapa perulangan dimulai dari indeks 1?
# 2. Apa fungsi variabel key?
# 3. Mengapa digunakan while, bukan for?
# 4. Operasi apa yang terjadi di dalam while?

# Jawaban Soal:
# 1. Karena elemen pertama (indeks 0) dianggap sudah terurut, jadi proses penyisipan dimulai dari indeks 1.
# 2. Menyimpan nilai elemen yang sedang diproses untuk dibandingkan dan disisipkan ke posisi yang tepat.
# 3. Karena jumlah pergeseran tidak diketahui pasti, "while" lebih cocok untuk berhenti saat kondisi terpenuhi.
# 4. Menggeser elemen yang lebih besar dari "key" ke kanan, memberi ruang agar "key" bisa disisipkan.