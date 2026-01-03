def Nilai_rupiah(n):
    return "Rp " + "{:,}".format(int(n)).replace(",", ".")