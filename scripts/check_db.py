import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect("../database/ecommerce.db")
cursor = conn.cursor()

# Pobranie listy tabel w bazie
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Wyświetlenie listy tabel
print("📌 Tabele w bazie danych:")
for table in tables:
    print(f" - {table[0]}")

# Sprawdzenie, czy tabela 'orders' istnieje
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders';")
orders_table = cursor.fetchone()

if orders_table:
    print("✅ Tabela 'orders' istnieje w bazie!")
else:
    print("❌ Brak tabeli 'orders'!")

# Sprawdzenie, czy tabela 'products' istnieje
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products';")
products_table = cursor.fetchone()

if products_table:
    print("✅ Tabela 'products' istnieje w bazie!")
else:
    print("❌ Brak tabeli 'products'!")
# Sprawdzenie, czy tabela 'categories' istnieje
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='categories';")
categories_table = cursor.fetchone()

if categories_table:
    print("✅ Tabela 'categories' istnieje w bazie!")
else:
    print("❌ Brak tabeli 'categories'!")

# Zamknięcie połączenia
conn.close()
