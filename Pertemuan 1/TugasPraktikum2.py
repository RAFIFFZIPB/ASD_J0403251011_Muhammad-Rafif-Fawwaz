import os

# ===================================
# Tugas Hands On: Stok Barang Kantin
# Nama File : stok_barang.txt
# ===================================

nama_file = 'stok_barang.txt'

# 1. Fungsi Membaca Data dari File
def bacaDataStok(nama_file):
    data_dict = {}
    # Cek apakah file ada sebelum membaca
    if not os.path.exists(nama_file):
        print(f"File {nama_file} tidak ditemukan. Memulai dengan data kosong.")
        return data_dict

    with open(nama_file, 'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip()
            if baris: # Pastikan baris tidak kosong
                # Format: KodeBarang,NamaBarang,Stok
                kode, nama, stok = baris.split(',')
                
                data_dict[kode] = {
                    'nama': nama, 
                    'stok': int(stok)
                }
    return data_dict

# 2. Fungsi Menampilkan Semua Barang (Menu 1)
def tampilkanDataStok(data_dict):
    print("\n=== DAFTAR STOK BARANG ===")
    print(f"{'Kode':<10} | {'Nama Barang':<20} | {'Stok':>5}")
    print("-" * 45)
    
    if not data_dict:
        print("Data kosong.")
    else:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]['nama']
            stok = data_dict[kode]['stok']
            print(f"{kode:<10} | {nama:<20} | {stok:>5}")

# 3. Fungsi Mencari Barang (Menu 2)
def cariBarang(data_dict):
    kode_input = input("\nMasukkan Kode Barang yang dicari: ").strip()

    if kode_input in data_dict:
        nama = data_dict[kode_input]['nama']
        stok = data_dict[kode_input]['stok']
        print("\n=== Barang Ditemukan ===")
        print(f"Kode : {kode_input}")
        print(f"Nama : {nama}")
        print(f"Stok : {stok}")
    else:
        print("\nBarang tidak ditemukan.")

# 4. Fungsi Menambah Barang Baru (Menu 3)
def tambahBarangBaru(data_dict):
    print("\n=== Tambah Barang Baru ===")
    kode_input = input("Masukkan Kode Barang: ").strip()

    # Validasi: Kode tidak boleh duplikat
    if kode_input in data_dict:
        print("Gagal: Kode sudah digunakan. Gunakan menu Update Stok jika ingin mengubah jumlah.")
        return

    nama_input = input("Masukkan Nama Barang: ").strip()
    
    try:
        stok_input = int(input("Masukkan Stok Awal: "))
        if stok_input < 0:
            print("Stok tidak boleh negatif.")
            return
    except ValueError:
        print("Input stok harus berupa angka.")
        return

    # Simpan ke dictionary
    data_dict[kode_input] = {
        'nama': nama_input,
        'stok': stok_input
    }
    print(f"Berhasil: {nama_input} ditambahkan dengan stok {stok_input}.")

# 5. Fungsi Update Stok (Menu 4)
def updateStokBarang(data_dict):
    print("\n=== Update Stok Barang ===")
    kode_input = input("Masukkan Kode Barang: ").strip()

    if kode_input not in data_dict:
        print("Barang tidak ditemukan.")
        return

    print(f"Barang: {data_dict[kode_input]['nama']} (Stok saat ini: {data_dict[kode_input]['stok']})")
    print("1. Tambah Stok")
    print("2. Kurangi Stok")
    pilihan = input("Pilih aksi (1/2): ")

    try:
        jumlah = int(input("Masukkan jumlah stok: "))
        if jumlah < 0:
            print("Jumlah harus positif.")
            return
            
        stok_lama = data_dict[kode_input]['stok']
        
        if pilihan == "1":
            # Menambah stok
            data_dict[kode_input]['stok'] += jumlah
            print(f"Stok berhasil ditambah. Stok sekarang: {data_dict[kode_input]['stok']}")
            
        elif pilihan == "2":
            # Mengurangi stok (Validasi tidak boleh negatif)
            if stok_lama - jumlah < 0:
                print(f"Gagal: Stok tidak mencukupi untuk dikurangi {jumlah}. Sisa stok: {stok_lama}")
            else:
                data_dict[kode_input]['stok'] -= jumlah
                print(f"Stok berhasil dikurangi. Stok sekarang: {data_dict[kode_input]['stok']}")
        else:
            print("Pilihan tidak valid.")
            
    except ValueError:
        print("Input harus berupa angka.")

# 6. Fungsi Simpan ke File (Menu 5)
def simpanData(nama_file, data_dict):
    try:
        with open(nama_file, 'w', encoding='utf-8') as file:
            for kode in sorted(data_dict.keys()):
                nama = data_dict[kode]['nama']
                stok = data_dict[kode]['stok']
                # Format tulis ulang: Kode,Nama,Stok
                baris = f"{kode},{nama},{stok}\n"
                file.write(baris)
        print(f"\nSeluruh data berhasil disimpan ke {nama_file}.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan: {e}")

# ===================================
# Program Utama (Main Loop)
# ===================================

def main():
    # Load data saat program dimulai
    data_stok = bacaDataStok(nama_file)
    print(f"Berhasil memuat {len(data_stok)} data barang.")

    while True:
        print("\n" + "="*40)
        print(" MENU MANAJEMEN STOK KANTIN")
        print("="*40)
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang (by Kode)")
        print("3. Tambah Barang Baru")
        print("4. Update Stok Barang (Tambah/Kurang)")
        print("5. Simpan Data ke File")
        print("0. Keluar")
        print("="*40)
        
        pilihan = input("Pilih menu (0-5): ")

        if pilihan == "1":
            tampilkanDataStok(data_stok)
        elif pilihan == "2":
            cariBarang(data_stok)
        elif pilihan == "3":
            tambahBarangBaru(data_stok)
        elif pilihan == "4":
            updateStokBarang(data_stok)
        elif pilihan == "5":
            simpanData(nama_file, data_stok)
        elif pilihan == "0":
            print("Program selesai. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()