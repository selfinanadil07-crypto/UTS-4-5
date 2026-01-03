def urai_desimal(data_teks):
   
    teks_bersih = data_teks.replace(',', '.')
    return list(map(float, teks_bersih.split()))

def hitung_akumulasi(daftar_angka):
    return sum(daftar_angka)

def rapi_presisi(nilai, jumlah_koma):
  
    format_teks = "{:." + str(jumlah_koma) + "f}"
    return format_teks.format(nilai)
