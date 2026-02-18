# ==========================================================
# Pertemuan 4
# Implementasi Dasar : Node pada Linked List
#
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================

# Membuat class Node (merupakan bagian dasar dari linked list)
class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai/data pada node
        self.next = None # pointer untuk node berikutnya, diinisialisasi dengan None

# 1) Membuat node satu per satu
NodeA = Node("A")
NodeB = Node("B")
NodeC = Node("C")

# 2) Menghubungkan node : A -> B -> C -> None
NodeA.next = NodeB # Node A menunjuk ke Node B
NodeB.next = NodeC # Node B menunjuk ke Node C

# 3) Menentukan node pertama (head) dari linked list
head = NodeA # Node A adalah head dari linked list

# 4) Traversal : Menampilkan data dari setiap node dalam linked list
current_node = head # Mulai traversal dari head
while current_node is not None: # Selama masih ada node yang bisa diakses
    print(current_node.data) # Tampilkan data dari node saat ini
    current_node = current_node.next # Pindah ke node berikutnya

#=========================================================
# Implementasi Dasar : Linked List + Insert Awal
#=========================================================
class LinkedList:
    def __init__(self):
        self.head = None # Inisialisasi head dengan None (linked list kosong)

    def insert_awal(self, data): # push dalam stack
        # 1) Membuat node baru dengan data yang diberikan
        nodeBaru = Node(data) # Panggil class Node
        # 2) Node baru merujuk ke head yang lama (node pertama saat ini)
        nodeBaru.next = self.head
        # 3) Head ping ke node baru
        self.head = nodeBaru

    def hapus_awal(self): # pop dalam stack
        data_terhapus = self.head.data # peek dalam stack
        self.head = self.head.next # Head sekarang merujuk ke node berikutnya (node kedua)
        print("Node yang terhapus:", data_terhapus) # Tampilkan data yang dihapus

    def tampilkan(self):
        current_node = self.head # Mulai traversal dari head
        while current_node is not None: # Selama masih ada node yang bisa diakses
            print(current_node.data) # Tampilkan data dari node saat ini
            current_node = current_node.next # Pindah ke node berikutnya

print("==== List Baru ====")
ll = LinkedList() # Instansiasi objek ke class LinkedList
ll.insert_awal("X") # Menambahkan node dengan data "X" di awal linked list
ll.insert_awal("Y") # Menambahkan node dengan data "Y" di awal linked list
ll.insert_awal("Z") # Menambahkan node dengan data "Z" di awal linked list
ll.tampilkan() # Menampilkan isi linked list setelah penambahan node baru
ll.hapus_awal() # Menghapus node pertama (head) dari linked list
ll.tampilkan() # Menampilkan isi linked list setelah penghapusan node pertama