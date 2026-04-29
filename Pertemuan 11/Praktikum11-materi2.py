# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Materi 2 : Implementasi BFS
# ==========================================================

# Struktur data untuk membuat antrian, kita gunakan dari library collections
from collections import deque

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

def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran graph menggunakan BFS
    # graph: dictionary yang menyimpan struktur graph
    # start: node awal untuk memulai Penelusuran/BFS

    # Queue digunakan untuk menyimpan node yang akan dikunjungi berikutnya
    queue = deque()

    # Variabel yang digunakan untuk menyimpan node yang sudah dikunjungi
    visited = set()

    # Masukkan node awal ke dalam queue
    queue.append(start)

    # Tandai node awal sebagai sudah dikunjungi
    visited.add(start)

    print("Urutan BFS:")

    # Selama queue tidak kosong, proses terus berjalan
    while queue:
        # Ambil node paling depan dari queue
        node = queue.popleft()
        print(node, end=' ') # Cetak node yang sedang dikunjungi

        # Kunjungi semua tetangga dari node saat ini
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Jika tetangga belum dikunjungi, tambahkan ke queue dan tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                queue.append(neighbor)
            
# Menjalankan BFS dari node A
bfs(graph, 'A')