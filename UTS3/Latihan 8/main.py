
from utils import urai_harga, hitung_total_bayar, ambil_jumlah_item

jumlah_konsumen = int(input("Berapa jumlah konsumen: "))

data_pembayaran = []

for i in range(1, jumlah_konsumen + 1):
    teks = input("Masukkan jumlah harga barang Konsumen " + str(i) + ": ")
    
    list_harga = urai_harga(teks)
    total = hitung_total_bayar(list_harga)
    
    data_pembayaran.append(total)

for i in range(1, jumlah_konsumen + 1):
    print("Total yang di bayarkan konsumen " + str(i) + ": ", data_pembayaran[i-1])
