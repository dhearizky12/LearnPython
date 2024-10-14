import math

# Kelas Induk untuk Bangun Datar
class BangunDatar:
    def hitung_luas(self):
        raise NotImplementedError("Metode ini harus diimplementasikan oleh subclass")

# Kelas Induk untuk Bangun Ruang
class BangunRuang:
    def hitung_luas(self):
        raise NotImplementedError("Metode ini harus diimplementasikan oleh subclass")

    def hitung_volume(self):
        raise NotImplementedError("Metode ini harus diimplementasikan oleh subclass")

# Subclass untuk Persegi
class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

# Subclass untuk Persegi Panjang
class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

# Subclass untuk Lingkaran
class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return math.pi * (self.jari_jari ** 2)

# Subclass untuk Kubus
class Kubus(BangunRuang):
    def __init__(self, rusuk):
        self.rusuk = rusuk

    def hitung_luas(self):
        return 6 * (self.rusuk ** 2)

    def hitung_volume(self):
        return self.rusuk ** 3

# Subclass untuk Bola
class Bola(BangunRuang):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return 4 * math.pi * (self.jari_jari ** 2)

    def hitung_volume(self):
        return (4/3) * math.pi * (self.jari_jari ** 3)

# Utility untuk validasi input dan memastikan nilai positif
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Input tidak boleh negatif atau 0. Harap masukkan angka positif lebih besar dari 0.")
            else:
                return value
        except ValueError:
            print("Input tidak valid, harap masukkan angka yang benar.")

# Fungsi modular untuk bangun datar
def menu_bangun_datar():
    print("\nPilih jenis bangun datar yang akan dihitung:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Lingkaran")
    jenis_datar = input("Pilih jenis (1-3): ")

    if jenis_datar == "1":
        sisi = get_float_input("Masukkan panjang sisi: ")
        persegi = Persegi(sisi)
        print(f"=============================")
        print(f"Luas persegi adalah: {persegi.hitung_luas():.2f} unit\u00B2")
        print(f"=============================")
        
    elif jenis_datar == "2":
        panjang = get_float_input("Masukkan panjang: ")
        lebar = get_float_input("Masukkan lebar: ")
        persegipanjang = PersegiPanjang(panjang, lebar)
        print(f"=============================")
        print(f"Luas persegi panjang adalah: {persegipanjang.hitung_luas():.2f} unit\u00B2")
        print(f"=============================")
        
    elif jenis_datar == "3":
        jari_jari = get_float_input("Masukkan jari-jari: ")
        lingkaran = Lingkaran(jari_jari)
        print(f"=============================")
        print(f"Luas lingkaran adalah: {lingkaran.hitung_luas():.2f} unit\u00B2")
        print(f"=============================")
    else:
        print("Pilihan tidak valid.")

# Fungsi modular untuk bangun ruang
def menu_bangun_ruang():
    print("\nPilih jenis bangun ruang yang akan dihitung:")
    print("1. Kubus")
    print("2. Bola")
    jenis_ruang = input("Pilih jenis (1-2): ")

    if jenis_ruang == "1":
        rusuk = get_float_input("Masukkan panjang rusuk: ")
        kubus = Kubus(rusuk)
        print(f"=============================")
        print(f"Luas permukaan kubus: {kubus.hitung_luas():.2f} unit\u00B2")
        print(f"=============================")
        print(f"Volume kubus: {kubus.hitung_volume():.2f} unit\u00B3")
        print(f"=============================")
        
    elif jenis_ruang == "2":
        jari_jari = get_float_input("Masukkan jari-jari: ")
        bola = Bola(jari_jari)
        print(f"=============================")
        print(f"Luas permukaan bola: {bola.hitung_luas():.2f} unit\u00B2")
        print(f"=============================")
        print(f"Volume bola: {bola.hitung_volume():.2f} unit\u00B3")
        print(f"=============================")
        
    else:
        print("Pilihan tidak valid.")

# Fungsi utama untuk mengatur menu
def main():
    while True:
        print("\nSelamat Datang di Program Penghitung Bangun Geometri!")
        print("----------------------------------------------------")
        print("1. Menghitung Luas Bangun Datar")
        print("2. Menghitung Luas dan Volume Bangun Ruang")
        print("3. Exit")
        pilihan = input("Silakan pilih opsi (1-3): ")

        if pilihan == "1":
            menu_bangun_datar()

        elif pilihan == "2":
            menu_bangun_ruang()

        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini. Semoga harimu menyenangkan!")
            break

        else:
            print("Pilihan tidak valid. Harap pilih angka antara 1-3.")

if __name__ == "__main__":
    main()
