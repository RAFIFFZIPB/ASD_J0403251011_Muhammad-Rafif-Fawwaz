# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Materi 2 : Implementasi Prim
# ==========================================================

# Library untuk priority queue
import heapq 

# Representasi graph menggunakan dictionary bersarang
graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 
 

# Fungsi : Prim untuk mencari Minimum Spanning Tree (MST)
# Graph harus dalam bentuk dictionary bersarang dengan bobot sebagai nilai
# Start adalah node awal untuk memulai MST 
def prim(graph, start): 
 
    visited = set([start]) 
 
    edges = [] 
 
    # Masukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
 
    mst = [] 
    total_weight = 0 
 
    while edges: # Selama masih ada edge yang bisa diproses
 
        weight, u, v = heapq.heappop(edges) # Ambil edge dengan bobot terkecil
 
        # Jika node tujuan belum dikunjungi, tambahkan edge ke MST
        if v not in visited: 
 
            visited.add(v) 
 
            # Tambahkan edge ke MST dan perbarui total bobot
            mst.append((u, v, weight)) 
            total_weight += weight 
 
            for neighbor, w in graph[v].items(): # Masukkan edge dari node baru ke priority queue
 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
 
    return mst, total_weight 
 
 
mst, total = prim(graph, 'A') 
 
print("Minimum Spanning Tree:") 
 
for edge in mst: 
    print(edge) 
 
print("Total bobot =", total)