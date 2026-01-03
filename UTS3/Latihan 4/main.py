from utils import hitung_total_diskon_belanja, parse, cari_diskon_belanja

teks = input("Masukkan harga barang anda: ")
data_angka = parse(teks)

total = hitung_total_diskon_belanja(data_angka)

persen_diskon = cari_diskon_belanja(total)

potongan = total * persen_diskon
total_bayar = total - potongan

print("Total Belanja :", total)
print("Diskon        :", persen_diskon * 100, "%")
print("Potongan      :", potongan)
print("Total Bayar   :", total_bayar)
