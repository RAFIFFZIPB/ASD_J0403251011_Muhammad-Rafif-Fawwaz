# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 3 : Tracing Insertion Sort
# data = [5, 2, 4, 6, 1, 3]
# ==========================================================

def insertion_sort(data):
    print("Data Awal : ", data)
    print("="*50)

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
        print(f"Iterasi {i} : {data}")

    return data

# Contoh penggunaan
data = [5, 2, 4, 6, 1, 3]
sorted_data = insertion_sort(data)
print("Hasil Sorting : ", sorted_data)

# Soal:
# 1. Tuliskan isi list setelah iterasi i = 1.
# 2. Tuliskan isi list setelah iterasi i = 3.
# 3. Berapa kali pergeseran terjadi pada iterasi i = 4?

# Jawaban:
# 1. Setelah iterasi i = 1, isi list adalah [2, 5, 4, 6, 1, 3].
# 2. Setelah iterasi i = 3, isi list adalah [1, 2, 4, 5, 6, 3].
# 3. Pada iterasi i = 4, terjadi 4 kali pergeseran (5, 4, 2, 1).