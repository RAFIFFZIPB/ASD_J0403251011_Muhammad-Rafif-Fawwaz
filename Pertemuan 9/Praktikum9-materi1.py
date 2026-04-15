# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 1 : Membuat Node
# ==========================================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

# Membuat Root
root = Node("A") # Membuat node root dengan data "A"

# Menampilkan isi node root
print("Data pada root : ", root.data) # Output: A
print("Data Child kiri root : ", root.left) # Output: None
print("Data Child kanan root : ", root.right) # Output: None


# Pembahasan :
# Pada kode di atas, kita membuat sebuah class Node yang memiliki atribut data, left, dan right.
# Atribut data digunakan untuk menyimpan nilai pada node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan kanan dari node tersebut. 
# Pada contoh penggunaan, kita membuat sebuah node root dengan data "A" dan menampilkan isi dari node tersebut.