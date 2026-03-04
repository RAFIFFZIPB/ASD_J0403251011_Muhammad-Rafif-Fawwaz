# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Materi 1 : Insertion Sort (Ascending)
# ==========================================================

def insertion_sort(data):
    # Loop mulai dari data kedua (index array ke 1)
    for i in range(1, len(data)):
        key = data[i] # Simpan nilai data[i] sebagai key
        j = i - 1 # Inisialisasi j sebagai index sebelum i

        # Geser 
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1

        # Sisipkan key pada posisi yang benar
        data[j + 1] = key
    return data
# Contoh penggunaan
data = [7, 8, 5, 2, 4, 6]
print("Data sebelum diurutkan : ", data)
sorted_data = insertion_sort(data)
print("Hasil Sorting : ", sorted_data)