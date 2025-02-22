import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect("../database/ecommerce.db")
cursor = conn.cursor()

# Wczytanie zapytań SQL z pliku schema.sql
with open("../database/schema.sql", "r", encoding="utf-8") as file:
    sql_script = file.read()

# Wykonanie zapytań SQL
cursor.executescript(sql_script)

# Zatwierdzenie zmian i zamknięcie połączenia
conn.commit()
conn.close()

print("✅ Baza danych została zainicjalizowana!")
