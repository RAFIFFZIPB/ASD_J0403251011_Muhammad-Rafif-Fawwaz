# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

class Node:
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None

class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, no, nama, servis):
        # Buat node baru dengan data pelanggan
        node_baru = Node(no, nama, servis)

        # Jika antrian kosong, front dan rear menunjuk ke node baru
        if self.rear is None:
            self.front = node_baru
            self.rear = node_baru
        else:
            # Sambungkan node terakhir ke node baru
            self.rear.next = node_baru
            # Pindahkan pointer rear ke node baru
            self.rear = node_baru

        print(f"Pelanggan '{nama}' berhasil ditambahkan ke antrian.")

    def dequeue(self):
        # Cek apakah antrian kosong
        if self.front is None:
            print("Antrian kosong. Tidak ada pelanggan yang dilayani.")
            return

        # Ambil data pelanggan terdepan
        dilayani = self.front
        print("\n--- Melayani Pelanggan ---")
        print(f"No Antrian : {dilayani.no}")
        print(f"Nama       : {dilayani.nama}")
        print(f"Servis     : {dilayani.servis}")
        print("Pelanggan berhasil dilayani.")

        # Geser pointer front ke node berikutnya
        self.front = self.front.next

        # Jika antrian menjadi kosong, rear juga di-reset ke None
        if self.front is None:
            self.rear = None

    def tampilkan(self):
        # Cek apakah antrian kosong
        if self.front is None:
            print("Antrian kosong.")
            return

        print("\n=== Daftar Antrian Bengkel ===")
        print(f"{'No':<10} {'Nama':<20} {'Jenis Servis':<20}")
        print("-" * 50)

        # Traversal dari front ke rear untuk menampilkan semua node
        current = self.front
        while current:
            print(f"{current.no:<10} {current.nama:<20} {current.servis:<20}")
            current = current.next

        print("-" * 50)

def main():
    q = QueueBengkel()
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama : ")
            servis = input("Servis : ")
            q.enqueue(no, nama, servis)
        elif pilih == "2":
            q.dequeue()
        elif pilih == "3":
            q.tampilkan()
        elif pilih == "4":
            print("Terima kasih telah menggunakan sistem antrian bengkel. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
