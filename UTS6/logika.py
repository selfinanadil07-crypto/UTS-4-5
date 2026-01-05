def menentukan_label_nadil(nilai):
    """Logika Tabel 1 """
    if 85 <= nilai <= 100:
        return "A"
    elif 80 <= nilai <= 84:
        return "A-"
    elif 75 <= nilai <= 79:
        return "B+"
    elif 70 <= nilai <= 74:
        return "B"
    elif 65 <= nilai <= 69:
        return "B-"
    elif 60 <= nilai <= 64:
        return "C+"
    elif 55 <= nilai <= 59:
        return "C"
    elif 45 <= nilai <= 54:
        return "D"
    elif nilai <= 44:
        return "E"
    else:
        return None

def transformasi_grade_nadil(huruf):
    # Logika Nomor 2: Huruf ke Nilai Akademik
    h = huruf.upper()
    if h == "A":
        return 4
    elif h == "A-":
        return 3.75
    elif h == "B+":
        return 3.5
    elif h == "B":
        return 3
    elif h == "B-":
        return 2.75
    elif h == "C+":
        return 2.5
    elif h == "C":
        return 2
    elif h == "D":
        return 1
    else:
        return 0
        
def hitung_total_sks_nadil(daftar_sks):
    # Logika Nomor 3: Menjumlahkan seluruh SKS dalam list
    return sum(daftar_sks)

#4. menghitung total nilai
def konversi_nilai_ke_ipk_mahasiswa(nilai: int) -> float:
    if 85 <= nilai <= 100:
        return 4
    elif 80 <= nilai <= 84:
        return 3.75
    elif 75 <= nilai <= 79:
        return 3.5
    elif 70 <= nilai <= 74:
        return 3
    elif 65 <= nilai <= 69:
        return 2.75
    elif 60 <= nilai <= 64:
        return 2.5
    elif 55 <= nilai <= 59:
        return 2
    elif 45 <= nilai <= 54:
        return 1
    elif nilai < 45:
        return 0

def total_nilai_ipk(daftar_sks, daftar_nilai):
    total = 0
    for sks, nilai in zip(daftar_sks, daftar_nilai):
        ipk = konversi_nilai_ke_ipk_mahasiswa(nilai)
        total += ipk * sks
    return total
    
 #5.Hitung ips
def hitung_ips_mahasiswa(daftar_sks, daftar_nilai):
    total_sks = sum(daftar_sks)
    total_nilai = 0
    for sks, nilai in zip(daftar_sks, daftar_nilai):
        ipk = konversi_nilai_ke_ipk_mahasiswa(nilai)
        total_nilai += ipk * sks
    if total_sks == 0:
        return 0
    return round(total_nilai / total_sks, 2)