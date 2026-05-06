# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Materi 1 : Implementasi Dijkstra
# ==========================================================

# heapq : modul untuk membuat priority queue
import heapq

# Representasi graph dengan bobot (weighted graph)
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
}

# Fungsi : Dijkstra untuk mencari jarak terpendek dari node awal ke semua node lainnya
def dijkstra(graph, start): 
    # Menyimpan jarak minimum 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak node awal = 0 
    distances[start] = 0 
 
    # Priority queue 
    pq = [(0, start)] 

    # Proses selama priority queue tidak kosong
    while pq: 
        current_distance, current_node = heapq.heappop(pq) 
 
        # Periksa semua tetangga 
        for neighbor, weight in graph[current_node].items(): 
 
            distance = current_distance + weight 
 
            # Jika ditemukan jarak lebih kecil 
            if distance < distances[neighbor]: 
 
                distances[neighbor] = distance # Update jarak minimum
 
                heapq.heappush(pq, (distance, neighbor)) # Masukkan tetangga ke priority queue dengan jarak baru
 
    return distances 
 
hasil = dijkstra(graph, 'A') 
print(hasil)