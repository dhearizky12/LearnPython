#Class Tamu
class Tamu:
    def __init__(self, nama, nomor_identitas):
        self.nama = nama
        self.nomor_identitas = nomor_identitas
    
    def pesan_kamar(self, kamar):
        if kamar.cek_status():
            kamar.ubah_status(False) #ubah status kamar menjadi tidak tersedia
            print(f"{self.nama} telah memesan kamar {kamar.nomor_kamar}.")
        else:
            print(f"Maaf, kamar {kamar.nomor_kamar} tidak tersedia.")
    
    def batal_pesan(self,kamar):
        if not kamar.cek_status():
            kamar.ubah_status(True) #ubah status kamar jadi tersedia
            print(f"{self.nama} telah membatalkan pemesanan kamar {kamar.nomor_kamar}.")
        else:
            print(f"Kamar {kamar.nomor_kamar} sudah tersedia, tidak perlu dibatalkan.")


#Class Kamar :
class Kamar:
    def __init__(self, nomor_kamar, tipe_kamar, harga_per_malam):
        self.nomor_kamar = nomor_kamar
        self.tipe_kamar = tipe_kamar
        self.harga_per_malam = harga_per_malam
        self.status = True #True berarti tersedia, False berarti tidak tersedia
    
    def cek_status(self):
        return self.status

    def ubah_status(self, status_baru):
        self.status = status_baru
    
class KamarStandar(Kamar):
    def __init__(self, nomor_kamar):
        super().__init__(nomor_kamar,'Standar',500000)

        #Polymorphism : Method hitung_total_biaya() di implementasikan
    def hitung_total_biaya(self, lama_inap):
        return self.harga_per_malam * lama_inap
    
#Class Kamar Deluxe (Inheritance)
class KamarDeluxe(Kamar):
    def __init__(self, nomor_kamar):
        super().__init__(nomor_kamar, 'Deluxe', 1000000)
    
    #polymorphism : Method hitung_total_biaya() di implementasikan
    def hitung_total_biaya(self, lama_inap):
        return self.harga_per_malam * lama_inap * 0.85 #diskon 15%

# Class Reservasi
class Reservasi:
    def __init__(self, tamu, kamar, lama_inap):
        self.tamu = tamu
        self.kamar = kamar
        self.lama_inap = lama_inap

    def buat_reservasi(self):
        if self.kamar.cek_status():
            self.kamar.ubah_status(False)
            print(f"Reservasi berhasil untuk {self.tamu.nama} di kamar {self.kamar.nomor_kamar} selama {self.lama_inap} malam.")
        else:
            print(f"Maaf, kamar {self.kamar.nomor_kamar} sudah tidak tersedia.")

    def hitung_total_biaya(self):
        total_biaya = self.kamar.hitung_total_biaya(self.lama_inap)
        print(f"Total biaya untuk {self.lama_inap} malam di kamar {self.kamar.tipe_kamar}: Rp{total_biaya:,}")
        return total_biaya


# Contoh penggunaan sistem reservasi
tamu1 = Tamu("Budi", "123456")
kamar1 = KamarStandar(101)
reservasi1 = Reservasi(tamu1, kamar1, 3)

tamu1.pesan_kamar(kamar1)
reservasi1.buat_reservasi()
reservasi1.hitung_total_biaya()

# Membatalkan reservasi
tamu1.batal_pesan(kamar1)


