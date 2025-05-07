# Retail Analytics ETL Pipeline (PySpark → PostgreSQL)

## 🧾 Overview

This project builds an end-to-end ETL pipeline using **PySpark* to extract, clean, transform, and load complex retail transactional data into a **PostgreSQL** data warehouse. It simulates a retail business scenario with customers, products, orders, and order items, storing them into a normalized schema, ready for business intelligence and analytics.

---

## 📁 Files Included

### 🔢 Datasets
- `customers.csv`: Customer profile data including name, gender, country, and signup details.
- `products.csv`: Product catalog including product names, categories, prices, and stock information.
- `orders.csv`: Customer orders including order dates and statuses.
- `order_items.csv`: Details of products purchased in each order, including quantity and unit price.

### 🛠️ ETL Scripts
- `generate_data`: Generates synthetic retail datasets using Faker.
- `run_pipeline.py`: Main script that executes the complete ETL pipeline.
- `etl/extract.py`: Extracts data from CSV files into PySpark DataFrames.
- `etl/transform.py`: Cleans and transforms the extracted data.
- `etl/load.py`: Loads the transformed data into PostgreSQL tables.
- `etl/utils.py`: Utility functions for Spark session creation.

### ⚙️ Configuration
- `config/config.py`: Contains database connection details and file paths.

### 📄 Other
- `requirements.txt`: List of Python dependencies required for this project.
- `README.md`: Project documentation (this file).

---

## 💻 Requirements

### Software
- Python 3.8+
- PostgreSQL database (local or Docker)
- Java 8+ (required for Spark)
- Apache Spark (via PySpark)

### Python Libraries
- `pyspark` `pandas`
- `faker`
- `psycopg2`
- `sqlalchemy`

### Driver
- PostgreSQL JDBC Driver `postgresql-42.7.1.jar` (for Spark–PostgreSQL connection)

---

## 🔁 ETL Pipeline Details

### 🔹 Extract
- Read CSV files (`customers`, `products`, `orders`, `order_items`) into PySpark DataFrames.

### 🔹 Transform
- Clean missing values.
- Derive new columns (e.g., customer age from DOB).
- Normalize fields (e.g., gender, prices).
- Validate referential integrity between datasets.

### 🔹 Load
- Insert cleaned and transformed data into PostgreSQL tables.
- Enforce foreign key constraints to maintain data warehouse relationships.

---

## 🏗️ PostgreSQL Data Warehouse Schema

### Tables
- **customers**: Customer personal information and derived age.
- **products**: Product catalog details including category, price, and brand.
- **orders**: Order-level data linked to customers.
- **order_items**: Item-level transaction details linked to orders and products.

### Relationships
- `customers.customer_id → orders.customer_idorders.order_id → order_items.order_id`
- `products.product_id → order_items.product_id`

---

## 🚀 How to Use

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download JDBC Driver
```bashcurl -o ~/Downloads/postgresql-42.7.1.jar https://jdbc.postgresql.org/download/postgresql-42.7.1.jar
```

### 3. Configure Database Settings
Edit the `config/config.py` file with your PostgreSQL:
- Host
- Port
- Database name
- Username
- Password

### 4. Create Database Tables
Manually execute SQL scripts to create the following tables:
- `customers`
- `products`
- `orders`
- `order_items`

Ensure primary and foreign keys are correctly defined.

### 5. Generate Synthetic Data
```bash
python generate_data.py
```

### 6. Run the ETL Pipeline
```bash
python run_pipeline.py
```

### 7. Verify the Load
Connect to your PostgreSQL database and validate that all tables are populated correctly.

---

## 📈 Contributio

Want to contribute? Here's how:

1. Fork this repository.
2. Create your feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request.

### Suggested Improvements
- Add data validation and quality checks.
- Create summary/aggregate tables.
- Schedule ETL using Apache Airflow.
- Add dashboards using Metabase or similar tools.

---

## 👨‍💻 Author

**Hari Chandan Edubilli**  
📧 Contact: [harichandan226@gmail.com](mailto:harichan226@gmail.com)

---

## 📄 License

This project is licensed under the **MIT License**.
