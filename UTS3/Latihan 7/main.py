from utils import urai_desimal, hitung_akumulasi, rapi_presisi

teks = input("Masukkan angka desimal yang anda inginkan: ")
koma = int(input("Mau berapa jumlah angka di belakang koma? "))

list_angka = urai_desimal(teks)
total_asli = hitung_akumulasi(list_angka)
hasil_akhir = rapi_presisi(total_asli, koma)

print("Total semua angka:", total_asli)
print("Hasil :", hasil_akhir)
