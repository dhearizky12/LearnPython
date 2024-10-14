# Custom exception for transaction errors
class TransactionError(Exception):
    pass

# Decorator untuk validasi dan pencatatan log transaksi
def log_transaksi(func):
    def wrapper(self, *args, **kwargs):
        try:
            hasil = func(self, *args, **kwargs)
            self.log_transaksi.append(f"{func.__name__.replace('_', ' ').capitalize()}: {args[0]}, saldo akhir: {self.saldo}")
            return hasil
        except TransactionError as e:
            print(f"Transaksi gagal: {e}")
    return wrapper

# Kelas AkunBank
class AkunBank:
    def __init__(self, nama_pemilik, nomor_akun, saldo_awal=0):
        self.nama_pemilik = nama_pemilik
        self.nomor_akun = nomor_akun
        self.saldo = saldo_awal
        self.log_transaksi = []

    @log_transaksi
    def setor_uang(self, jumlah):
        if jumlah <= 0:
            raise TransactionError("Jumlah setoran harus lebih besar dari nol.")
        self.saldo += jumlah

    @log_transaksi
    def tarik_uang(self, jumlah):
        if jumlah > self.saldo:
            raise TransactionError("Saldo tidak mencukupi untuk penarikan.")
        self.saldo -= jumlah

    def tampilkan_saldo(self):
        print(f"Saldo {self.nama_pemilik} ({self.nomor_akun}): Rp {self.saldo}")
    
    def tampilkan_log(self):
        print(f"Log transaksi {self.nama_pemilik}:")
        for log in self.log_transaksi:
            print(log)

# Kelas Transfer untuk menangani transfer antar akun
class Transfer:
    def __init__(self, akun_pengirim, akun_penerima):
        self.akun_pengirim = akun_pengirim
        self.akun_penerima = akun_penerima

    @log_transaksi
    def transfer_uang(self, jumlah):
        if jumlah > self.akun_pengirim.saldo:
            raise TransactionError("Saldo pengirim tidak mencukupi untuk transfer.")
        self.akun_pengirim.tarik_uang(jumlah)
        self.akun_penerima.setor_uang(jumlah)
        print(f"Transfer berhasil: Rp {jumlah} dari {self.akun_pengirim.nama_pemilik} ke {self.akun_penerima.nama_pemilik}")

# Main program
akun_A = AkunBank("A", "123456", saldo_awal=1000000)
akun_B = AkunBank("B", "789101", saldo_awal=500000)

# Setor uang ke akun A
akun_A.setor_uang(1000000)
# Tarik uang dari akun A
akun_A.tarik_uang(500000)
# Transfer uang dari akun A ke akun B
transfer = Transfer(akun_A, akun_B)
transfer.transfer_uang(300000)

# Coba tarik uang melebihi saldo
akun_A.tarik_uang(800000)  # Gagal, saldo tidak cukup

# Menampilkan saldo dan log transaksi
akun_A.tampilkan_saldo()
akun_A.tampilkan_log()

akun_B.tampilkan_saldo()
akun_B.tampilkan_log()
