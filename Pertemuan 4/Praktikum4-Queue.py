# ==========================================================
# Pertemuan 4
# Implementasi Dasar : Queue berbasis Linked List
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

# queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        # mengecek apakah queue kosong
        return self.front is None

    def enqueue(self, data):
        # menambah data di akhir queue (rear)
        nodeBaru = Node(data)
        
        # jika queue masih kosong, front dan rear akan menunjuk ke node baru
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # jika queue tidak kosong, rear akan menunjuk ke node baru

        self.rear.next = nodeBaru # rear menunjuk ke node baru
        self.rear = nodeBaru # rear sekarang menjadi node baru

    def dequeue(self):   
        # 1) Ambil data yang paling depan (front)
        data_terhapus = self.front.data
        # 2) Geser front ke node berikutnya
        self.front = self.front.next
        
        # 3) Jika setelah dequeue queue menjadi kosong, rear juga harus di-set ke None
        if self.front is None:
            self.rear = None
        
        return data_terhapus # kembalikan data yang dihapus

    def tampilkan(self):
        current_node = self.front # Mulai traversal dari front
        print("Front->", end="")
        while current_node is not None: # Selama masih ada node yang bisa diakses
            print(current_node.data, end="->") # Tampilkan data dari node saat ini
            current_node = current_node.next # Pindah ke node berikutnya
        print("none <- Rear di node terakhir")


# Instantiasi objek class QueueLL
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()