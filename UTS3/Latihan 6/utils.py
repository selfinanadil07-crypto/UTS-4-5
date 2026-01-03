def hitung_total_belanja(daftar_harga):
    
    return sum(daftar_harga)

def parse_list(pajak_belanja):
    
    return list(map(int, pajak_belanja.split()))