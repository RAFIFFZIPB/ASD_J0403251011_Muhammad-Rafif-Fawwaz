# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# Praktikum 13 - Graph III: Spanning Tree 
# ==========================================================
# ==========================================================
# Latihan 5: Tugas Mandiri: Buat Program MST dengan Kasus Baru
# Kasus 1: Jaringan Jalan Antar Kota
# ==========================================================

# Representasi weighted graph sebagai daftar edge
# Format: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor',  'Jakarta'),
    (2, 'Bogor',  'Depok'),
    (3, 'Depok',  'Jakarta'),
    (6, 'Jakarta','Bandung'),
    (4, 'Depok',  'Bandung'),
]

# Daftar semua kota (node)
nodes = {'Bogor', 'Jakarta', 'Depok', 'Bandung'}

# ---- Algoritma Kruskal ----
# Urutkan semua edge dari bobot terkecil
edges.sort()

# Union-Find: untuk mendeteksi cycle
parent = {node: node for node in nodes}

# Fungsi untuk menemukan root dari node (dengan path compression)
def find(node):
    # Cari root dari node (dengan path compression)
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

# Fungsi untuk menggabungkan dua kelompok, kembalikan False jika sudah satu kelompok
def union(a, b):
    # Gabungkan dua kelompok, kembalikan False jika sudah satu kelompok
    ra, rb = find(a), find(b)
    if ra == rb:
        return False  # Akan membentuk cycle, skip
    parent[ra] = rb
    return True

# Pilih edge satu per satu dari yang terkecil
mst_edges = []
total_bobot = 0

# Proses edge berdasarkan bobot terkecil
for bobot, kota1, kota2 in edges:
    if union(kota1, kota2):  # Ambil hanya jika tidak membentuk cycle
        mst_edges.append((kota1, kota2, bobot))
        total_bobot += bobot

# Output hasil MST
print("=== MST Jaringan Jalan Antar Kota (Algoritma Kruskal) ===")
print("\nEdge yang dipilih:")
for kota1, kota2, bobot in mst_edges:
    print(f"  {kota1} -- {kota2}  (bobot: {bobot})")

print(f"\nTotal bobot minimum: {total_bobot}")


# =========================================================
# Jawaban Analisis: 
# 1. Kasus apa yang dipilih? 
# 2. Algoritma apa yang digunakan? 
# 3. Edge mana saja yang dipilih dalam MST? 
# 4. Berapa total bobot MST? 
# 5. Mengapa edge tertentu tidak dipilih?
# =========================================================
# Jawaban :
# 1. Kasus 1: Jaringan Jalan Antar Kota. Menghubungkan Bogor, Depok,
#    Jakarta, dan Bandung dengan total jarak jalan seminimum mungkin.
#
# 2. Digunakan algoritma Kruskal. Caranya: urutkan semua edge dari bobot
#    terkecil, lalu pilih satu per satu selama tidak membentuk cycle.
#
# 3. Edge yang dipilih dalam MST:
#    - Bogor  -- Depok   (bobot: 2)
#    - Depok  -- Jakarta (bobot: 3)
#    - Depok  -- Bandung (bobot: 4)
#
# 4. Total bobot MST = 2 + 3 + 4 = 9
#
# 5. Edge yang tidak dipilih:
#    - Bogor -- Jakarta (5): tidak dipilih karena Bogor dan Jakarta sudah
#      terhubung melalui Bogor-Depok-Jakarta, mengambilnya akan membentuk cycle.
#    - Jakarta -- Bandung (6): tidak dipilih karena Jakarta dan Bandung sudah
#      terhubung via Depok, dan bobotnya lebih besar dari Depok-Bandung.
