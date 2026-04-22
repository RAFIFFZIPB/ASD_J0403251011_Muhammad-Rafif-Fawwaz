# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 4 : Rotasi Kanan pada BST Tidak Seimbang
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

# Fungsi rotasi kanan
# Alur Fungsi Rotate Right : Simpan child kiri sebagai y, simpan subtree kanan y sebagai T2, lakukan rotasi dengan menjadikan x child kanan dari y dan T2 child kiri dari x, kembalikan y sebagai root baru
def rotate_right(x):
    # x adalah root lama
    y = x.left  # y adalah child kiri x
    T2 = y.right # subtree kanan milik y disimpan sementara

    # Proses rotasi
    y.right = x # x menjadi child kanan dari y
    x.left = T2 # child kiri x diganti dengan T2

    # y menjadi root baru
    return y

# -----------------------------
# Program utama
# -----------------------------

# Membuat tree yang tidak seimbang:
# 30 -> 20 -> 10
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

# Melakukan rotasi kanan pada root
root = rotate_right(root)

print("\nPreorder sesudah rotasi kanan:")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)
