# 🌊 SQL Intermediate: Sales Dashboard

## 📌 Project Description
This project is a SQL-based sales analysis system. It allows adding customers, products, orders, and performing analytical queries.

## 🚀 Features
- ✅ Create and manage an SQLite database  
- ✅ Add customers, products, and orders  
- ✅ Execute SQL queries for sales analysis  
- ✅ Advanced analytics: top customers, best-selling products  
- ✅ Interactive terminal – users choose options and perform operations  

## 🛠 Technologies
- **Python** (SQLite, SQLAlchemy)  
- **SQLite** (database)  
- **SQL** (advanced queries)  
- **PyCharm** (development environment)  

## 📂 Project Structure
```
SQL_Intermediate/
│── database/               # Database files
│   │── ecommerce.db        # Main database
│   │── schema.sql          # SQL table structure
│   │── insert_data.sql     # Sample data
│   │── queries.sql         # SQL queries
│── scripts/                # Python scripts
│   │── setup_db.py         # Creating tables
│   │── populate_db.py      # Adding test data
│   │── check_db.py         # Checking tables
│   │── insert_data.py      # Adding customers, orders, and products
│   │── run_query.py        # Running SQL queries
│── README.md               # Project documentation
```

## 📖 How to Use?
### 1️⃣ Initialize the database:
```bash
python scripts/setup_db.py
```

### 2️⃣ Add sample data:
```bash
python scripts/populate_db.py
```

### 3️⃣ Add customers, products, and orders:
```bash
python scripts/insert_data.py
```

### 4️⃣ Run SQL queries:
```bash
python scripts/run_query.py
```

## 🎯 Sample SQL Analyses
### ✅ Top Customers (Who Spent the Most?)
```sql
SELECT customers.first_name, customers.last_name, SUM(orders.total_amount) AS total_spent
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id
ORDER BY total_spent DESC
LIMIT 5;
```

### ✅ Best-Selling Products
```sql
SELECT products.name, COUNT(orders.order_id) AS total_orders
FROM orders
JOIN products ON orders.customer_id = products.product_id
GROUP BY products.name
ORDER BY total_orders DESC
LIMIT 5;
```

### ✅ Orders from the Last 7 Days
```sql
SELECT * FROM orders WHERE order_date >= DATE('now', '-7 days');
```

## 📢 Author
- 👤 **Michał Wenz**  
- 📧 **https://github.com/Znev434**

