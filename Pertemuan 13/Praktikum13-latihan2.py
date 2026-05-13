# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# Praktikum 13 - Graph III: Spanning Tree 
# ==========================================================
# ==========================================================
# Latihan 2: Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
] 
# Mengurutkan edge berdasarkan bobot terkecil 
edges.sort() 

mst = [] # List Kosong untuk menyimpan edge yang termasuk dalam MST
total_weight = 0 

connected = set() # Set sederhana untuk node yang sudah dipilih

for weight, u, v in edges: 
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected: 

        mst.append((u, v, weight)) # Tambahkan edge ke MST dan perbarui total bobot
        total_weight += weight 

        connected.add(u) # Tandai node sebagai terhubung
        connected.add(v) 

print("Minimum Spanning Tree:") 

for edge in mst: 
    print(edge) 

print("Total bobot =", total_weight) 

# =========================================================
# Jawaban Analisis: 
# 1. Edge mana yang dipilih pertama kali? 
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
# 3. Berapa total bobot MST yang dihasilkan? 
# 4. Mengapa edge tertentu tidak dipilih?
# =========================================================
# Jawaban :
# 1. Edge yang dipilih pertama kali adalah edge dengan bobot terkecil, yaitu (1, 'C', 'D').
# 2. Edge dengan bobot paling kecil dipilih lebih dahulu untuk meminimalkan total bobot MST.
# 3. Total bobot MST yang dihasilkan adalah 6.
# 4. Edge tertentu tidak dipilih karena jika dipilih, edge tersebut akan membentuk cycle dalam MST.