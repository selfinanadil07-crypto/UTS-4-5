from kumpulan_fungsi_bangun_ruang_nadil import limas_segitiga, prisma_pentagon, limas_segi_empat, prisma_segi_empat, kubus, tabung, kerucut, balok, prisma_segitiga, bola
import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print(" 1. Limas Segitiga")
    print(" 2. Prisma Pentagon (Segi-5)")
    print(" 3. Limas Segi Empat")
    print(" 4. Prisma Segi Empat")
    print(" 5. Kubus")
    print(" 6. Tabung")
    print(" 7. Kerucut")
    print(" 8. Balok")
    print(" 9. Prisma Segitiga")
    print("10. Bola")
    print("11. Keluar")

while True:
    bersihkan_layar()
    menu()
    pilihan = input("Pilih menu (1-11): ")

    if pilihan == '1':
        la = float(input("Masukkan Luas Alas : "))
        lst = float(input("Masukkan Luas Sisi Tegak : "))
        t = float(input("Masukkan Tinggi : "))
        lp, vol = limas_segitiga(la, lst, t)
        
        print(f"Luas Permukaan: {lp}")
        print(f"Volume: {vol}")

    elif pilihan == '2':
        la = float(input("Masukkan Luas Alas : "))
        ka = float(input("Masukkan Keliling Alas : "))
        t = float(input("Masukkan Tinggi : "))
        lp, vol = prisma_pentagon(la, ka, t)
        
        print(f"Luas Permukaan: {lp}")
        print(f"Volume: {vol}")

    elif pilihan == '3':
        la = float(input("Masukkan Luas Alas : "))
        lst = float(input("Masukkan Luas Sisi Tegak : "))
        t = float(input("Masukkan Tinggi : "))
        lp, vol = limas_segi_empat(la, lst, t)
        
        print(f"Luas Permukaan: {lp}")
        print(f"Volume: {vol}")

    elif pilihan == '4':
        la = float(input("Masukkan Luas Alas : "))
        ka = float(input("Masukkan Keliling Alas : "))
        t = float(input("Masukkan Tinggi : "))
        lp, vol = prisma_segi_empat(la, ka, t)
        
        print(f"Luas Permukaan: {lp}")
        print(f"Volume: {vol}")

    elif pilihan == '5':
        s = float(input("Masukkan Sisi : "))
        lp, vol = kubus(s)
        
        print(f"Luas Permukaan: {lp}")
        print(f"Volume: {vol}")

    elif pilihan == '6':
        r = float(input("Masukkan Jari-jari : "))
        t = float(input("Masukkan Tinggi : "))
        lp, vol = tabung(r, t)
        
        print(f"Luas Permukaan: {lp}")
        print(f"Volume: {vol}")

    elif pilihan == '7':
        r = float(input("Masukkan Jari-jari : "))
        t = float(input("Masukkan Tinggi : "))
        s = float(input("Masukkan Garis Pelukis : "))
        lp, vol = kerucut(r, t, s)
        
        print(f"Luas Permukaan: {lp}")
        print(f"Volume: {vol}")

    elif pilihan == '8':
        p = float(input("Masukkan Panjang : "))
        l = float(input("Masukkan Lebar : "))
        t = float(input("Masukkan Tinggi : "))
        lp, vol = balok(p, l, t)
        
        print(f"Luas Permukaan: {lp}")
        print(f"Volume: {vol}")

    elif pilihan == '9':
        la = float(input("Masukkan Luas Alas : "))
        ka = float(input("Masukkan Keliling Alas : "))
        t = float(input("Masukkan Tinggi : "))
        lp, vol = prisma_segitiga(la, ka, t)
       
        print(f"Luas Permukaan: {lp}")
        print(f"Volume: {vol}")

    elif pilihan == '10':
        r = float(input("Masukkan Jari-jari: "))
        lp, vol = bola(r)
       
        print(f"Luas Permukaan: {lp}")
        print(f"Volume: {vol}")

    elif pilihan == '11':
        print("\nTERIMAAA KASIHHH!!!")
        break

    else:
        print("\nPilihan tidak valid!")

    input("\n")
