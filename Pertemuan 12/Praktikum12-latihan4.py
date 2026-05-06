# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================
# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
# ==========================================================

import heapq 
# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
graph = { 
'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, 
'Perpustakaan': {'Lab': 3}, 
'Kantin': {'Lab': 4, 'Aula': 7}, 
'Lab': {'Aula': 1}, 
'Aula': {} 
} 


def dijkstra(graph, start):
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """ 

    # Inisialisasi jarak minimum
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 # Jarak node awal = 0

    priority_queue = [(0, start)] 

    # Proses selama priority queue tidak kosong
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]: 
            continue 

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight # Hitung jarak ke tetangga

            if distance < distances[neighbor]: # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) # Masukkan tetangga ke priority queue dengan jarak baru

    return distances 

hasil = dijkstra(graph, 'Gerbang') 
print("Jarak terpendek dari Gerbang Kampus:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "menit")

# Pertanyaan Analisis 
# Tuliskan jawaban sebagai komentar di bagian bawah program. 
# # Jawaban Analisis: 
# # 1. Lokasi mana yang paling dekat dari Gerbang? 
# # 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula? 
# # 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan. 
# # 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?

# Jawaban Analisis:
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh 2 menit.
# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit melalui jalur Gerbang -> Kantin -> Lab -> Aula.
# 3. Tidak, jalur langsung tidak selalu menghasilkan jarak paling kecil. Dalam kasus ini, jalur langsung dari Gerbang ke Aula tidak ada, sehingga kita harus melalui jalur lain yang mungkin memiliki waktu tempuh lebih lama tetapi tetap lebih cepat daripada jalur langsung yang tidak tersedia.
# 4. Dijkstra cocok digunakan pada kasus lokasi kampus ini karena graph yang digunakan memiliki bobot positif (waktu tempuh dalam menit) dan kita ingin mencari jarak terpendek dari satu titik awal (Gerbang) ke semua titik lainnya. Dijkstra efisien untuk graph dengan bobot positif dan memberikan hasil yang akurat untuk kasus ini.