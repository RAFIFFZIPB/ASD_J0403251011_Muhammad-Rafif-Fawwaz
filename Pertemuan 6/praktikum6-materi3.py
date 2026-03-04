# ==========================================================
# Nama : Muhammad Rafif Fawwaz
# NIM : J0403251011
# Kelas : TPL B1
# ==========================================================
# ==========================================================
# Materi 3 : Merge Sort (Ascending)
# ==========================================================

def merge_sort(data):

    if len(data) <= 1: # Base case : jika data hanya memiliki 1 elemen atau kosong, maka sudah terurut
        return data
    
    # Divide : membuat data menjadi 2 bagian
    mid = len(data) // 2
    left_half = data[:mid] # Slicing bagian kiri
    right_half = data[mid:] # Slicing bagian kanan

    # Recursive call : memanggil fungsi merge_sort secara rekursif untuk bagian kiri dan kanan
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge : menggabungkan data yang sudah diurutkan
    return merge(left_sorted, right_sorted)


def merge(left_half, right_half):
    
    result = [] # List untuk menyimpan hasil penggabungan
    i = j = 0

    # Membandingkan elemen kiri dan kanan
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    # Menambahkan sisa data dari left_half atau right_half
    result.extend(left_half[i:])
    result.extend(right_half[j:])

    return result

# Contoh penggunaan
data = [13, 7, 28, 5, 19, 36, 4]
print ("Hasil Sorting : ", merge_sort(data))