# Kelas Induk Item dengan parameter opsional
class Item:
    def __init__(self, title=None, author=None, publisher=None, pages=None):
        self.title = title or "-"
        self.author = author or "-"
        self.publisher = publisher or "-"
        self.pages = pages or "-"

    def get_info(self):
        # Method ini bisa diubah oleh subclass
        return f"Title: {self.title}"

# Subclass Book
class Book(Item):
    def __init__(self, title=None, author=None, publisher=None, pages=None, genre=None):
        super().__init__(title, author, publisher, pages)
        self.genre = genre or "-"

    def get_info(self):
        info = super().get_info()
        return f"Book:\n{info}\nAuthor: {self.author}\nPublisher: {self.publisher}\nPages: {self.pages}\nGenre: {self.genre}"

# Subclass Furniture
class Furniture(Item):
    def __init__(self, title=None, material=None, size=None, color=None):
        super().__init__(title)  # Hanya mengirim title ke superclass
        self.material = material or "-"
        self.size = size or "-"
        self.color = color or "-"

    def get_info(self):
        # Tidak menampilkan author, publisher, atau pages
        return f"Furniture:\nTitle: {self.title}\nMaterial: {self.material}\nSize: {self.size}\nColor: {self.color}"

# Kelas Library
class Library:
    def __init__(self):
        self.items = []
        self.id_auto_generate =  11

    def add_item(self, item):
        formatted_id = f"{self.id_auto_generate:04}"
        self.items.append((item, formatted_id))
        self.id_auto_generate += 1
        print(f"++++Item {formatted_id} {item.title} has been added++++")

    def remove_item(self, item_to_remove):
        #cek apakah input adalah string(misal judul atau material)
        array_after_remove = []
        if isinstance(item_to_remove, str):
            #Hapus item jika title atau material sama dngan input string
            for item, formatted_id in self.items:
                # Cek apakah item memiliki atribut 'title' atau 'material'
                if not (hasattr(item, 'title') and item.title == item_to_remove):
                    array_after_remove.append((item, formatted_id))

            self.items = array_after_remove
            print(f"----Item {item_to_remove} has been removed----")
        else :
            #Hapus item jika item adalah objek yang sama
            for item, formatted_id in self.items:
                # Cek apakah item memiliki atribut 'title' atau 'material'
                if item != item_to_remove:
                    array_after_remove.append((item, formatted_id))

            self.items = array_after_remove

    def show_all_items(self):
        if not self.items:
            print("Libray is empty.")
        else :
            print("===== Show All Items from class Library =====")
            for item, number in self.items:
                print( f"ID. {number} " + item.get_info())
                print("-" * 40)
            print("======= End Show All Items From Class Library ======")

# Membuat objek Book dengan sebagian atribut
book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", "HarperCollins", 1178, "Fantasy")
book2 = Book("Physics for Scientists and Engineers", "Raymond A. Serway", "Raymond A. Serway", 1328, "Textbook")
book3 = Book("National Geographic", None, "National Geographic Society", 146, "Magazine") 

# Membuat objek Furniture dengan sebagian atribut
furniture1 = Furniture("Chair", "Wood", "50x50x90 cm", "Brown")
furniture2 = Furniture("Desk", "Steel", "120x60x75 cm", "Black") 
furniture3 = Furniture("Shelf", "Particleboard","100x30x150 cm","Yellow")

# Membuat objek Library dan menambahkan item
library = Library()
library.add_item(book1)
library.add_item(book2)
library.add_item(book3)
library.add_item(furniture1)
library.add_item(furniture2)
library.add_item(furniture3)

# Menampilkan semua item di perpustakaan
library.show_all_items()
library.remove_item("The Lord of the Rings")
library.show_all_items()

library.add_item(Furniture("Sofa", "Cotton", "50x50x90 cm", "Blue"))
library.show_all_items()
