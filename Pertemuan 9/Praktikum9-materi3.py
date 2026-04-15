# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 3: Membuat Traversal Preorder
# ==========================================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

# Fungsi Preorder : Root -> Left -> Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ") # Menampilkan data pada node
        preorder(node.left) # Traversal ke child kiri
        preorder(node.right) # Traversal ke child kanan

# Membuat Node Root
root = Node("A") # Membuat node root dengan data "A"

# Membuat Child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan hasil Traversal Preorder
print("Hasil Traversal Preorder : ")
preorder(root) # Output: A B D E C

# Penjelasan :
"""
Traversal preorder adalah metode untuk mengunjungi semua node dalam sebuah pohon biner.
Urutannya adalah:
1. Kunjungi node saat ini (root)
2. Traversal ke child kiri
3. Traversal ke child kanan
Dalam contoh ini, hasil traversal preorder adalah A B D E C, karena kita mengunjungi root "A" dulu, lalu ke child kiri "B", terus ke child kiri "D", lalu ke child kanan "E", dan terakhir ke child kanan "C".
"""