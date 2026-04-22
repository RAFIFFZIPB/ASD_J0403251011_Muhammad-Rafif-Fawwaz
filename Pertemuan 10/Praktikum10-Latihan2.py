# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 4 : Membuat BST Yang Tidak Seimbang
# ==========================================================

# Class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan

# Fungsi insert untuk BST
# Alur Fungsi Insert : Jika root kosong, buat node baru. Jika data lebih kecil, masuk ke subtree kiri. Jika data lebih besar, masuk ke subtree kanan.
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data)
    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

# Fungsi preorder untuk melihat bentuk tree
# Alur Fungsi Preorder : Cetak data, kunjungi child kiri, kunjungi child kanan
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi sederhana untuk menampilkan struktur tree
# Alur Fungsi Tampil Struktur : Cetak posisi dan data, kunjungi child kiri, kunjungi child kanan
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# -----------------------------
# Program utama
# -----------------------------
root = None

# Data dimasukkan berurutan naik
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)

print("\n\nStruktur BST:")
tampil_struktur(root)


# Pembahasan :
# 1. Mengapa Tree Condong ke Kanan?
# Karena data dimasukkan dalam urutan naik (10, 20, 30), setiap nilai baru lebih besar dari nilai sebelumnya, sehingga selalu masuk ke child kanan.
# 2. Mengapa Semakin Panjang Tree, Pencarian Semakin Lambat?
# Karena Tree menjadi tidak seimbang, dengan semua node berada di satu sisi (kanan), sehingga pencarian harus melewati semua node untuk menemukan nilai tertentu, yang menyebabkan waktu pencarian menjadi O(n) dalam kasus terburuk.
# 3. Mengapa BST Tidak selalu seimbang?
# Karena struktur BST sangat bergantung pada urutan data yang dimasukkan. Jika data dimasukkan dalam urutan yang sudah terurut (naik atau turun), maka BST akan menjadi tidak seimbang. Untuk menjaga keseimbangan, diperlukan algoritma khusus seperti AVL.