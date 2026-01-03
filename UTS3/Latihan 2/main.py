from utils import hitung_jumlah_data_nadil, parse_list

input_user = input("Masukkan angka yang anda inginkan : ")
angka = parse_list(input_user)

total = hitung_jumlah_data_nadil(angka)
print("Total nilai anda: ", total)