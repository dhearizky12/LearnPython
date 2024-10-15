class JamTanganMewah:
    jumlah_jam = 0  # class variable untuk menyimpan jumlah jam tangan yang dibuat

    def __init__(self, ukiran=None):
        # constructor untuk jam tangan reguler
        if ukiran is not None:
            raise ValueError("Tidak bisa menggunakan ukiran dengan constructor ini.")
        JamTanganMewah.jumlah_jam += 1
        print(f"Permintaan jam tangan mewah berhasil di terima")

    @classmethod
    def get_jumlah_jam(cls):
        return cls.jumlah_jam

    @classmethod
    def jam_dengan_ukiran(cls, teks_ukiran):
        # constructor alternatif untuk jam tangan dengan ukiran
        # sebelum teks diukir, teks akan divalidasi
        if cls.validasi_teks(teks_ukiran):
            obj = cls()  # membuat instance jam tangan biasa terlebih dahulu
            obj.teks_ukiran = teks_ukiran
            print(f"Request teks ukiran : {teks_ukiran} berhasil diterima")
            JamTanganMewah.jumlah_jam += 1  # Menambah jumlah jam hanya jika validasi berhasil
            return obj
        return None  # Jika validasi gagal, tidak membuat objek

    @staticmethod
    def validasi_teks(teks):
        # static method untuk memvalidasi teks ukiran berdasarkan aturan yang ditentukan:
        # 1. Tidak boleh lebih dari 40 karakter
        # 2. Harus terdiri dari karakter alfanumerik (angka dan huruf)
        # 3. Jika tidak sesuai dengan aturan, tampilkan pesan error
        errorMessage = f"Teks yang diinginkan: {teks}, jumlah teks: {len(teks)}, "
        if len(teks) > 40:
            errorMessage += "Teks tidak boleh lebih dari 40 karakter dan harus alfanumerik."
            print(errorMessage)
            return False
        if not JamTanganMewah.is_alfa_numerik(teks):
            errorMessage += "Teks harus alfanumerik."
            print(errorMessage)
            return False
        return True

    @staticmethod
    def is_alfa_numerik(teks):
        # Memeriksa apakah teks hanya terdiri dari karakter alfanumerik dan spasi
        for char in teks:
            if not (char.isalnum()):  
                return False
        return True


# Pengujian kode sesuai output yang diharapkan
jam1 = JamTanganMewah  # jam tangan reguler
jam2 = JamTanganMewah.jam_dengan_ukiran("123Loremipsumdolorsitamet")  # ukiran valid
jam3 = JamTanganMewah.jam_dengan_ukiran("123Lorem ipsum dolor sit amet")  # ukiran invalid (spasi dianggap tidak alphanumerik)
jam4 = JamTanganMewah.jam_dengan_ukiran("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor")  # ukiran invalid
jam5 = JamTanganMewah.jam_dengan_ukiran("123 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor")  # ukiran invalid

# Menampilkan jumlah jam tangan yang telah dibuat
print(f"Jumlah jam tangan: {JamTanganMewah.get_jumlah_jam()}")
