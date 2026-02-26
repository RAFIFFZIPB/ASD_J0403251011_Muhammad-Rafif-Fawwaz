# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):
    # Base case: ketika panjang hasil sudah mencapai panjang yang diinginkan, cetak hasil
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # Recursive case: coba tambahkan setiap angka ke hasil
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)

# Penjelasan bagaimana cara mencegah angka yang sama muncul berulang:
"""
Untuk mencegah angka yang sama muncul berulang, kita bisa menambahkan
kondisi untuk memeriksa apakah angka yang akan ditambahkan sama dengan
angka terakhir yang sudah ada di hasil. Jika sama, kita bisa melewati
penambahan tersebut dan melanjutkan ke angka berikutnya. Dengan cara ini,
kita hanya akan menghasilkan kombinasi PIN yang tidak memiliki angka
yang sama berurutan.
"""
