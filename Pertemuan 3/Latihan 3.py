# ==========================================================
# TUGAS Pertemuan 3 - Linked List - Latihan 3
#
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        """Menambahkan elemen di akhir doubly linked list"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse ke node terakhir
        current = self.head
        while current.next:
            current = current.next
        
        # Tambahkan node baru di akhir
        current.next = new_node
        new_node.prev = current
    
    def search(self, key):
        """Mencari elemen dalam doubly linked list"""
        current = self.head
        
        while current:
            if current.data == key:
                return True
            current = current.next
        
        return False
    
    def display(self):
        """Menampilkan isi doubly linked list"""
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return ", ".join(elements)

# Program utama
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    # Input elemen
    input_data = input("Masukkan elemen ke dalam Doubly Linked List: (Contoh: 1, 2, 3, ...): ")
    elements = [int(x.strip()) for x in input_data.split(',')]
    
    # Masukkan elemen ke doubly linked list
    for element in elements:
        dll.insert(element)
    
    # Input elemen yang ingin dicari
    search_key = int(input("Masukkan elemen yang ingin dicari: "))
    
    # Cari elemen
    if dll.search(search_key):
        print(f"Elemen {search_key} ditemukan dalam Doubly Linked List.")
    else:
        print(f"Elemen {search_key} tidak ditemukan dalam Doubly Linked List.")
