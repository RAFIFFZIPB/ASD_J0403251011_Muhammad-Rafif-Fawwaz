# ===================================
# Praktikum 2: Konsep ADT dan File Handling (Studi Kasus)
# Latihan Dasar 1 : Membuat fungsi load data
# ===================================

nama_file = 'data_mahasiswa.txt'

def bacaDataMahasiswa(nama_file):
    data_dict = {}
    with open(nama_file, 'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip()  # menghapus spasi dan karakter newline
            nim, nama, nilai = baris.split(',')  # memisahkan berdasarkan koma

            data_dict[nim] = {
                'nama': nama, 'nilai': int(nilai)
            }  # menyimpan dalam dictionary
    return data_dict

buka_file = bacaDataMahasiswa(nama_file)
# print("jumlah data mahasiswa:", len(buka_file))

# ===================================
# Praktikum 2: Konsep ADT dan File Handling (Studi Kasus)
# Latihan Dasar 2 : Membuat fungsi menampilkan data
# ===================================

def tampilkanDataMahasiswa(data_dict):
    # Menampilkan header tabel
    print("\n")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>10}")
    print("-" * 50)
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]['nama']
        nilai = data_dict[nim]['nilai']
        print(f"{nim:<10} {nama:<12} {nilai:>10}")

# Memanggil fungsi untuk menampilkan data mahasiswa
# tampilkanDataMahasiswa(buka_file)

# ===================================
# Praktikum 2: Konsep ADT dan File Handling (Studi Kasus)
# Latihan Dasar 3 : Membuat fungsi mencari data
# ===================================

def cariDataMahasiswa(data_dict):

    nim_input = input("\nMasukkan NIM yang ingin dicari: ")

    if nim_input in data_dict:
        nama = data_dict[nim_input]['nama']
        nilai = data_dict[nim_input]['nilai']
        print("\n=== Data Mahasiswa Ditemukan: ===")
        print(f"NIM: {nim_input}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("\nData Mahasiswa Tidak Ditemukan.")

# Memanggil fungsi untuk mencari data mahasiswa
# cariDataMahasiswa(buka_file)

# ===================================
# Praktikum 2: Konsep ADT dan File Handling (Studi Kasus)
# Latihan Dasar 4 : Membuat fungsi update nilai
# ===================================

# Fungsi untuk mengupdate nilai mahasiswa berdasarkan NIM
def updateNilaiMahasiswa(data_dict):

    # Meminta input NIM dari pengguna
    nim_input = input("\nMasukkan NIM yang nilainya ingin diupdate: ")

    # Jika NIM tidak ditemukan di data, batalkan operasi
    if nim_input not in data_dict:
        print("\nData Mahasiswa Tidak Ditemukan. Update dibatalkan.")
        return

    # Minta input nilai baru, bersihkan spasi lalu konversi ke int
    # (letak .strip() harus sebelum konversi ke int untuk menghindari error)
    try:
        nilai_str = input("Masukkan nilai baru(0-100): ").strip()
        nilai_baru = int(nilai_str)
    except ValueError:
        print("\nInput nilai tidak valid. Harap masukkan angka.")
        return

    # Validasi rentang nilai (0-100)
    if nilai_baru < 0 or nilai_baru > 100:
        print("\nNilai tidak valid. Harap masukkan nilai antara 0 dan 100.")
        return

    # Simpan perubahan dan beri konfirmasi
    nilai_lama = data_dict[nim_input]['nilai']
    data_dict[nim_input]['nilai'] = nilai_baru
    print(f"\nNilai mahasiswa dengan NIM {nim_input} berhasil diupdate dari {nilai_lama} menjadi {nilai_baru}.")
# Memanggil fungsi untuk mengupdate nilai mahasiswa
# updateNilaiMahasiswa(buka_file)


# ===================================
# Praktikum 2: Konsep ADT dan File Handling (Studi Kasus)
# Latihan Dasar 5 : Membuat fungsi simpan data
# ===================================

def simpanDataMahasiswa(nama_file, data_dict):
    with open(nama_file, 'w', encoding='utf-8') as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['nama']
            nilai = data_dict[nim]['nilai']
            baris = f"{nim},{nama},{nilai}\n"
            file.write(baris)
    print("\nData mahasiswa berhasil disimpan ke file.")
# Memanggil fungsi untuk menyimpan data mahasiswa
# simpanDataMahasiswa(nama_file, buka_file)

# ===================================
# Praktikum 2: Konsep ADT dan File Handling (Studi Kasus)
# Latihan Dasar 6 : Membuat menu program
# ===================================

def main():

    #Menjalankan fungsi 1 untuk load data
    buka_file = bacaDataMahasiswa(nama_file)

    while True:
        print("\n=== Menu Program Manajemen Data Mahasiswa ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Update Nilai Mahasiswa")
        print("4. Simpan Data Mahasiswa")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkanDataMahasiswa(buka_file)
        elif pilihan == "2":
            cariDataMahasiswa(buka_file)
        elif pilihan == "3":
            updateNilaiMahasiswa(buka_file)
        elif pilihan == "4":
            simpanDataMahasiswa(nama_file, buka_file)
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
# Menjalankan program utama
if __name__ == "__main__":
    main()