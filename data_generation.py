# generate_data.py

import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker()

# Parameters
NUM_CUSTOMERS = 1000
NUM_PRODUCTS = 200
NUM_ORDERS = 5000
OUTPUT_DIR = "data"

# Helper: Random dates
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

# Generate Customers
def generate_customers(num_customers):
    customers = []
    for i in range(num_customers):
        customers.append([
            i + 1,  # CustomerID starting from 1
            fake.first_name(),
            fake.last_name(),
            fake.date_of_birth(minimum_age=18, maximum_age=80),
            random.choice(["Male", "Female", "Other"]),
            fake.country(),
            fake.date_between(start_date='-10y', end_date='today')
        ])
    
    return pd.DataFrame(customers, columns=["CustomerID", "FirstName", "LastName", "DOB", "Gender", "Country", "SignupDate"])

# Generate Products
def generate_products(num_products):
    categories = ["Electronics", "Clothing", "Home", "Sports", "Books", "Toys", "Beauty"]
    brands = ["BrandA", "BrandB", "BrandC", "BrandD", "BrandE"]

    products = []
    for i in range(num_products):
        products.append([
            i + 1,  # ProductID
            fake.word().capitalize() + " " + random.choice(["Pro", "Plus", "Max", "Lite", "Basic"]),
            random.choice(categories),
            round(random.uniform(5.0, 1000.0), 2),
            random.choice(brands),
            random.randint(0, 500)  # Stock quantity
        ])
    
    return pd.DataFrame(products, columns=["ProductID", "ProductName", "Category", "Price", "Brand", "Stock"])

# Generate Orders
def generate_orders(num_orders, customers_df):
    orders = []
    for i in range(num_orders):
        customer = customers_df.sample(1).iloc[0]
        orders.append([
            i + 1,  # OrderID
            customer["CustomerID"],
            random_date(datetime(2018, 1, 1), datetime(2024, 12, 31)),
            random.choice(["Completed", "Cancelled", "Pending", "Returned"])
        ])
    
    return pd.DataFrame(orders, columns=["OrderID", "CustomerID", "OrderDate", "Status"])

# Generate Order Items
def generate_order_items(orders_df, products_df):
    order_items = []
    order_item_id = 1

    for idx, order in orders_df.iterrows():
        num_items = random.randint(1, 5)  # Each order has 1-5 items
        product_samples = products_df.sample(num_items)
        
        for _, product in product_samples.iterrows():
            quantity = random.randint(1, 10)
            unit_price = product["Price"]

            order_items.append([
                order_item_id,
                order["OrderID"],
                product["ProductID"],
                quantity,
                unit_price
            ])
            order_item_id += 1

    return pd.DataFrame(order_items, columns=["OrderItemID", "OrderID", "ProductID", "Quantity", "UnitPrice"])

# Main script
def main():
    print("Generating complex retail data...")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    customers_df = generate_customers(NUM_CUSTOMERS)
    products_df = generate_products(NUM_PRODUCTS)
    orders_df = generate_orders(NUM_ORDERS, customers_df)
    order_items_df = generate_order_items(orders_df, products_df)

    customers_df.to_csv(os.path.join(OUTPUT_DIR, "customers.csv"), index=False)
    products_df.to_csv(os.path.join(OUTPUT_DIR, "products.csv"), index=False)
    orders_df.to_csv(os.path.join(OUTPUT_DIR, "orders.csv"), index=False)
    order_items_df.to_csv(os.path.join(OUTPUT_DIR, "order_items.csv"), index=False)

    print("✅ Data generated and saved in 'data/' folder!")

if __name__ == "__main__":
    main()
