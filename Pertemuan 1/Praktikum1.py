# ===================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1 : Membaca seluruh isi file
# ===================================

# membuka file dengan mode read
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    # membaca seluruh isi file
    isi_file = file.read()
# menampilkan isi file
print(isi_file)

print("===Hasil Read===")
print("Tipe data:", type(isi_file))
print("Jumlah karakter:", len(isi_file))
print("Jumlah baris:", isi_file.count('\n') + 1)

# Membuka file perbaris
print("\n===Membaca File Perbaris===")
jumlah_baris = 0
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        jumlah_baris += 1
        baris = baris.strip()  # menghapus spasi dan karakter newline
        print("Baris ke-", jumlah_baris)
        print("Isinya:", baris)


# ====================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 2 : Parsing baris menjadi kolom data
# ===================================

print("\n===Parsing Baris===\n")
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip()  # menghapus spasi dan karakter newline
        nim, nama, nilai = baris.split(',')  # memisahkan berdasarkan koma
        print("NIM   :", nim, "| Nama  :", nama, "| Nilai :", nilai)

# ====================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 3 : Membaca file dan menyimpan data dalam list
# ===================================

data_list = []
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip()  # menghapus spasi dan karakter newline
        
        #Simpan sebagai list of dictionary
        data_list.append({nim, nama, int(nilai)})

print("\n===Data Mahasiswa dalam List===")
print(data_list)

print("=== Jumlah Record dalam List ===")
print(len(data_list))

print("=== Menampilkan Data Record tertentu ===")
# Menampilkan data record tertentu, misalnya record ke-2
print("Record ke-2:", data_list[1])

# ====================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 4 : Membaca file dan menyimpan ke dalam dictionary
# ===================================
data_dict = {}
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip()  # menghapus spasi dan karakter newline
        nim, nama, nilai = baris.split(',')  # memisahkan berdasarkan koma

        data_dict[nim] = {
            'nama': nama, 'nilai': int(nilai)
        }  # menyimpan dalam dictionary
print("\n===Data Mahasiswa dalam Dictionary===")
print(data_dict)