# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Materi 2 : Implementasi Bellman-Ford
# ==========================================================

# Representasi graph dengan bobot (weighted graph)
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
}

# Fungsi : Bellman-Ford untuk mencari jarak terpendek dari node awal ke semua node lainnya
def bellman_ford(graph, start): 
 
    # Inisialisasi jarak minimum
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0  # Jarak node awal = 0
 
    # Relaksasi berulang 
    for _ in range(len(graph) - 1): 
 
        # Periksa semua edge
        for node in graph: 
 
            for neighbor, weight in graph[node].items(): # Periksa semua tetangga dari node saat ini
 
                if distances[node] + weight < distances[neighbor]: # Jika ditemukan jarak lebih kecil
 
                    distances[neighbor] = distances[node] + weight # Update jarak minimum
 
    return distances

hasil = bellman_ford(graph, 'A') 
print(hasil)