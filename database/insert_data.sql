-- Wstawianie przykładowych klientów
INSERT INTO customers (first_name, last_name, email) VALUES
('Jan', 'Kowalski', 'jan.kowalski@example.com'),
('Anna', 'Nowak', 'anna.nowak@example.com'),
('Piotr', 'Wiśniewski', 'piotr.wisniewski@example.com');

-- Wstawianie przykładowych kategorii produktów
INSERT INTO categories (name) VALUES
('Elektronika'),
('Odzież'),
('Książki');

-- Wstawianie przykładowych produktów
INSERT INTO products (name, description, price, stock, category_id) VALUES
('Laptop', 'Laptop gamingowy', 3999.99, 10, 1),
('Smartfon', 'Nowoczesny smartfon', 1999.99, 20, 1),
('Koszulka', 'Bawełniana koszulka', 49.99, 50, 2),
('Jeansy', 'Stylowe jeansy', 149.99, 30, 2),
('Książka Python', 'Podstawy Pythona', 79.99, 100, 3);

-- Wstawianie przykładowych zamówień
INSERT INTO orders (customer_id, total_amount) VALUES
(1, 3999.99),
(2, 1999.99),
(3, 229.98);
