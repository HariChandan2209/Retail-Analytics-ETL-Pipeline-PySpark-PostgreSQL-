
# Retail Analytics ETL Pipeline (PySpark → PostgreSQL)

## 📚 Project Description

This project builds an **end-to-end ETL pipeline** using **PySpark** to extract, clean, transform, and load complex retail transactional data into a **PostgreSQL data warehouse**.

The pipeline handles multi-entity datasets (Customers, Products, Orders, Order Items) and creates a normalized warehouse model suitable for business intelligence and advanced analytics.

---

## 🚀 Project Structure

```plaintext
retail_etl_project/
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   └── order_items.csv
├── config/
│   └── config.py
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── utils.py
├── generate_data.py
├── run_pipeline.py
├── requirements.txt
└── README.md
🏗️ ETL Pipeline Overview

Phase	Description
Extract	Read multiple CSV datasets into PySpark DataFrames
Transform	Clean data, derive additional fields (e.g., Customer Age), validate schema
Load	Insert clean, transformed data into PostgreSQL warehouse tables
🗃️ PostgreSQL Warehouse Schema

Tables:

customers — Dimension: Customer profiles
products — Dimension: Product catalog
orders — Fact: Customer orders
order_items — Fact: Items within each order
Relationships:

customers (CustomerID PK)
   └── orders (CustomerID FK)
           └── order_items (OrderID FK, ProductID FK)
products (ProductID PK)
   └── order_items (ProductID FK)
🛠️ Technologies Used

PySpark — Data extraction, transformation
PostgreSQL — Data warehouse (relational model)
Faker — Generate synthetic retail data
Python — Scripting
JDBC Driver — PostgreSQL connection with Spark
⚙️ How to Run the Project

1. Install Requirements
pip install -r requirements.txt
Make sure pyspark, faker, psycopg2, and sqlalchemy are installed.

2. Download PostgreSQL JDBC Driver
Download PostgreSQL driver:

curl -o ~/Downloads/postgresql-42.7.1.jar https://jdbc.postgresql.org/download/postgresql-42.7.1.jar
Make sure the .jar path is correctly referenced inside etl/utils.py.

3. Configure Database Connection
Update config/config.py with your PostgreSQL username, password, and database name.

Example:

POSTGRESQL = {
    'host': 'localhost',
    'port': '5432',
    'database': 'retail',
    'user': 'postgres',
    'password': 'password'
}
4. Generate Synthetic Data
python generate_data.py
This creates 4 datasets:

customers.csv
products.csv
orders.csv
order_items.csv
in the data/ directory.

5. Create PostgreSQL Tables
Run the following SQL DDL scripts manually in your PostgreSQL database:

CREATE TABLE customers (
    CustomerID INT PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    DOB DATE,
    Gender TEXT,
    Country TEXT,
    SignupDate DATE,
    Age INT
);

CREATE TABLE products (
    ProductID INT PRIMARY KEY,
    ProductName TEXT,
    Category TEXT,
    Price FLOAT,
    Brand TEXT,
    Stock INT
);

CREATE TABLE orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT REFERENCES customers(CustomerID),
    OrderDate DATE,
    Status TEXT
);

CREATE TABLE order_items (
    OrderItemID INT PRIMARY KEY,
    OrderID INT REFERENCES orders(OrderID),
    ProductID INT REFERENCES products(ProductID),
    Quantity INT,
    UnitPrice FLOAT
);
6. Run the ETL Pipeline
python run_pipeline.py
✅ This will load all clean datasets into PostgreSQL warehouse tables.

📈 Future Enhancements

Add data quality checks and validations
Partition large datasets by OrderDate (monthly/yearly)
Build analytical aggregate tables (monthly revenue, top-selling products)
Connect to BI tools like Metabase, PowerBI for visualization
Orchestrate ETL using Airflow
✨ Acknowledgments

Apache Spark
PostgreSQL
Faker Python Library
📬 Contact

For any queries or collaboration opportunities, please feel free to reach out!

