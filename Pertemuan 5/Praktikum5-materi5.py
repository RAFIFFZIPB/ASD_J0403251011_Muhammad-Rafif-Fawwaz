# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas:
        return
    # Base case
    if len(hasil) == n:
        print(hasil)
        return
    # Pilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1)
    # Pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

biner_batas(4, 2)

# Penjelasan Kode:
# 1. Fungsi `biner_batas` bertugas mencari kombinasi biner sepanjang `n` digit.
# 2. Syarat utamanya adalah jumlah angka '1' tidak boleh lebih dari `batas`.
# 3. Kita mencoba menambahkan digit satu per satu:
#    - Kalau kita pilih '0', jumlah '1' tetap.
#    - Kalau kita pilih '1', jumlah '1' bertambah.
# 4. **Pruning (Pemangkasan)**: Jika jumlah '1' sudah melebihi batas, kita langsung berhenti di cabang itu (tidak lanjut cari).
# 5. Jika panjang digit sudah mencapai `n` (dan syarat batas '1' terpenuhi), hasilnya dicetak.