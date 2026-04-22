# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Latihan 1 : Node dan Insert BST
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

# Alur Fungsi Insert : 
def insert(root, data):
    if root is None: # Jika root kosong, buat node baru
        return Node(data)

    if data < root.data: # Jika data yang akan dimasukkan lebih kecil dari data pada node saat ini
        root.left = insert(root.left, data) # Rekursif ke child kiri
    elif data > root.data: # Jika data yang akan dimasukkan lebih besar dari data pada node saat ini
        root.right = insert(root.right, data) # Rekursif ke child kanan

    return root

# Mengisi data ke dalam BST
root = None
data_list = [50, 30, 70 , 20, 40, 60, 80]

for data in data_list:
    root = insert(root, data)

# ==========================================================
# Latihan 2 : Traversal Inorder
# ==========================================================

# Alur Fungsi Traversal Inorder : Kunjungi child kiri, cetak data, kunjungi child kanan
def inorder(root):
    if root:
        inorder(root.left) # Kunjungi child kiri
        print(root.data, end=' ') # Cetak data pada node saat ini
        inorder(root.right) # Kunjungi child kanan

print("Hasil Inorder : ")
inorder(root)

# ==========================================================
# Latihan 3 : Search di BST
# ==========================================================

def search(root, key):
    if root is None: # Jika root kosong, berarti data tidak ditemukan
        return False
    
    if root.data == key: # Jika data pada node saat ini sama dengan key yang dicari
        return True

    if key < root.data: # Jika key yang dicari lebih kecil dari data pada node saat ini, cari di child kiri
        return search(root.left, key)
    else: # Jika key yang dicari lebih besar dari data pada node saat ini, cari di child kanan
        return search(root.right, key)
    
# Uji pencarian
key = 40

if search(root, key):
    print(f"\nData {key} ditemukan di dalam BST.")
else:
    print(f"\nData {key} tidak ditemukan di dalam BST.")