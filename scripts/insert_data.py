import sqlite3

# Funkcja do dodawania nowego klienta
def add_customer():
    first_name = input("🔹 Podaj imię: ")
    last_name = input("🔹 Podaj nazwisko: ")
    email = input("🔹 Podaj e-mail: ")

    conn = sqlite3.connect("../database/ecommerce.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)",
                   (first_name, last_name, email))

    conn.commit()
    conn.close()
    print("✅ Nowy klient został dodany!")

# Funkcja do dodawania nowego produktu
def add_product():
    name = input("🔹 Podaj nazwę produktu: ")
    description = input("🔹 Podaj opis produktu: ")
    price = float(input("🔹 Podaj cenę: "))
    stock = int(input("🔹 Podaj ilość w magazynie: "))
    category_id = int(input("🔹 Podaj ID kategorii: "))

    conn = sqlite3.connect("../database/ecommerce.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO products (name, description, price, stock, category_id) VALUES (?, ?, ?, ?, ?)",
                   (name, description, price, stock, category_id))

    conn.commit()
    conn.close()
    print("✅ Nowy produkt został dodany!")

# Funkcja do dodawania nowego zamówienia
def add_order():
    customer_id = int(input("🔹 Podaj ID klienta: "))
    total_amount = float(input("🔹 Podaj wartość zamówienia: "))

    conn = sqlite3.connect("../database/ecommerce.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO orders (customer_id, total_amount) VALUES (?, ?)",
                   (customer_id, total_amount))

    conn.commit()
    conn.close()
    print("✅ Nowe zamówienie zostało dodane!")

# Główne menu wyboru
while True:
    print("\n📌 Wybierz opcję:")
    print("1 - Dodaj nowego klienta")
    print("2 - Dodaj nowy produkt")
    print("3 - Dodaj nowe zamówienie")
    print("0 - Wyjście")

    choice = input("🔹 Wybierz numer: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        add_product()
    elif choice == "3":
        add_order()
    elif choice == "0":
        print("👋 Zamykanie programu...")
        break
    else:
        print("❌ Nieprawidłowy wybór! Spróbuj ponownie.")
