def menentukan_kelulusan_mahasiswa(daftar_nilai, batas):
    total = sum(daftar_nilai)
    
    rata_rata = total / len(daftar_nilai)
    
    if rata_rata >= batas:
        status = "LULUS"
    else:
        status = "TIDAK LULUS"
        
    return total, rata_rata, status
