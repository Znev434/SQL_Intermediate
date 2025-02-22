import sqlite3

# Dostępne zapytania
queries = {
    "1": "SELECT COUNT(*) AS liczba_klientów FROM customers;",
    "2": "SELECT COUNT(*) AS liczba_zamówień FROM orders;",
    "3": "SELECT ROUND(AVG(total_amount), 2) AS srednia_wartosc_zamowienia FROM orders;",
    "4": "SELECT name, price FROM products ORDER BY price DESC LIMIT 1;",
    "5": """SELECT categories.name AS kategoria, COUNT(products.product_id) AS liczba_produktów
             FROM products
             JOIN categories ON products.category_id = categories.category_id
             GROUP BY categories.name;""",
    "6": """SELECT customers.first_name, customers.last_name, SUM(orders.total_amount) AS suma_wydatków
             FROM customers
             JOIN orders ON customers.customer_id = orders.customer_id
             GROUP BY customers.customer_id
             ORDER BY suma_wydatków DESC
             LIMIT 5;""",
    "7": """SELECT products.name, COUNT(orders.order_id) AS liczba_zamówień
             FROM orders
             JOIN products ON orders.customer_id = products.product_id
             GROUP BY products.name
             ORDER BY liczba_zamówień DESC
             LIMIT 5;""",
    "8": """SELECT ROUND(AVG(product_count), 2) AS srednia_produktow_na_zamowienie
             FROM (
                 SELECT orders.order_id, COUNT(products.product_id) AS product_count
                 FROM orders
                 JOIN products ON orders.customer_id = products.product_id
                 GROUP BY orders.order_id
             );""",
    "9": "SELECT * FROM orders WHERE order_date >= DATE('now', '-7 days');"
}

while True:
    # Menu wyboru
    print("\n📊 Wybierz zapytanie do wykonania:")
    print("1 - Liczba klientów w bazie")
    print("2 - Liczba zamówień w bazie")
    print("3 - Średnia wartość zamówienia")
    print("4 - Najdroższy produkt")
    print("5 - Liczba produktów w każdej kategorii")
    print("6 - Najlepsi klienci (kto wydał najwięcej)")
    print("7 - Najczęściej kupowane produkty")
    print("8 - Średnia liczba produktów na zamówienie")
    print("9 - Zamówienia z ostatnich 7 dni")
    print("0 - Wyjście z programu")

    choice = input("🔹 Wybierz numer zapytania: ")

    if choice == "0":
        print("👋 Zamykanie programu...")
        break  # Kończymy pętlę

    if choice in queries:
        # Połączenie z bazą danych
        conn = sqlite3.connect("../database/ecommerce.db")
        cursor = conn.cursor()

        # Wykonanie wybranego zapytania
        cursor.execute(queries[choice])
        results = cursor.fetchall()

        # Wyświetlenie wyników
        print("\n📊 Wynik zapytania:")
        for row in results:
            print(row)

        # Zamknięcie połączenia
        conn.close()
    else:
        print("❌ Nieprawidłowy wybór! Spróbuj ponownie.")
