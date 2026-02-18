# ==========================================================
# TUGAS Pertemuan 3 - Linked List - Latihan 5
#
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        """Menambahkan elemen di akhir linked list"""
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
    
    def reverse(self):
        """Membalik linked list tanpa membuat linked list baru"""
        prev = None
        current = self.head
        
        while current:
            # Simpan node berikutnya
            next_node = current.next
            
            # Balik pointer
            current.next = prev
            
            # Geser pointer
            prev = current
            current = next_node
        
        # Update head ke node terakhir (sekarang jadi node pertama)
        self.head = prev
    
    def display(self):
        """Menampilkan isi linked list"""
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        result = " -> ".join(elements)
        return result + " -> null" if elements else "null"

# Program utama
if __name__ == "__main__":
    ll = LinkedList()
    
    # Input elemen
    input_data = input("Masukkan elemen untuk Linked List: (Contoh : 1, 2, 3, ...): ")
    elements = [int(x.strip()) for x in input_data.split(',')]
    
    # Masukkan elemen ke linked list
    for element in elements:
        ll.insert(element)
    
    # Tampilkan linked list sebelum dibalik
    print(f"Linked List sebelum dibalik: {ll.display()}")
    
    # Balik linked list
    ll.reverse()
    
    # Tampilkan linked list setelah dibalik
    print(f"Linked List setelah dibalik: {ll.display()}")
