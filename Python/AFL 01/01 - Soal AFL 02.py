class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity  # Jumlah yang diminta pengguna

    def display_information(self):
        total_price = self.get_total_price()
        print(f"Name : {self.name}")
        print(f"Price : {self.price:.2f}")
        print(f"Quantity : {self.quantity}")
        print(f"Total Price : {total_price:.2f}")
        print("*" * 30)

    def get_total_price(self):
        return self.price * self.quantity

class Warehouse:
    def __init__(self, product, stock_quantity):
        self.product = product
        self.stock_quantity = stock_quantity  # Stok di warehouse

    def display_warehouse_stock(self):
        print("=========== Warehouse Stock =============")
        print(f"Product Name : {self.product.name}")
        print(f"Product stock : {self.stock_quantity}")

class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, product, warehouse):
        if warehouse.stock_quantity < product.quantity:  # Cek jika stok kurang dari permintaan
            print(f"Warning: Stok {product.name} di warehouse kurang dari permintaan.")  # Perbaikan di sini
            return
        
        if warehouse.stock_quantity > 0:  # Cek jika ada stok
            quantity_to_add = min(product.quantity, warehouse.stock_quantity)
            self.cart_items.append((product, quantity_to_add))
            warehouse.stock_quantity -= quantity_to_add  # Kurangi stok di warehouse
            product.quantity -= quantity_to_add  # Tambahkan ke keranjang
            print(f"Added {quantity_to_add} {product.name}(s) to cart.")

    def remove_from_cart(self, product):
        self.cart_items = [item for item in self.cart_items if item[0] != product]
        print(f"Removed {product.name} from cart.")

    def view_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
        else:
            print("============= Cart items : ======================")
            for product, quantity in self.cart_items:
                print(f"{product.name} - Quantity : {quantity}")

    def get_total_price(self):
        print("\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        total = sum(product.price * quantity for product, quantity in self.cart_items)
        return total

class Customer:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email
        self.shopping_cart = ShoppingCart()

    def checkout(self):
        total_price = self.shopping_cart.get_total_price()
        print(f"Total harga : {total_price:.2f}")
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n")
        self.shopping_cart.cart_items.clear()

# Inisialisasi produk
baju_wanita = Product("Baju Wanita", 200000, 3)
baju_wanita.display_information()
baju_pria = Product("Baju Pria", 250000, 2)
baju_pria.display_information()
baju_anak = Product("Baju Anak", 150000, 10)
baju_anak.display_information()

# Membuat warehouse
warehouse_A = Warehouse(baju_wanita, 10)  
warehouse_B = Warehouse(baju_pria, 5)     
warehouse_C = Warehouse(baju_anak, 20) 

warehouse_A.display_warehouse_stock()
warehouse_B.display_warehouse_stock()
warehouse_C.display_warehouse_stock()

# Membuat customer
customer = Customer("Dhea Fiky", "dhea_rizky", "email@example.com")

# Menambahkan produk ke keranjang belanja customer
print("\n*************============*****************")
customer.shopping_cart.add_item(baju_wanita, warehouse_A)  # Membeli 3 Baju Wanita
customer.shopping_cart.add_item(baju_pria, warehouse_B)    # Membeli 2 Baju Pria
customer.shopping_cart.add_item(baju_anak, warehouse_C)    # Membeli 10 Baju Anak
print("\n*************============*****************")

# Menampilkan isi keranjang belanja
customer.shopping_cart.view_cart()

# Checkout dan tampilkan total harga
customer.checkout()

warehouse_A.display_warehouse_stock()
warehouse_B.display_warehouse_stock()
warehouse_C.display_warehouse_stock()
