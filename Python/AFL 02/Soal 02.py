import math

# Kelas Induk untuk Bangun Datar
class BangunDatar:
    def hitung_luas(self):
        pass

# Kelas Induk untuk Bangun Ruang
class BangunRuang:
    def hitung_luas(self):
        pass

    def hitung_volume(self):
        pass

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

# Fungsi untuk menjalankan program
def main():
    while True:
        print("\nMenghitung Luas dan Volume Bangun")
        print("--------------------------------")
        print("1. Bangun Datar")
        print("2. Bangun Ruang")
        print("3. Exit")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            print("\nPilih jenis bangun datar yang akan dihitung:")
            print("1. Persegi")
            print("2. Persegi Panjang")
            print("3. Lingkaran")
            jenis_datar = input("Pilih jenis (1-3): ")

            if jenis_datar == "1":
                sisi = float(input("Masukkan panjang sisi: "))
                persegi = Persegi(sisi)
                print(f"Luas permukaan: {persegi.hitung_luas()}")

            elif jenis_datar == "2":
                panjang = float(input("Masukkan panjang: "))
                lebar = float(input("Masukkan lebar: "))
                persegipanjang = PersegiPanjang(panjang, lebar)
                print(f"Luas permukaan: {persegipanjang.hitung_luas()}")

            elif jenis_datar == "3":
                jari_jari = float(input("Masukkan jari-jari: "))
                lingkaran = Lingkaran(jari_jari)
                print(f"Luas permukaan: {lingkaran.hitung_luas()}")

        elif pilihan == "2":
            print("\nPilih jenis bangun ruang yang akan dihitung:")
            print("1. Kubus")
            print("2. Bola")
            jenis_ruang = input("Pilih jenis (1-2): ")

            if jenis_ruang == "1":
                rusuk = float(input("Masukkan nilai rusuk: "))
                kubus = Kubus(rusuk)
                print(f"Luas permukaan: {kubus.hitung_luas()}")
                print(f"Volume: {kubus.hitung_volume()}")

            elif jenis_ruang == "2":
                jari_jari = float(input("Masukkan nilai jari-jari: "))
                bola = Bola(jari_jari)
                print(f"Luas permukaan: {bola.hitung_luas()}")
                print(f"Volume: {bola.hitung_volume()}")

        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
