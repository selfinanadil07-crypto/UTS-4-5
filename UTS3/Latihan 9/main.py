from utils import urai_nilai_mahasiswa, hitung_rata_akademik

jumlah_mhs = int(input("Masukkan Jumlah Mahasiswa: "))

hasil_akhir = []

for i in range(1, jumlah_mhs + 1):
    data_teks = input("Masukkan Nilai Mahasiswa " + str(i) + ": ")
    
    list_nilai = urai_nilai_mahasiswa(data_teks)
    rata = hitung_rata_akademik(list_nilai)
    hasil_akhir.append(rata)

for i in range(1, jumlah_mhs + 1):
    print("Rata - Rata Nilai Mahasiswa " + str(i) + ": ", hasil_akhir[i-1])