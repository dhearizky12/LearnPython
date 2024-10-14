def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dijalankan.")
        func()
        print("Setelah fungsi dijalankan.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello, World!")