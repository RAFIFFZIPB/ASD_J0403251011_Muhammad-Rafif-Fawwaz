# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Materi 3 : Implementasi DFS
# ==========================================================


# Repesentasi graph
graph ={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dfs(graph, node, visited):
# Fungsi untuk melakukan penelusuran graph menggunakan DFS
# graph: dictionary yang menyimpan struktur graph
# node : menyimpan node yang sedang dikunjungi
# visited: set untuk menyimpan node yang sudah dikunjungi

# Tandai node saat ini sebagai sudah dikunjungi
    visited.add(node)
    print(node, end=' ') # Cetak node yang sedang dikunjungi

# periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:

        # Jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            dfs(graph, neighbor, visited) # Lakukan DFS secara rekursif ke tetangga tersebut

visited = set() # Set untuk menyimpan node yang sudah dikunjungi  

# Menjalankan dfs dari Node A
dfs(graph, 'A', visited)
