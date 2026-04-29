# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
# ==========================================================

# Representasi graph
graph = {
 'Rumah': ['Sekolah', 'Toko'],
 'Sekolah': ['Perpustakaan'],
 'Toko': ['Pasar'],
 'Perpustakaan': [],       
 'Pasar': []                  
}

from collections import deque  # Struktur data untuk membuat antrian, kita gunakan dari library collections

def bfs(graph, start):
    # Inisialisasi set untuk melacak node yang sudah dikunjungi (mencegah pengulangan)
    visited = set()

    # Inisialisasi antrian dengan node awal
    queue = deque([start])

    # Tandai node awal sebagai sudah dikunjungi
    visited.add(start)

    # Proses selama antrian masih ada
    while queue:
        # Ambil node terdepan dari antrian (FIFO)
        node = queue.popleft()
        print(node, end=" ")  # Cetak node yang sedang dikunjungi

        # Iterasi semua tetangga dari node saat ini
        for neighbor in graph[node]:
            if neighbor not in visited:   # Hanya kunjungi node yang belum dikunjungi
                visited.add(neighbor)     # Tandai tetangga sebagai sudah dikunjungi
                queue.append(neighbor)    # Masukkan tetangga ke antrian untuk dikunjungi berikutnya

print("BFS dari Rumah:")
bfs(graph, 'Rumah')

# ==========================================================
# Pertanyaan Analisis
# ==========================================================
#
# 1. Node mana yang dikunjungi pertama?
#    Jawab : Node 'Rumah' dikunjungi pertama karena merupakan node awal (start).
#    Setelah itu, tetangganya dikunjungi secara berurutan: 'Sekolah', lalu 'Toko'
#    (sesuai urutan dalam adjacency list).
#
# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
#    Jawab: Karena cara kerja BFS itu menjelajah per level (layer by layer). 
#    Dia bakal ngecek semua lokasi yang jaraknya 1 langkah dulu sampai habis, 
#    baru lanjut ke lokasi yang jaraknya 2 langkah, begitu seterusnya. Makanya, 
#    saat BFS pertama kali nemu lokasi tujuan, itu udah dijamin rute terpendek 
#    (paling sedikit langkahnya) untuk graph tanpa bobot (unweighted graph) kayak gini.
#
# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
#    Jawab: Urutan kunjungan akan berubah mengikuti topologi atau struktur 
#    jalur yang baru. Algoritma BFS sangat bergantung pada konektivitas 
#    antar node dan urutan node tersebut saat dimasukkan ke dalam antrean 
#    (queue). Sebagai contoh, apabila posisi node 'Sekolah' diubah menjadi 
#    cabang dari node 'Pasar', maka 'Sekolah' akan dikunjungi lebih akhir 
#    karena tingkat kedalamannya (level) bertambah.
