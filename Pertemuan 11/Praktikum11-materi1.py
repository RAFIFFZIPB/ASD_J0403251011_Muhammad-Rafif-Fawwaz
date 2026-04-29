# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Materi 1 : Implementasi Graph 
# ==========================================================

# Representasi Graph
graph = {
    'A':['B', 'C'],
    'B':['A', 'D'],
    'C':['A', 'D'],
    'D':['B', 'C'],
}

# Menampilkan graph
for node in graph:
    print(node, '->', graph[node])