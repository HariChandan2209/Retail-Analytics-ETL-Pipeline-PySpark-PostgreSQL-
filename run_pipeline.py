# run_pipeline.py

import os

# Set JAVA_HOME and SPARK_HOME
os.environ["JAVA_HOME"] = "/Library/Java/JavaVirtualMachines/temurin-21.jdk/Contents/Home"
os.environ["SPARK_HOME"] = "/opt/anaconda3/lib/python3.12/site-packages/pyspark"

from etl.extract import extract_data
from etl.transform import transform_customers, transform_products, transform_orders, transform_order_items
from etl.load import load_to_postgres

def main():
    print("Starting complex ETL pipeline...")

    # Extract
    customers_df, products_df, orders_df, order_items_df = extract_data()

    # Transform
    customers_clean = transform_customers(customers_df)
    products_clean = transform_products(products_df)
    orders_clean = transform_orders(orders_df)
    order_items_clean = transform_order_items(order_items_df)

    # Load
    load_to_postgres(customers_clean, "customers")
    load_to_postgres(products_clean, "products")
    load_to_postgres(orders_clean, "orders")
    load_to_postgres(order_items_clean, "order_items")

    print("✅ All tables loaded successfully into PostgreSQL!")

if __name__ == "__main__":
    main()
