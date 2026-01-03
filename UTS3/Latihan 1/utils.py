def cari_nilai_tertinggi_dan_terendah_mahasiswa(data):
    rata_rata = sum(data) / len(data)
    tertinggi = max(data)
    terendah = min(data)
    return rata_rata, tertinggi, terendah

def parse_list(teks_masuk):
    return list(map(int, teks_masuk.split()))
