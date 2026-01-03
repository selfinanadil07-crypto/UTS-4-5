def urai_nilai_mahasiswa(nilai):
    return list(map(int, nilai.split()))

def hitung_total_nilai_mahasiswa(daftar_nilai):
    return sum(daftar_nilai)

def hitung_rata_akademik(daftar_nilai):
    return sum(daftar_nilai) / len(daftar_nilai)
