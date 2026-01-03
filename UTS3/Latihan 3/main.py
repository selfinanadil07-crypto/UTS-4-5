from utils import menentukan_kelulusan_mahasiswa

input_user = input("Masukkan data nilai: ")
batas_nilai = input("Masukkan batas kelulusan: ")

list_nilai = list(map(int, input_user.split()))
batas_angka = int(batas_nilai)

hasil = menentukan_kelulusan_mahasiswa(list_nilai, batas_angka)

print("Total Nilai Keseluruhan  :", hasil[0])
print("Nilai Rata-rata  :", hasil[1])
print("Hasil    :", hasil[2])