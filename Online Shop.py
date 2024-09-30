# Base class: Product
class Product:
    def __init__(self, name, price, quantity, sku):
        self.name = name        # Nama produk
        self.price = price      # Harga produk
        self.quantity = quantity # Jumlah stok produk
        self.sku = sku          # Identifier unik produk

    def buy(self, quantity):
        """Mengurangi quantity produk saat dibeli"""
        if quantity > self.quantity:
            raise ValueError(f"Requested quantity {quantity} exceeds available stock {self.quantity}.")
        self.quantity -= quantity
        print(f"Purchased {quantity} of {self.name}. Remaining stock: {self.quantity}.")

    def restock(self, quantity):
        """Menambah quantity produk saat restock"""
        self.quantity += quantity
        print(f"Restocked {quantity} of {self.name}. New stock: {self.quantity}.")

    def info(self):
        """Menampilkan informasi dasar produk"""
        print(f"======= Product Info: ========")
        print(f"SKU: {self.sku}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price:.2f}")
        print(f"Stock: {self.quantity}")
        


# Subclass: Electronics
class Electronics(Product):
    def __init__(self, name, price, quantity, sku, warranty_years, brand):
        super().__init__(name, price, quantity, sku)
        self.warranty_years = warranty_years
        self.brand = brand

    def info(self):
        """Menampilkan informasi produk Elektronik"""
        super().info()
        print(f"Brand: {self.brand}")
        print(f"Warranty: {self.warranty_years} years")
        print("*" * 30)


# Subclass: Clothing
class Clothing(Product):
    def __init__(self, name, price, quantity, sku, size, fabric_type):
        super().__init__(name, price, quantity, sku)
        self.size = size
        self.fabric_type = fabric_type

    def info(self):
        """Menampilkan informasi produk Pakaian"""
        super().info()
        print(f"Size: {self.size}")
        print(f"Fabric: {self.fabric_type}")
        print("*" * 30)


# Subclass: Book
class Book(Product):
    def __init__(self, name, price, quantity, sku, author, genre):
        super().__init__(name, price, quantity, sku)
        self.author = author
        self.genre = genre

    def info(self):
        """Menampilkan informasi produk Buku"""
        super().info()
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print("*" * 30)


# ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        """Menambah produk ke keranjang"""
        if quantity > product.quantity:
            print(f"Warning: Requested quantity for {product.name} exceeds stock.")
        else:
            self.cart_items.append((product, quantity))
            print(f"Added {quantity} of {product.name} to the cart.")

    def remove_from_cart(self, product):
        """Menghapus produk dari keranjang"""
        self.cart_items = [item for item in self.cart_items if item[0] != product]
        print(f"Removed {product.name} from the cart.")

    def view_cart(self):
        """Melihat isi keranjang"""
        if not self.cart_items:
            print("Cart is empty.")
        else:
            print("Items in cart:")
            for product, quantity in self.cart_items:
                print(f"{product.name} - Quantity: {quantity}")

    def checkout(self):
        """Checkout untuk menghitung total harga, mengurangi stok, dan mengosongkan keranjang"""
        if not self.cart_items:
            print("Cart is empty.")
            return

        total_cost = 0
        for product, quantity in self.cart_items:
            total_cost += product.price * quantity
            product.buy(quantity)

        print(f"Total cost: {total_cost:.2f}")
        self.cart_items.clear()
        print("Checkout complete. Cart is now empty.")


# Customer class
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def view_cart(self):
        """Melihat keranjang belanja customer"""
        self.shopping_cart.view_cart()

    def checkout(self):
        """Customer melakukan checkout"""
        self.shopping_cart.checkout()


# Example usage:

# Membuat produk
print("====== inisialisasi prodcut ======")
laptop = Electronics("Laptop", 15000000, 3, "SKU12345", 2, "Apple")
tshirt = Clothing("T-Shirt", 150000, 4, "SKU54321", "M", "Cotton")
novel = Book("The Great Gatsby", 90000, 6, "SKU98765", "F. Scott Fitzgerald", "Fiction")

# Menampilkan informasi produk
laptop.info()
tshirt.info()
novel.info()

# Membuat customer
customer = Customer("John Doe", "john@example.com")

# Menambah produk ke keranjang belanja
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
customer.shopping_cart.add_to_cart(laptop, 5)
customer.shopping_cart.add_to_cart(tshirt, 3)
customer.shopping_cart.add_to_cart(novel, 5)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Melihat isi keranjang
customer.view_cart()

# Melakukan checkout
customer.checkout()

# Melihat stok produk setelah checkout
laptop.info()
tshirt.info()
novel.info()

print("=====restock=====")
laptop.restock(2)
print("=====restock=====")

laptop.info()
