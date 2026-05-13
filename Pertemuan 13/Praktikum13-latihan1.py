# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# Praktikum 13 - Graph III: Spanning Tree 
# ==========================================================
# ==========================================================
# Latihan 1: Memahami Konsep Spanning Tree
# ==========================================================

# Daftar edge graph 
edges = [ 
    ('A', 'B'), 
    ('A', 'C'), 
    ('A', 'D'), 
    ('C', 'D'), 
    ('B', 'D') 
] 
# Contoh spanning tree 
spanning_tree = [ 
    ('A', 'C'), 
    ('C', 'D'), 
    ('D', 'B') 
]
 
print("Edge pada graph:") 
for edge in edges: 
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree: 
    print(edge) 

print("\nJumlah edge graph =", len(edges)) 
print("Jumlah edge spanning tree =", len(spanning_tree))

# =========================================================
# Jawaban Analisis: 
# 1. Apa perbedaan graph awal dan spanning tree? 
# 2. Mengapa spanning tree tidak boleh memiliki cycle? 
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# =========================================================
# Jawaban :
# 1. Graph awal adalah kumpulan semua node dan edge yang ada, termasuk
#    edge yang membentuk cycle. Spanning tree adalah subgraph dari graph
#    awal yang menghubungkan semua node tanpa ada cycle, hanya mengambil
#    edge-edge yang diperlukan saja.
#
# 2. Spanning tree tidak boleh memiliki cycle karena tujuannya adalah
#    menghubungkan semua node dengan jalur paling efisien. Jika ada cycle,
#    berarti ada edge yang redundan (tidak dibutuhkan) karena node tersebut
#    sudah terhubung melalui jalur lain.
#
# 3. Jumlah edge spanning tree selalu n-1 (n = jumlah node), sedangkan
#    graph awal bisa memiliki lebih banyak edge. Ini karena spanning tree
#    hanya menyisakan edge yang benar-benar dibutuhkan untuk menghubungkan
#    semua node, membuang edge yang membentuk cycle.


