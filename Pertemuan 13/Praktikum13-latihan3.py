# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# Praktikum 13 - Graph III: Spanning Tree 
# ==========================================================
# ==========================================================
# Latihan 3: Implementasi Algoritma Prim
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
 
# Tampilkan edge yang termasuk dalam MST dan total bobotnya 
for edge in mst: 
    print(edge) 
 
print("Total bobot =", total)

# =========================================================
# Jawaban Analisis: 
# 1. Node awal apa yang digunakan? 
# 2. Edge mana yang dipilih pertama kali? 
# 3. Bagaimana Prim menentukan edge berikutnya? 
# 4. Berapa total bobot MST yang dihasilkan? 
# 5. Apa perbedaan pendekatan Prim dan Kruskal? 
# =========================================================
# Jawaban :
# 1. Node awal yang digunakan adalah 'A'.
# 2. Edge yang dipilih pertama kali adalah edge dengan bobot terkecil dari node 'A', yaitu (2, 'A', 'C').
# 3. Prim menentukan edge berikutnya dengan memilih edge dengan bobot terkecil yang menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi.
# 4. Total bobot MST yang dihasilkan adalah 6.
# 5. Perbedaan pendekatan Prim dan Kruskal adalah Prim memulai dari satu node dan menambahkan edge terkecil yang menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi, sedangkan Kruskal mengurutkan semua edge berdasarkan bobot dan menambahkan edge terkecil yang tidak membentuk cycle.