from kumpulan_fungsi_bangun_datar import layang_layang, segitiga, persegi, jajar_genjang, belah_ketupat, trapesium, heksagon, lingkaran, persegi_panjang, pentagon
import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print(" 1. Layang-layang")
    print(" 2. Segitiga")
    print(" 3. Persegi")
    print(" 4. Jajar Genjang")
    print(" 5. Belah Ketupat")
    print(" 6. Trapesium")
    print(" 7. Heksagon (Segi-6)")
    print(" 8. Lingkaran")
    print(" 9. Persegi Panjang")
    print("10. Pentagon (Segi-5)")
    print("11. Keluar")

while True:
    bersihkan_layar()
    menu()
    pilihan = input("Pilih menu (1-11): ")

    if pilihan == '1':
        d1 = float(input("Masukkan Diagonal 1: "))
        d2 = float(input("Masukkan Diagonal 2: "))
        s1 = float(input("Masukkan Sisi 1: "))
        s2 = float(input("Masukkan Sisi 2: "))
        kel, luas = layang_layang(d1, d2, s1, s2)
        
        print(f"Keliling: {kel}")
        print(f"Luas: {luas}")

    elif pilihan == '2':
        a = float(input("Masukkan Alas: "))
        t = float(input("Masukkan Tinggi: "))
        s1 = float(input("Masukkan Sisi 1: "))
        s2 = float(input("Masukkan Sisi 2: "))
        s3 = float(input("Masukkan Sisi 3: "))
        kel, luas = segitiga(a, t, s1, s2, s3)
        
        print(f"Keliling: {kel}")
        print(f"Luas: {luas}")

    elif pilihan == '3':
        s = float(input("Masukkan Sisi: "))
        kel, luas = persegi(s)
        
        print(f"Keliling: {kel}")
        print(f"Luas: {luas}")

    elif pilihan == '4':
        a = float(input("Masukkan Alas: "))
        t = float(input("Masukkan Tinggi: "))
        sm = float(input("Masukkan Sisi Miring: "))
        kel, luas = jajar_genjang(a, t, sm)
        
        print(f"Keliling: {kel}")
        print(f"Luas: {luas}")

    elif pilihan == '5':
        s = float(input("Masukkan Sisi: "))
        d1 = float(input("Masukkan Diagonal 1: "))
        d2 = float(input("Masukkan Diagonal 2: "))
        kel, luas = belah_ketupat(s, d1, d2)
        
        print(f"Keliling: {kel}")
        print(f"Luas: {luas}")

    elif pilihan == '6':
        a = float(input("Masukkan Sisi Atas: "))
        b = float(input("Masukkan Sisi Bawah: "))
        c = float(input("Masukkan Sisi Samping 1: "))
        d = float(input("Masukkan Sisi Samping 2: "))
        t = float(input("Masukkan Tinggi: "))
        kel, luas = trapesium(a, b, c, d, t)
        
        print(f"Keliling: {kel}")
        print(f"Luas: {luas}")

    elif pilihan == '7':
        s = float(input("Masukkan Sisi: "))
        kel, luas = heksagon(s)
        
        print(f"Keliling: {kel}")
        print(f"Luas: {luas}")

    elif pilihan == '8':
        r = float(input("Masukkan Jari-jari: "))
        kel, luas = lingkaran(r)
        
        print(f"Keliling: {kel}")
        print(f"Luas: {luas}")

    elif pilihan == '9':
        p = float(input("Masukkan Panjang: "))
        l = float(input("Masukkan Lebar: "))
        kel, luas = persegi_panjang(p, l)
        
        print(f"Keliling: {kel}")
        print(f"Luas: {luas}")

    elif pilihan == '10':
        s = float(input("Masukkan Sisi: "))
        kel, luas = pentagon(s)
        
        print(f"Keliling: {kel}")
        print(f"Luas: {luas}")

    elif pilihan == '11':
        print("\nTERIMA KASIHHHHH!!")
        break
    
    else:
        print("\nPilihan tidak valid! Silakan pilih nomor 1 sampai 11.")

    input("\n")