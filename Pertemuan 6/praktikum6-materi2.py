# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Materi 2 : Insertion Sort dengan Tracing
# ==========================================================

def insertion_sort(data):

    #melihat data awal
    print ("Data Awal : ", data)
    print("="*50)

    # Loop mulai dari data kedua (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] # Simpan nilai data[i] sebagai key
        j = i - 1 # Inisialisasi j sebagai index sebelum i

        print(f"Iterasi ke-{i} :")
        print(f"Nilai Key yang akan disisipkan : {key}")
        print(f"Bagian kiri (yang sudah diurutkan) : {data[:i]}")
        print(f"Bagian kanan (yang belum diurutkan) : {data[i:]}")


        # Geser 
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        # Sisipkan key pada posisi yang benar
        data[j + 1] = key

        print(f"Setelah disisipkan : {data}")
        print("-"*50)
    return data

# Contoh penggunaan
data = [7, 8, 5, 2, 4, 6]
sorted_data = insertion_sort(data)
print("Hasil Sorting : ", sorted_data)    