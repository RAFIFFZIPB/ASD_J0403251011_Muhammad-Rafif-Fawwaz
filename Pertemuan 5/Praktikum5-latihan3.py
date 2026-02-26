# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):

    # Base case : jika index sudah mencapai akhir list, kembalikan elemen terakhir
    if index == len(data) - 1:
        return data[index]
    
    # Recursive case : cari nilai maksimum di sisa list
    maks_sisa = cari_maks(data, index + 1)

    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa
    
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# Penjelasan Alur Program:
# 1. Fungsi cari_maks(data, index) dipanggil dengan data = [3, 7, 2, 9, 5] dan index = 0
# 2. Karena index != akhir list, maka masuk ke recursive case: cari_maks(data, 1)
# 3. Proses ini berlanjut hingga index mencapai akhir list, yang merupakan base case
# 4. Base case mengembalikan elemen terakhir (5), kemudian hasil dibandingkan mundur hingga index = 0
# 5. Hasil akhir adalah 9, yang merupakan nilai maksimum dalam list