# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 2 : Membuat Node Tree
# ==========================================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

# Membuat Node Root
root = Node("A") # Membuat node root dengan data "A"

# Membuat Child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi node root dan childnya
print("Data pada root : ", root.data) # Output: A
print("Data Child kiri root : ", root.left.data) # Output: B
print("Data Child kanan root : ", root.right.data) # Output: C
print("Data Child kiri dari B : ", root.left.left.data) # Output: D
print("Data Child kanan dari B : ", root.left.right.data) # Output: E

# Penjelasan :
"""
Tree itu seperti pohon terbalik, ada satu node paling atas yang disebut root, terus bercabang ke bawah.
Tiap node bisa punya dua anak, yaitu child kiri dan child kanan.
Di sini kita bikin tree sederhana dengan root "A", terus "A" punya anak "B" dan "C", lalu "B" punya anak "D" dan "E".
Cara aksesnya tinggal ikutin jalurnya, misal root.left.right bakal ngasih kita node "E".
"""