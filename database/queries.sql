-- Liczba klientów w bazie
SELECT COUNT(*) AS liczba_klientów FROM customers;

-- Liczba zamówień w bazie
SELECT COUNT(*) AS liczba_zamówień FROM orders;

-- Średnia wartość zamówienia
SELECT ROUND(AVG(total_amount), 2) AS srednia_wartosc_zamowienia FROM orders;

-- Najdroższy produkt
SELECT name, price FROM products ORDER BY price DESC LIMIT 1;

-- Liczba produktów w każdej kategorii
SELECT categories.name AS kategoria, COUNT(products.product_id) AS liczba_produktów
FROM products
JOIN categories ON products.category_id = categories.category_id
GROUP BY categories.name;

-- Klienci, którzy wydali najwięcej pieniędzy
SELECT customers.first_name, customers.last_name, SUM(orders.total_amount) AS suma_wydatków
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id
ORDER BY suma_wydatków DESC
LIMIT 5;

-- Najczęściej kupowane produkty
SELECT products.name, COUNT(orders.order_id) AS liczba_zamówień
FROM orders
JOIN products ON orders.customer_id = products.product_id
GROUP BY products.name
ORDER BY liczba_zamówień DESC
LIMIT 5;

-- Średnia liczba produktów na zamówienie
SELECT ROUND(AVG(product_count), 2) AS srednia_produktow_na_zamowienie
FROM (
    SELECT orders.order_id, COUNT(products.product_id) AS product_count
    FROM orders
    JOIN products ON orders.customer_id = products.product_id
    GROUP BY orders.order_id
);

-- Zamówienia z ostatnich 7 dni
SELECT * FROM orders WHERE order_date >= DATE('now', '-7 days');
