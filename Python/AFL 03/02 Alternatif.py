import locale

# Set locale ke format Indonesia (ID)
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

def handle_error_decorator(our_function):
    def internal_wrapper(*args, **kwargs):
        try:
            return our_function(*args, **kwargs)
        except AkunError as e:
            print("!"*30)
            print(f"Unable to proceed your request.\n{our_function.__name__}: {e}")
            print("!"*30)
    return internal_wrapper

class AkunError(Exception):
    pass

class AkunBank:
    def __init__(self, nomor_rekening, saldo):
        self.__nomor_rekening = nomor_rekening
        self.__saldo = saldo
        print("=== Selamat, Rekening anda berhasil di buat ===")
        print(f"Nomor Rekening : {self.__nomor_rekening}")
        print(f"Saldo: {locale.currency(self.__saldo, grouping=True)}")
        print(f"Bank Ciputra")
        print("===============================================")
    
    @property
    def nomor_rekening(self):
        return self.__nomor_rekening
    
    @nomor_rekening.setter
    @handle_error_decorator
    def nomor_rekening(self, value):
        raise AkunError(f"No Rekening Tidak Dapat Diubah ke : {value}")
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    @handle_error_decorator
    def saldo(self, value):
        old_saldo = self.__saldo
        if value < 0:
            raise AkunError(f"Saldo Tidak Boleh Negatif")
        self.__saldo = value
        print(f"Saldo berhasil diubah dari {locale.currency(old_saldo, grouping=True)} menjadi {locale.currency(self.__saldo, grouping=True)}")

    @handle_error_decorator
    def setor(self, jumlah):
        old_saldo = self.__saldo
        if jumlah > 1000000:
            print(f"Anda menyetor sebesar {locale.currency(jumlah, grouping=True)}. Penyetoran dalam jumlah besar, diperlukan audit")
        self.saldo += jumlah
        print(f"Anda menyetor sebesar: {locale.currency(jumlah, grouping=True)}. Saldo sebelumnya: {locale.currency(old_saldo, grouping=True)}, Saldo saat ini: {locale.currency(self.saldo, grouping=True)}")

    @handle_error_decorator
    def tarik(self, jumlah):
        if jumlah > self.saldo:
            raise AkunError(f"Saldo Tidak Mencukupi. Permintaan tarik dana : {locale.currency(jumlah, grouping=True)}, Sedangkan saldo sebesar : {locale.currency(self.saldo, grouping=True)}")
        elif jumlah > 1000000:
            print(f"Anda menarik sebesar {locale.currency(jumlah, grouping=True)}. Penarikan dalam jumlah besar, diperlukan audit")
        self.saldo -= jumlah
        print(f"Anda menarik saldo sebesar: {locale.currency(jumlah, grouping=True)}. Saldo saat ini: {locale.currency(self.saldo, grouping=True)}")
    
    @handle_error_decorator
    def hapus_rekening(self):
        if self.saldo != 0:
            raise AkunError(f"Masih ada Saldo, Tidak Dapat Menghapus No rekening")
        print(f"No rekening {self.nomor_rekening} berhasil dihapus.")

# Contoh Penggunaan
# Metode eksekusi untuk menjalankan perintah dengan penanganan error
def eksekusi(akun, aksi, *args):
    try:
        if aksi == "setor":
            akun.setor(*args)
        elif aksi == "tarik":
            akun.tarik(*args)
        elif aksi == "hapus":
            akun.hapus_rekening()
        elif aksi == "ubah_saldo":
            akun.saldo = args[0]
        elif aksi == "ubah_nomor_rekening":
            akun.nomor_rekening = args[0]
        else:
            print("Aksi tidak dikenali.")
    except AkunError as e:
        print("!"*30)
        print(e)
        print("!"*30)

# Contoh Penggunaan
akun = AkunBank("123456789", 1000000)

# Ubah Nomor Rekening menjadi 987654321 (harus error)
eksekusi(akun, "ubah_nomor_rekening", "987654321")

# Ganti saldo menjadi -2.000.000 (harus error)
eksekusi(akun, "ubah_saldo", -2000000)

# Ganti saldo menjadi 100.000 (sukses)
eksekusi(akun, "ubah_saldo", 100000)

# Tambahkan setoran 5.000.000 (perlu audit)
print("="*50)
eksekusi(akun, "setor", 5000000)
print("="*50)

# Tarik Saldo sebesar 10.000.000 (harus error)
eksekusi(akun, "tarik", 10000000)

# Hapus no rekening 123456789 (harus error)
eksekusi(akun, "hapus")

# Tampilkan Saldo Terakhir
print(f"Saldo Terakhir: {akun.saldo}")
