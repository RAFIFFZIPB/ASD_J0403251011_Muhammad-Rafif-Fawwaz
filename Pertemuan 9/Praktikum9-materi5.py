# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 5: Membuat Traversal Postorder
# ==========================================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

# Fungsi Postorder : Left -> Right -> Root
def postorder(node):
    if node is not None:
        postorder(node.left) # Traversal ke child kiri
        postorder(node.right) # Traversal ke child kanan
        print(node.data, end=" ") # Menampilkan data pada node

# Membuat Node Root
root = Node("A") # Membuat node root dengan data "A"

# Membuat Child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan hasil Traversal Postorder
print("Hasil Traversal Postorder : ")
postorder(root) # Output: D E B C A

# Penjelasan :
"""
Traversal postorder adalah metode untuk mengunjungi semua node dalam sebuah pohon biner.
Urutannya adalah:
1. Traversal ke child kiri
2. Traversal ke child kanan
3. Kunjungi node saat ini (root)
Dalam contoh ini, hasil traversal postorder adalah D E B C A, karena kita mengunjungi child kiri "D" dulu, lalu ke child kanan "E", terus ke root "B", lalu ke child kanan "C", dan terakhir ke root "A".
"""