import datetime

# Class Produk
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Stock: {self.stock}")

# Class Pengguna/User
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        print(f"User: {self.name} and Email : {self.email}\n")

# Class Keranjang Belanja
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.stock -= quantity  # Mengurangi stok
            print(f"Added {quantity} {product.name}(s) to cart.")
        else:
            print(f"Not enough stock for {product.name}.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("\nItems in your cart:")
            for product, quantity in self.items:
                print(f"{product.name} - Quantity: {quantity}, Price per item: {product.price:}")

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.items)

# Class Pembayaran
class Payment:
    def __init__(self, method_Payment, account_id):
        self.method_Payment = method_Payment
        self.account_id = account_id

    def process_payment(self, total_amount):
        print(f"\nProcessing payment of {total_amount:.2f} via {self.method_Payment}.")
        print(f"Account ID: {self.account_id}")

# Class Invoice
class Invoice:
    invoice_counter = 1

    def __init__(self, user, cart, payment):
        self.invoice_number = f"INV{Invoice.invoice_counter}"
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.user = user
        self.cart = cart
        self.payment = payment
        Invoice.invoice_counter += 1

    def print_invoice(self):
        print(f"\n===== INVOICE {self.invoice_number} =====")
        print(f"Date: {self.date}")
        print(f"Customer: {self.user.name}")
        print(f"Email: {self.user.email}")
        print("Items purchased:")
        self.cart.view_cart()
        print(f"Total: {self.cart.total_price():.2f}")
        print(f"Payment Method: {self.payment.method_Payment}")
        print("===========================")

# Simulasi Pembelian
# Inisialisasi User
user = User("dhea  rizky", "dhea@example.com")
user.get_info()

# Inisialisasi Produk
laptop = Product("Laptop", 5000.00, 5)
smartphone = Product("Smartphone", 1500.00, 10)

# Inisialisasi Keranjang Belanja
cart = ShoppingCart()

# Tambah produk ke keranjang
cart.add_to_cart(laptop, 1)
cart.add_to_cart(smartphone, 2)

# Lihat isi keranjang
cart.view_cart()

# Inisialisasi Pembayaran
payment = Payment("Credit Card", "123456789")

# Proses Pembayaran
payment.process_payment(cart.total_price())

# Buat dan Cetak Invoice
invoice = Invoice(user, cart, payment)
invoice.print_invoice()

##########

user1 = User("dhea  rizky", "dhea@example.com")
user1.get_info()

# Inisialisasi Produk
laptop1 = Product("Laptop", 5000.00, 5)
smartphone1 = Product("Smartphone", 1500.00, 10)

# Inisialisasi Keranjang Belanja
cart1 = ShoppingCart()

# Tambah produk ke keranjang
cart1.add_to_cart(laptop, 1)
cart1.add_to_cart(smartphone, 2)

# Lihat isi keranjang
cart1.view_cart()

# Inisialisasi Pembayaran
payment1 = Payment("Credit Card", "123456789")

# Proses Pembayaran
payment1.process_payment(cart.total_price())

# Buat dan Cetak Invoice
invoice1 = Invoice(user, cart, payment)
invoice1.print_invoice()
