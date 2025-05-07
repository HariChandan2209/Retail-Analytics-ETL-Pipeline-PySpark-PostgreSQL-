# config/config.py

POSTGRESQL = {
    'host': 'localhost',
    'port': '5432',
    'database': 'retail',  # Using your database name 'retail' (you can change to 'retail_dw' if you want)
    'user': 'postgres',     # Your PostgreSQL username
    'password': 'password'  # Your PostgreSQL password
}

DATA_PATHS = {
    'customers': 'data/customers.csv',
    'products': 'data/products.csv',
    'orders': 'data/orders.csv',
    'order_items': 'data/order_items.csv'
}

SPARK_CONFIG = {
    'appName': 'RetailAnalyticsETL',
    'master': 'local[*]'
}
