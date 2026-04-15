# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 4: Membuat Traversal Inorder
# ==========================================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

# Fungsi Inorder : Left -> Root -> Right
def inorder(node):
    if node is not None:
        inorder(node.left) # Traversal ke child kiri
        print(node.data, end=" ") # Menampilkan data pada node
        inorder(node.right) # Traversal ke child kanan

# Membuat Node Root
root = Node("A") # Membuat node root dengan data "A"

# Membuat Child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan hasil Traversal Inorder
print("Hasil Traversal Inorder : ")
inorder(root) # Output: D B E A C

# Penjelasan :
"""
Traversal inorder adalah metode untuk mengunjungi semua node dalam sebuah pohon biner.
Urutannya adalah:
1. Traversal ke child kiri
2. Kunjungi node saat ini (root)
3. Traversal ke child kanan
Dalam contoh ini, hasil traversal inorder adalah D B E A C, karena kita mengunjungi child kiri "D" dulu, lalu ke root "B", terus ke child kanan "E", lalu ke root "A", dan terakhir ke child kanan "C".
"""