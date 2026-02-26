# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Studi Kasus : Sistem Antrian pada Layanan Akademik
# Implementasi Queue => 
# Enqueue : Memindahkan pointer rear (menambah data di akhir antrian)
# Dequeue : Memindahkan pointer front (menghapus data paling depan)
# Front => A -> B -> Rear
# 
# ==========================================================

# 1) Mendefinisikan Node (Unit dasar dari linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim = nim    # Menyimpan NIM mahasiswa
        self.nama = nama   # Menyimpan nama mahasiswa
        self.next = None   # Pointer ke node berikutnya

# 2) Mendefinisikan Queue, terdiri dari pointer front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        # Ketika queue kosong, front dan rear akan bernilai None
        return self.front is None
    
    # Menambahkan data mahasiswa ke dalam antrian (enqueue)
    def enqueue(self, nim, nama):
        # Membuat node baru dengan data mahasiswa
        nodeBaru = Node(nim, nama)
        
        # Jika queue masih kosong, front dan rear akan menunjuk ke node baru
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # Jika queue tidak kosong, rear akan menunjuk ke node baru
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    # Menghapus data paling depan (Memberikan Layanan kepada mahasiswa yang paling depan dalam antrian)
    def dequeue(self):

        # Handle case ketika queue kosong, tidak ada mahasiswa yang dapat dilayani
        if self.is_empty():
            print("Antrian kosong, tidak ada mahasiswa yang dapat dilayani.")
            return None

        # 1) Ambil data yang paling depan (front)
        node_dilayani = self.front
        # 2) Geser front ke node berikutnya
        self.front = self.front.next
        
        # 3) Jika setelah dequeue queue menjadi kosong, rear juga harus di-set ke None
        if self.front is None:
            self.rear = None
        
        return node_dilayani # kembalikan data yang dilayani (NIM dan nama mahasiswa)
    
    # Menampilkan isi antrian
    def tampilkan(self):
        print("Daftar Antrian Mahasiswa (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. NIM: {current.nim} - {current.nama}")
            current = current.next
            no += 1

        if self.is_empty():
            print("Antrian kosong.")

# Program Utama

def main():

    q = queueAkademik() # Instansiasi objek queueAkademik

    while True:
        print("\n=== Sistem Antrian Layanan Akademik ===")
        print("1. Tambah Mahasiswa ke Antrian (Enqueue)")
        print("2. Layani Mahasiswa (Dequeue)")
        print("3. Tampilkan Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == '1':
            nim = input("Masukkan NIM mahasiswa: ").strip()
            nama = input("Masukkan nama mahasiswa: ").strip()
            q.enqueue(nim, nama)
            print(f"Mahasiswa {nama} dengan NIM {nim} telah ditambahkan ke antrian.")
        
        elif pilihan == '2':
            mahasiswa_dilayani = q.dequeue()
            if mahasiswa_dilayani is not None:
                print(f"Mahasiswa yang dilayani: {mahasiswa_dilayani.nim} - {mahasiswa_dilayani.nama}")
        
        elif pilihan == '3':
            q.tampilkan()
        
        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem antrian layanan akademik.")
            break
        
        else:
            print("Pilihan tidak valid, silakan pilih menu 1-4.")

if __name__ == "__main__":
    main()