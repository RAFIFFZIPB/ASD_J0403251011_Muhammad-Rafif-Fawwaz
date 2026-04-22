# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 5 : Rotasi Kiri pada BST Tidak Seimbang
# ==========================================================

# Class Node
class Node:
    def __init__(self, data):
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan

# Fungsi preorder untuk melihat isi tree
# Alur Fungsi Preorder : Cetak data, kunjungi child kiri, kunjungi child kanan
def preorder(root):
    # Jika root tidak kosong, cetak data dan kunjungi child kiri dan kanan
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi untuk menampilkan struktur tree
# Alur Fungsi Tampil Struktur : Cetak posisi dan data, kunjungi child kiri, kunjungi child kanan
def tampil_struktur(root, level=0, posisi="Root"):
    # Jika root tidak kosong, cetak posisi dan data, lalu kunjungi child kiri dan kanan dengan level yang meningkat
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# Fungsi rotasi kiri
# Alur Fungsi Rotate Left : Simpan child kanan sebagai y, simpan subtree kiri y sebagai T2, lakukan rotasi dengan menjadikan x child kiri dari y dan T2 child kanan dari x, kembalikan y sebagai root baru
def rotate_left(x):
    # x adalah root lama
    y = x.right # y adalah child kanan x
    T2 = y.left # subtree kiri milik y disimpan sementara

    # Proses rotasi
    y.left = x # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2

    # y menjadi root baru
    return y

# -----------------------------
# Program utama
# -----------------------------

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri:")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)
