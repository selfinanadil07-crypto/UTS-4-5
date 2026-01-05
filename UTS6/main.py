import os
from logika import (
    menentukan_label_nadil, 
    transformasi_grade_nadil, 
    hitung_total_sks_nadil, 
    konversi_nilai_ke_ipk_mahasiswa, 
    total_nilai_ipk, 
    hitung_ips_mahasiswa
)

def main():
    while True:
        
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("================ MENU PILIHAN ================")
        print("1. Nomor 1 (Menentukan Label)")
        print("2. Nomor 2 (Transformasi Grade)")
        print("3. Nomor 3 (Hitung Total SKS)")
        print("4. Nomor 4 (Total Nilai IPK)")
        print("5. Nomor 5 (Hitung IPS Mahasiswa)")
        print("6. Keluar")
        
        pilihan = input("Pilih nomor menu: ")

        if pilihan == "1":
            print("\n_________________NOMOR 1____________")
            try:
                skor = float(input("Masukkan Nilai: "))
                label = menentukan_label_nadil(skor)
                print(f"Label: {label}")
            except ValueError:
                print("Error: Harap masukkan angka.")

        elif pilihan == "2":
            print("\n_________________NOMOR 2____________")
            input_huruf = input("Masukkan Huruf Nilai (A, B+, C): ")
            hasil_bobot = transformasi_grade_nadil(input_huruf)
            print(f"Nilai : {hasil_bobot}")

        elif pilihan == "3":
            print("\n_________________NOMOR 3____________")
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

        elif pilihan == "4":
            print("\n_____________NOMOR 4________________")
            try:
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
            except ValueError:
                print("Error: Masukkan angka yang valid!")

        elif pilihan == "5":
            print("\n______________NOMOR 5________________")
            try:
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
            except ValueError:
                print("Error: Masukkan angka yang valid!")

        elif pilihan == "6":
            print("\nKeluar dari program...")
            break
            
        else:
            print("\nPilihan tidak tersedia!")

        input("\n")

if __name__ == "__main__":
    main()
