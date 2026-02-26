# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):

    # Base case: ketika panjang hasil sudah mencapai n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # Recursive case: coba tambahkan 'A' dan 'B' ke hasil
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)


# Penjelasan bagaimana jumlah kombinasi dihasilkan:
# 1. Fungsi `kombinasi` dipanggil dengan n = 2 dan hasil = ""
# 2. Karena panjang hasil belum mencapai n, maka kita mencoba menambahkan 'A'
# 3. Fungsi `kombinasi` dipanggil lagi dengan hasil = "A"
# 4. Proses ini berlanjut hingga hasil mencapai panjang n, yang merupakan base case
# 5. Ketika hasil mencapai panjang n, kita mencetak hasil tersebut dan kembali ke pemanggilan sebelumnya
# 6. Setelah mencoba dengan 'A', kita kembali dan mencoba dengan 'B' pada setiap tingkat rekursi
# 7. Hasil akhir adalah semua kombinasi huruf 'A' dan 'B' dengan panjang n, yaitu: "AA", "AB", "BA", "BB"
