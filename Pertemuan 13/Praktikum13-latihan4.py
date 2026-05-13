# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# Praktikum 13 - Graph III: Spanning Tree 
# ==========================================================
# ==========================================================
# Latihan 4: Studi Kasus: Jaringan Kabel Antar Gedung
# ==========================================================

# Representasi weighted graph sebagai adjacency list
graph = {
    'GedungA': [('GedungB', 4), ('GedungC', 2), ('GedungD', 5)],
    'GedungB': [('GedungA', 4), ('GedungD', 3)],
    'GedungC': [('GedungA', 2), ('GedungD', 1)],
    'GedungD': [('GedungB', 3), ('GedungC', 1), ('GedungA', 5)],
}

# ---- Algoritma Kruskal ----
# Langkah: urutkan semua edge dari biaya terkecil, lalu pilih edge
# yang tidak membentuk cycle sampai semua node terhubung.

# Kumpulkan semua edge (hindari duplikat)
all_edges = []
visited_edges = set()
for node, neighbors in graph.items():
    for neighbor, cost in neighbors:
        edge = tuple(sorted([node, neighbor]))
        if edge not in visited_edges:
            all_edges.append((cost, edge[0], edge[1]))
            visited_edges.add(edge)

# Urutkan edge berdasarkan biaya (terkecil dulu)
all_edges.sort()

# Union-Find: struktur data untuk mendeteksi cycle
parent = {node: node for node in graph}

# Fungsi untuk menemukan root dari node
def find(node):
    # Cari root dari node
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

# Fungsi untuk menggabungkan dua kelompok
def union(node1, node2):
    # Gabungkan dua kelompok
    root1, root2 = find(node1), find(node2)
    if root1 == root2:
        return False  # Sudah terhubung, akan membentuk cycle
    parent[root1] = root2
    return True

# Pilih edge satu per satu dari yang termurah
mst_edges = []
total_biaya = 0

# Proses edge berdasarkan biaya terkecil
for cost, u, v in all_edges:
    if union(u, v):  # Hanya ambil jika tidak membentuk cycle
        mst_edges.append((u, v, cost))
        total_biaya += cost

# Output hasil
print("=== Jaringan Kabel Biaya Minimum (Algoritma Kruskal) ===")
print("\nEdge yang dipilih:")
for u, v, cost in mst_edges:
    print(f"  {u} -- {v}  (biaya: {cost})")

print(f"\nTotal biaya minimum: {total_biaya}")

# =========================================================
# Jawaban Analisis: 
# 1. Algoritma apa yang digunakan? 
# 2. Edge mana saja yang dipilih? 
# 3. Berapa total biaya minimum? 
# 4. Mengapa MST cocok digunakan pada kasus ini?
# =========================================================
# Jawaban :
# 1. algoritma Kruskal, Cara kerjanya: urutkan semua edge dari
#    biaya terkecil, lalu pilih edge satu per satu selama tidak membentuk
#    cycle, sampai semua node terhubung.
#
# 2. Edge yang dipilih:
#    - GedungC -- GedungD (biaya: 1)
#    - GedungA -- GedungC (biaya: 2)
#    - GedungB -- GedungD (biaya: 3)
#
# 3. Total biaya minimum = 1 + 2 + 3 = 6
#
# 4. MST cocok untuk kasus ini karena tujuannya adalah menghubungkan
#    semua gedung (node) dengan total biaya kabel (edge) sekecil mungkin,
#    tanpa jalur yang berlebihan. Itulah persis yang dilakukan MST:
#    menghubungkan semua node dengan biaya total minimum dan tanpa cycle.