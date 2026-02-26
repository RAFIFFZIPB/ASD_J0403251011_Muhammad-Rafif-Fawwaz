# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================

def jumlah_list(data, index=0):
   # Base case: jika index sudah mencapai panjang list
   if index == len(data):
      return 0
   
   # Recursive case: elemen sekarang + jumlah elemen setelahnya
   return data[index] + jumlah_list(data, index + 1)
print(jumlah_list([2, 4, 6, 8])) # Output: 20

# Penjelasan Kode:
# 1. Fungsi jumlah_list(data, index) dipanggil dengan data = [2, 4, 6, 8] dan index = 0
# 2. Karena index != panjang list, maka masuk ke recursive case: data[0] + jumlah_list(data, 1)
# 3. Proses ini berlanjut hingga index mencapai panjang list, yang merupakan base case
# 4. Base case mengembalikan 0, kemudian hasil dikalikan mundur hingga index = 0
# 5. Hasil akhir adalah 20