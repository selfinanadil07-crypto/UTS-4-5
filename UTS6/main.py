from logika import menentukan_label_nadil, transformasi_grade_nadil, hitung_total_sks_nadil, konversi_nilai_ke_ipk_mahasiswa, total_nilai_ipk, hitung_ips_mahasiswa

def main():
   
    print("_________________NOMOR 1____________")
    try:
        skor = float(input("Masukkan Nilai: "))
        label = menentukan_label_nadil(skor)
        print(f"Label: {label}")
    except ValueError:
        print("Error: Harap masukkan angka.")

    input("\n")

    print("_________________NOMOR 2____________")
    input_huruf = input("Masukkan Huruf Nilai (A, B+, C): ")
    hasil_bobot = transformasi_grade_nadil(input_huruf)
    print(f"Nilai : {hasil_bobot}")

if __name__ == "__main__":
    main()
    
    input("\n")

    print("_________________NOMOR 3____________")
    try:
        jml = int(input("Masukkan jumlah mata kuliah: "))
        list_sks = []
        
        for i in range(1, jml + 1):
            sks = int(input(f"sks mata kuliah {i}: "))
            list_sks.append(sks)
        
        total = hitung_total_sks_nadil(list_sks)
        print(f"\nTotal SKS: {total}")
        
    except ValueError:
        print("Error: Harap masukkan angka bulat!")
        
    input("\n")
        
print("\n_____________NOMOR 4________________")


print("Jumlah Data: ", end="")
jumlah = int(input())

daftar_sks = []
daftar_nilai = []

print("=== input sks ===")
for i in range(jumlah):
    sks = int(input(f"SKS {i+1}: "))
    daftar_sks.append(sks)

print("\n=== Input Nilai Mahasiswa ===")
for i in range(jumlah):
    nilai = int(input(f"Nilai {i+1}: "))
    daftar_nilai.append(nilai)

total = total_nilai_ipk(daftar_sks, daftar_nilai)
print("\nTotal Nilai:", round(total, 2))

print("______________NOMOR 5________________")
print("Jumlah Data: ", end="")
jumlah = int(input())

daftar_sks = []
daftar_nilai = []

print("=== input sks ===")
for i in range(jumlah):
    sks = int(input(f"SKS {i+1}: "))
    daftar_sks.append(sks)

print("\n=== input Nilai Mahasiswa ===")
for i in range(jumlah):
    nilai = int(input(f"Nilai {i+1}: "))
    daftar_nilai.append(nilai)

ips = hitung_ips_mahasiswa(daftar_sks, daftar_nilai)
print("\nIPS:", ips)