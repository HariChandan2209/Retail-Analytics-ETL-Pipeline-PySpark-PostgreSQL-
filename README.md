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
