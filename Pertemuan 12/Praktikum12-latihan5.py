# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================
# ==========================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path
# Algoritma: Dijkstra - Jalur Terpendek Antar Kota
# ==========================================================

import heapq

# 1. Representasi graph berbobot menggunakan dictionary
# Setiap kunci adalah kota asal, nilainya adalah dictionary
# berisi kota tujuan beserta bobot (jarak/waktu tempuh)
graph = {
    'Bogor':   {'Jakarta': 5, 'Depok': 2},
    'Depok':   {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra untuk mencari jarak terpendek
def dijkstra(graph, start):
    # Inisialisasi semua jarak dengan tak hingga, kecuali node awal
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue: (jarak_saat_ini, node)
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika sudah ditemukan jarak yang lebih pendek sebelumnya
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Perbarui jarak jika ditemukan jalur yang lebih pendek
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 3. Penentuan node awal
start_node = 'Bogor'

# 4. Jalankan algoritma Dijkstra dan tampilkan hasil
hasil = dijkstra(graph, start_node)

print(f"Jarak terpendek dari {start_node} ke semua kota:")
print("-" * 35)
for kota, jarak in hasil.items():
    if kota != start_node:
        print(f"  {start_node} -> {kota:10} = {jarak} km")

