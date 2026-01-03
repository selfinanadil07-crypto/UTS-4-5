def urai_harga(teks_input):
    return list(map(int, teks_input.split()))

def hitung_total_bayar(daftar_harga):
    return sum(daftar_harga)

def ambil_jumlah_item(daftar_harga):
    return len(daftar_harga)
