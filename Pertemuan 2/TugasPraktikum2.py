# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output:
    - stok_dict (dictionary)
      key = kode_barang
      value = {"nama": nama_barang, "stok": stok_int}
    """
    stok_dict = {}
    
    # TODO: Buka file dan baca seluruh baris
    # Menggunakan try-except untuk menangani jika file belum ada
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            # TODO: Untuk setiap baris:
            for baris in f:
                # - gunakan strip() untuk menghilangkan \n
                baris = baris.strip()
                # Cek jika baris kosong agar tidak error
                if not baris:
                    continue
                
                # - split(",") untuk memisahkan kolom
                parts = baris.split(",")
                
                # Pastikan format datanya pas (ada 3 bagian) untuk menghindari crash
                if len(parts) == 3:
                    kode, nama, stok = parts
                    # - simpan ke dictionary
                    stok_dict[kode] = {
                        "nama": nama, 
                        "stok": int(stok)
                    }
    except FileNotFoundError:
        print(f"Info: File {nama_file} belum ada. Memulai dengan data kosong.")
            
    return stok_dict

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    # TODO: Tulis ulang seluruh isi file berdasarkan stok_dict
    try:
        with open(nama_file, "w", encoding="utf-8") as f:
            # Kita urutkan key-nya agar file tersimpan rapi
            for kode in sorted(stok_dict.keys()):
                nama = stok_dict[kode]["nama"]
                stok = stok_dict[kode]["stok"]
                f.write(f"{kode},{nama},{stok}\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan: {e}")

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """
    print("\n--- DAFTAR STOK BARANG ---")
    
    # TODO: Jika kosong, tampilkan pesan stok kosong
    if not stok_dict:
        print("Data stok kosong.")
        return

    # TODO: Tampilkan dengan format rapi: kode | nama | stok
    print(f"{'Kode':<10} | {'Nama Barang':<20} | {'Stok':>5}")
    print("-" * 45)
    
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<20} | {stok:>5}")

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    print("\n--- CARI BARANG ---")
    kode = input("Masukkan kode barang: ").strip()
    
    # TODO: Cek apakah kode ada di dictionary
    if kode in stok_dict:
        # Jika ada: tampilkan detail barang
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"Ditemukan -> Kode: {kode}, Nama: {nama}, Stok: {stok}")
    else:
        # Jika tidak ada: tampilkan 'Barang tidak ditemukan'
        print("Barang tidak ditemukan.")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    print("\n--- TAMBAH BARANG BARU ---")
    kode = input("Masukkan kode barang baru: ").strip()
    
    # TODO: Validasi kode tidak boleh duplikat
    if kode in stok_dict:
        # Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return
        print(f"Gagal: Kode {kode} sudah digunakan. Gunakan menu Update Stok.")
        return

    nama = input("Masukkan nama barang: ").strip()
    
    # TODO: Input stok awal (integer)
    try:
        stok_awal = int(input("Masukkan stok awal: "))
        if stok_awal < 0:
            print("Stok tidak boleh negatif.")
            return
            
        # TODO: Simpan ke dictionary
        stok_dict[kode] = {"nama": nama, "stok": stok_awal}
        print(f"Berhasil menambahkan {nama} (Stok: {stok_awal})")
        
    except ValueError:
        print("Input stok harus berupa angka.")

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    print("\n--- UPDATE STOK BARANG ---")
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    
    # TODO: Cek apakah kode ada di dictionary
    # Jika tidak ada: tampilkan pesan dan return
    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return

    print(f"Barang: {stok_dict[kode]['nama']} (Stok saat ini: {stok_dict[kode]['stok']})")
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()
    
    # TODO: Input jumlah perubahan stok
    try:
        jumlah = int(input("Masukkan jumlah: "))
        if jumlah < 0:
            print("Jumlah harus positif.")
            return

        stok_sekarang = stok_dict[kode]["stok"]

        # TODO:
        # - Jika pilihan 1: stok = stok + jumlah
        if pilihan == "1":
            stok_dict[kode]["stok"] = stok_sekarang + jumlah
            print(f"Stok berhasil ditambah. Total sekarang: {stok_dict[kode]['stok']}")
            
        # - Jika pilihan 2: stok = stok - jumlah
        elif pilihan == "2":
            # - Jika hasil < 0: batalkan dan tampilkan error
            if stok_sekarang - jumlah < 0:
                print(f"Gagal: Stok tidak cukup. Sisa stok hanya {stok_sekarang}.")
            else:
                stok_dict[kode]["stok"] = stok_sekarang - jumlah
                print(f"Stok berhasil dikurangi. Sisa sekarang: {stok_dict[kode]['stok']}")
        else:
            print("Pilihan menu update tidak valid.")
            
    except ValueError:
        print("Input jumlah harus berupa angka.")

# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(NAMA_FILE)
    
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()