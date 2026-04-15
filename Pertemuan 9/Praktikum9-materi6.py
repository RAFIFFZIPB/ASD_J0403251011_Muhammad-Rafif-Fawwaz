# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 6 : Struktur Organisasi Perusahaan
# ==========================================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

def preorder(node):
    if node is not None:
        print(node.data, end=" ") # Menampilkan data pada node
        preorder(node.left) # Traversal ke child kiri
        preorder(node.right) # Traversal ke child kanan        

# Membuat Tree Struktur Organisasi Perusahaan
root = Node("Direktur")

# Child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.right = Node("Staff 3")

# Menjalankan Traversal Preorder untuk menampilkan struktur organisasi
print("Struktur Organisasi Perusahaan (Preorder): ")
preorder(root)

# Penjelasan :
"""
Traversal preorder adalah metode untuk mengunjungi semua node dalam sebuah pohon biner.
Urutannya adalah:
1. Kunjungi node saat ini (root)
2. Traversal ke child kiri
3. Traversal ke child kanan

Dalam contoh ini, struktur organisasi perusahaan ditampilkan menggunakan traversal preorder.
Output yang dihasilkan adalah:
Struktur Organisasi Perusahaan (Preorder): Direktur Manajer A Staff 1 Staff 2 Manajer B Staff 3
"""