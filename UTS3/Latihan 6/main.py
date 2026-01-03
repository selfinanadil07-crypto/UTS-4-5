from utils import hitung_total_belanja, parse_list

input_user = input("Masukkan harga barang-barang : ")

daftar_harga = parse_list(input_user)
total_awal = hitung_total_belanja(daftar_harga)

pajak = 0.1
nominal_pajak = total_awal * pajak
total_akhir = total_awal + nominal_pajak


print(f"Jumlah Barang : {len(daftar_harga)}")
print(f"Total Awal    : {total_awal}")
print(f"Pajak (10%)   : {nominal_pajak}")
print(f"Total Bayar   : {total_akhir}")
