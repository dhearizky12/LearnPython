import locale

# Set locale ke format Indonesia (ID)
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

def handle_error_decorator(our_function):
    def internal_wrapper(*args, **kwargs):
        try:
            return our_function(*args, **kwargs)
        except AkunError as e:
            print("z"*65)
            print(f"Unable to proceed your request.\n{e}")
            print("z"*65)
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
        messageInfo = (f"Saldo berhasil diubah dari {locale.currency(old_saldo, grouping=True)} ")
        messageInfo += (f"menjadi {locale.currency(self.__saldo, grouping=True)}")
        print(messageInfo)
            
    @handle_error_decorator
    def setor(self, jumlah):
        old_saldo = self.__saldo
        if jumlah < 0 :
            raise AkunError(f"Tidak boleh menyetor uang dalam bentuk negatif")
        elif jumlah == 0 :
            raise AkunError(f"Tidak boleh menyetor uang dalam bentuk 0")
        if jumlah > 1000000:
            messageInfo = (f"Anda menyetor sebesar {locale.currency(jumlah, grouping=True)}.")
            messageInfo += (f"Penyetoran dalam jumlah besar, diperlukan audit")
            print(messageInfo)

        self.saldo += jumlah
        messageInfo = (f"Anda menyetor sebesar: {locale.currency(jumlah, grouping=True)}.")
        messageInfo += (f"Saldo sebelumnya: {locale.currency(old_saldo, grouping=True)},")
        messageInfo += (f"Saldo saat ini: {locale.currency(self.saldo, grouping=True)}")
        print(messageInfo)
            

    @handle_error_decorator
    def tarik(self, jumlah):
        old_saldo = self.__saldo
        if jumlah > self.saldo:
            errorMessage = (f"Saldo Tidak Mencukupi. Permintaan tarik dana :")
            errorMessage += (f"{locale.currency(jumlah, grouping=True)}. ")
            errorMessage += (f"\nSedangkan saldo anda sebesar : {locale.currency(self.saldo, grouping=True)}")
            raise AkunError(errorMessage)
        elif jumlah > 1000000:
            messageInfo = (f"Anda menarik sebesar {locale.currency(jumlah, grouping=True)}.")
            messageInfo += (f"Penarikan dalam jumlah besar, diperlukan audit.")
            print(messageInfo)
                
            self.saldo -= jumlah
            messageInfo = (f"Anda menarik saldo sebesar: {locale.currency(jumlah, grouping=True)}.")
            messageInfo += (f"Saldo sebelumnya: {locale.currency(old_saldo, grouping=True)},")
            messageInfo += (f"\nSaldo saat ini: {locale.currency(self.saldo, grouping=True)}")
            print(messageInfo)
            
    
    @handle_error_decorator
    def hapus_rekening(self):
        if self.saldo != 0:
            errorMessage = (f"Masih ada Saldo : {locale.currency(self.saldo, grouping=True)} ,")
            errorMessage += (f"Tidak Dapat Menghapus No rekening")
            raise AkunError(errorMessage)
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
        print(e)

# Contoh Penggunaan
akun = AkunBank("123456789", 1000000)

# Ubah Nomor Rekening menjadi 987654321 (harus error)
eksekusi(akun, "ubah_nomor_rekening", "987654321")

# Ganti saldo menjadi -2.000.000 (harus error)
eksekusi(akun, "ubah_saldo", -2000000)

# Ganti saldo menjadi 100.000 (sukses)
eksekusi(akun, "ubah_saldo", 100000)

# Tambahkan setoran 5.000.000 (perlu audit)
print("="*75)
eksekusi(akun, "setor", 5000000)
print("="*75)

print("+"*70)
eksekusi(akun, "setor", -580000)
print("+"*70)

# Tarik Saldo sebesar 10.000.000 (harus error)
eksekusi(akun, "tarik", 10000000)

# Hapus no rekening 123456789 (harus error)
eksekusi(akun, "hapus")

# Tampilkan Saldo Terakhir
print(f"Saldo Terakhir: {locale.currency(akun.saldo, grouping=True)}")
