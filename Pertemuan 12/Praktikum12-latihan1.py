# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================
# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang 
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 
# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D'] # Jalur A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # Jalur A -> C -> D

# Menampilkan hasil perhitungan jalur
print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2)

# Menentukan jalur terpendek
if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D")

# Pertanyaan Analisis 
# Tuliskan jawaban sebagai komentar di bagian bawah program. 
# # Jawaban Analisis: 
# # 1. Berapa total bobot jalur A -> B -> D?
# # 2. Berapa total bobot jalur A -> C -> D? 
# # 3. Jalur mana yang dipilih sebagai jalur terpendek? 
# # 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit? 

# Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D adalah 4 (A ke B) + 5 (B ke D) = 9.
# 2. Total bobot jalur A -> C -> D adalah 2 (A ke C) + 1 (C ke D) = 3.
# 3. Jalur yang dipilih sebagai jalur terpendek adalah A -> C -> D karena memiliki total bobot yang lebih kecil (3) dibandingkan dengan jalur A -> B -> D (9).
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit karena setiap edge memiliki bobot yang berbeda. Sebuah jalur dengan lebih banyak edge bisa memiliki total bobot yang lebih kecil jika edge-edge tersebut memiliki bobot yang rendah, sedangkan jalur dengan sedikit edge bisa memiliki total bobot yang lebih besar jika edge-edge tersebut memiliki bobot yang tinggi. Oleh karena itu, untuk menentukan jalur terpendek, kita harus mempertimbangkan total bobot dari jalur tersebut, bukan hanya jumlah edge-nya.