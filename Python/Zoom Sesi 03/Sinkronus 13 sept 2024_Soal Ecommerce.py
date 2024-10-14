# Class untuk Produk
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Stock: {self.stock}")

# Class untuk User/Pembeli
class User:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        print(f"User: {self.name}")

# Class untuk Keranjang Belanja
class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.cart_items.append((product, quantity))
            product.stock -= quantity
            print(f"Added {quantity} {product.name}(s) to cart.")
        else:
            print(f"Sorry, not enough stock for {product.name}.")

    def remove_from_cart(self, product):
        self.cart_items = [item for item in self.cart_items if item[0] != product]
        print(f"Removed {product.name} from cart.")

    def view_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
        else:
            print("Cart items:")
            for product, quantity in self.cart_items:
                print(f"{product.name} - Quantity: {quantity}")

    def get_total_price(self):
        total = sum(product.price * quantity for product, quantity in self.cart_items)
        return total

# Class untuk Invoice
class Invoice:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
        self.total_price = cart.get_total_price()

    def generate_invoice(self):
        print("======= INVOICE =======")
        self.user.get_info()
        self.cart.view_cart()
        print(f"Total price: ${self.total_price:.2f}")
        print("=======================")

# Skenario Pembelian
# Inisialisasi produk
product1 = Product("Laptop", 1200, 10)
product2 = Product("Smartphone", 800, 15)

# Inisialisasi user
user1 = User("John Doe")

# User menambahkan produk ke keranjang
cart = ShoppingCart()
cart.add_to_cart(product1, 1)  # Membeli 1 Laptop
cart.add_to_cart(product2, 2)  # Membeli 2 Smartphone

# Menampilkan isi keranjang
cart.view_cart()

# User melakukan checkout dan mendapatkan invoice
invoice = Invoice(user1, cart)
invoice.generate_invoice()
