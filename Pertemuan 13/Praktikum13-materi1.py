# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Materi 1 : Implementasi Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
]

# Mengurutkan edge berdasarkan bobot 
edges.sort() 
 
mst = [] # List Kosong untuk menyimpan edge yang termasuk dalam MST
total_weight = 0 # Variabel untuk menyimpan total bobot MST
 
# Set sederhana untuk node yang sudah dipilih 
connected = set() 
 
for weight, u, v in edges: 
 
    # Jika edge tidak membentuk cycle sederhana 
    if u not in connected or v not in connected: 
 
        # Tambahkan edge ke MST dan perbarui total bobot
        mst.append((u, v, weight)) 
        total_weight += weight 
 
        # Tandai node sebagai terhubung
        connected.add(u) 
        connected.add(v) 
 
print("Minimum Spanning Tree:") 
 
for edge in mst: 
    print(edge) 
 
print("Total bobot =", total_weight)