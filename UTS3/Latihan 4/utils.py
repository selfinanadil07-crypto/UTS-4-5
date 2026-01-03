def hitung_total_diskon_belanja(data):
    return sum(data)

def parse(data_str):
    return [int(angka) for angka in data_str.split()]

def cari_diskon_belanja(total_belanja):
   
    if total_belanja > 50000: 
        return 0.1
    else:
        return 0.0