# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 2 : Studi Kasus DFS (Eksplorasi Jalur)
# ==========================================================

# Representasi graph
graph = {
 'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'D': [],
 'E': [],
 'F': []
}


def dfs(graph, node, visited):
# Fungsi : Melakukan penelusuran graph menggunakan DFS
# graph: dictionary yang menyimpan struktur graph
# node : menyimpan node yang sedang dikunjungi
# visited: set untuk menyimpan node yang sudah dikunjungi

    visited.add(node) # Tandai node saat ini sebagai sudah dikunjungi
    print(node, end=" ")

    # periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        if neighbor not in visited:  # Jika tetangga belum pernah dikunjungi
            dfs(graph, neighbor, visited) # Lakukan DFS secara rekursif ke tetangga tersebut

# Set untuk menyimpan node yang sudah dikunjungi
visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited)

# ==========================================================
# Pertanyaan Analisis
# ==========================================================
#
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
#    Jawab: DFS bekerja secara rekursif. Setiap kali menemukan tetangga yang belum
#      dikunjungi, fungsi langsung dipanggil ulang untuk tetangga tersebut sebelum
#      melanjutkan ke tetangga berikutnya. Akibatnya, DFS selalu menyelesaikan
#      satu cabang penuh sebelum berpindah ke cabang lain.
#
# 2. Apa yang terjadi jika urutan neighbor diubah?
#    Jawab: Urutan kunjungan berubah mengikuti urutan neighbor di adjacency list.
#      Contoh: jika 'A': ['C', 'B'], maka DFS akan mengunjungi C -> F terlebih
#      dahulu sebelum B -> D -> E. Semua node tetap terkunjungi, hanya urutannya
#      yang berbeda.
#
# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
#    Jawab: DFS menghasilkan urutan : A B D E C F
#      BFS menghasilkan urutan  : A B C D E F
#
#      DFS menelusuri satu cabang sampai habis baru berpindah ke cabang lain,
#      sedangkan BFS mengunjungi semua node pada level yang sama sebelum turun
#      ke level berikutnya. DFS cocok untuk eksplorasi semua jalur, BFS cocok
#      untuk mencari jalur terpendek.