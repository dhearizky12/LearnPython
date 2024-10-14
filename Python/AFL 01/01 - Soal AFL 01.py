class Siswa:
    def __init__(self, nama, nilai_matematika, nilai_fisika, nilai_kimia, total_mataKuliah):
        self.nama = nama
        self.nilai_matematika = nilai_matematika
        self.nilai_fisika = nilai_fisika
        self.nilai_kimia = nilai_kimia
        self.total_matakuliah = total_mataKuliah

    def get_nilai_rata_rata(self):
        total_nilai = self.nilai_matematika + self.nilai_fisika + self.nilai_kimia
        return total_nilai / self.total_matakuliah

    # Method untuk menampilkan informasi siswa
    def tampilkan_info(self):
        rata_rata = self.get_nilai_rata_rata()
        print(f"Nama: {self.nama}")
        print(f"Nilai Matematika: {self.nilai_matematika}")
        print(f"Nilai Fisika: {self.nilai_fisika}")
        print(f"Nilai Kimia: {self.nilai_kimia}")
        print(f"Nilai Rata-rata: {rata_rata:.2f}")
        print("-" * 30)

# Membuat list kosong untuk menampung objek siswa
daftar_siswa = []

# Menambahkan objek siswa ke dalam list menggunakan .append()
daftar_siswa.append(Siswa("Siswa 1", 60, 75, 85, 3))
daftar_siswa.append(Siswa("Siswa 2", 75, 55, 90, 3))
daftar_siswa.append(Siswa("Siswa 3", 85, 90, 60, 3))

# Menampilkan informasi untuk setiap siswa
for siswa in daftar_siswa:
    siswa.tampilkan_info()

# Menghitung total rata-rata dari semua siswa
def hitung_total_rata_rata(siswa_list):
    total_rata_rata = 0
    for siswa in siswa_list:
        total_rata_rata += siswa.get_nilai_rata_rata()
    return total_rata_rata / len(siswa_list)

# Menghitung dan menampilkan nilai rata-rata total dari semua siswa
total_rata_rata = hitung_total_rata_rata(daftar_siswa)
print(f"Nilai rata-rata total dari semua siswa adalah: {total_rata_rata:.2f}")
