# ==========================================================
# TUGAS Pertemuan 3 - Linked List - Latihan 1
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
    
    def delete_node(self, key):
        """Menghapus node dengan nilai tertentu"""
        temp = self.head
        
        # Jika head yang akan dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        
        # Cari node yang akan dihapus
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        # Jika key tidak ditemukan
        if temp is None:
            return
        
        # Hapus node
        prev.next = temp.next
        temp = None
    
    def display(self):
        """Menampilkan isi linked list"""
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return " -> ".join(elements) if elements else "List kosong"

# Program utama
if __name__ == "__main__":
    ll = LinkedList()
    
    # Elemen linked list yang sudah disediakan
    elements = [5, 10, 15, 20, 25]
    
    # Masukkan elemen ke linked list
    for element in elements:
        ll.insert(element)
    
    print(f"\nLinked List sebelum penghapusan: {ll.display()}")
    
    # Input elemen yang ingin dihapus
    delete_key = int(input("\nMasukkan elemen yang ingin dihapus: "))
    
    # Hapus elemen
    ll.delete_node(delete_key)
    
    print(f"Linked List setelah penghapusan: {ll.display()}")
