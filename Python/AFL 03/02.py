class AkunError(Exception):
    pass

class AkunBank:
    def __init__(self, nomor_rekening, saldo):
        self.__nomor_rekening = nomor_rekening
        self.__saldo = saldo
        print(f"No Rekening: {self.__nomor_rekening}")
        print(f"Saldo: {self.__saldo}")
        print("=======================")
    
    @property
    def nomor_rekening(self):
        return self.__nomor_rekening
    
    # Jika seseorang mencoba mengubah nomor akun, beri peringatan dengan memunculkan error exception
    @nomor_rekening.setter
    def nomor_rekening(self, value):
        raise AkunError("No Rekening Tidak Dapat Diubah")
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, value):
        if value < 0:
            raise AkunError("Saldo Tidak Boleh Negatif")
        self.__saldo = value

    def setor(self, jumlah):
        if jumlah > 1000000:
            print("Penyetoran Dalam Jumlah Besar, diperlukan audit")
        self.saldo += jumlah
        print(f"Anda menyetor sebear : {jumlah}. Saldo anda saat ini : {self.saldo}")

    def tarik(self, jumlah):
        if jumlah > 1000000:
            print("Penarikan Dalam Jumlah Besar, diperlukan audit")
        if jumlah > self.saldo:
            raise AkunError("Saldo Tidak Mencukupi")
        self.saldo -= jumlah
        print(f"Saldo: {self.saldo}")
    
    def hapus_rekening(self):
        if self.saldo != 0:
            raise AkunError("Masih ada Saldo, Tidak Dapat Menghapus No rekening")
        print(f"No rekening {self.nomor_rekening} berhasil dihapus.")


# Contoh Penggunaan
try:
    # Buat akun bank dengan no rekening: 123456789 , dengan saldo 1.000.000
    akun = AkunBank("123456789", 1000000)
    
    # Ubah Nomor Rekening menjadi 987654321 (harus error)
    try:
        akun.nomor_rekening = "987654321"
    except AkunError as e:
        print(e)
    
    # Ganti saldo menjadi -2.000.000 (harus error)
    try:
        akun.saldo = -2000000
    except AkunError as e:
        print(e)
    
    # Ganti saldo menjadi 100.000 (sukses)
    akun.saldo = 100000
    
    # Tambahkan setoran 5.000.000 (perlu audit)
    akun.setor(5000000)
    
    # Tarik Saldo sebesar 10.000.000 (harus error)
    try:
        akun.tarik(10000000)
    except AkunError as e:
        print(e)
    
    # Hapus no rekening 123456789 (harus error)
    try:
        akun.hapus_rekening()
    except AkunError as e:
        print(e)
    
    # Tampilkan Saldo Terakhir
    print(f"Saldo: {akun.saldo}")
    
except AkunError as e:
    print(f"Error: {e}")
