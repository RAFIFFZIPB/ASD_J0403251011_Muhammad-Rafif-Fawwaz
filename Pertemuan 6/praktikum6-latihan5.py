# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 5 : Melengkapi Fungsi Merge
# ==========================================================

# def merge(left, right):
    
#     result = [] # List untuk menyimpan hasil penggabungan
#     i = j = 0

#     # Membandingkan elemen kiri dan kanan
#     while i < len(left) and j < len(right):
#         if _______________________:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     # Menambahkan sisa data dari left atau right
#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# Soal:
# 1. Lengkapi kondisi agar menjadi ascending.
# 2. Jelaskan fungsi result.extend().

# Jawaban:
# 1. Melengkapi Kode
def merge(left, right):
    
    result = [] # List untuk menyimpan hasil penggabungan
    i = j = 0

    # Membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # Kondisi untuk ascending
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Menambahkan sisa data dari left atau right
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# 2. Penjelasan Fungsi result.extend()
# Fungsi result.extend() berguna untuk menggabungkan seluruh isi sebuah list ke list lain sekaligus. Pada kode ini, extend() dipakai untuk langsung memasukkan sisa elemen dari list 'left' atau 'right' yang belum terproses ke dalam 'result' tanpa perlu melakukan perulangan satu per satu.