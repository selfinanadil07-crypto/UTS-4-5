from utils import cari_nilai_tertinggi_dan_terendah_mahasiswa, parse_list

input_mentah = input("Masukkan daftar nilai mahasiswa: ")
daftar_nilai = parse_list(input_mentah)

rerata, nilai_max, nilai_min = cari_nilai_tertinggi_dan_terendah_mahasiswa(daftar_nilai)

print("Rata-rata Nilai :", rerata)
print("Nilai Tertinggi :", nilai_max)
print("Nilai Terendah  :", nilai_min)