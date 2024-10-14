class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    @age.deleter
    def age(self):
        del self._age
    
    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Age cannot be negative.")
        self._age = new_age



# 1 Apa yang dilakukan oleh potongan kode tersebut?

#a. Membuat sebuah objek Person dengan nama dan umur.

#b.Membuat sebuah decorator property untuk enkapsulasi variabel umur pada objek Person. (v)

#c.Membuat sebuah getter untuk variabel umur pada objek Person.

#d. Membuat sebuah setter untuk variabel umur pada objek Person.


#person = Person("dhea",26)
person = Person("dhea",-6)
print(person._age)
print(person._name)

person.age = 30
print(person._age)
print(person._name)

person.age = 7
print(person._age)
print(person._name)
del person._age
#print(person._age)
print(person._name)

#...2
#Apa yang dilakukan oleh decorator property pada variabel age?
#a. Membuat variabel age menjadi tidak dapat diubah.
#b. Mengubah tampilan variabel age sehingga hanya dapat ditampilkan dalam format yang sudah ditentukan.
#c. Mengenkapsulasi variabel age sehingga hanya dapat diakses melalui method getter dan setter. (v)
#d. Membuat variabel age menjadi dapat diubah.
#...

#3
#Apa yang dilakukan oleh method age.setter pada potongan kode tersebut?

#a.Membuat variabel age menjadi tidak dapat diubah.
#b.Memvalidasi nilai variabel age sebelum diubah.(v)
#c.Mengubah nilai variabel age.
#d.Menambahkan nilai variabel age.

#4.
#Apa yang terjadi jika nilai yang diberikan pada method setter melebihi nilai maksimum untuk umur?
#a.Program menghasilkan pesan kesalahan.
#b.Nilai variabel age menjadi negatif.
#c.Program mengalami kegagalan dan berhenti.(v)
#d.Variabel age tidak berubah.

#5
#Apa yang dilakukan oleh method age.deleter pada potongan kode tersebut?
#a.Mengubah nilai variabel age.
#b.Menghapus nilai variabel age.(v)
#c.Membuat variabel age menjadi tidak dapat diubah.
#d.Menambahkan nilai variabel age.


