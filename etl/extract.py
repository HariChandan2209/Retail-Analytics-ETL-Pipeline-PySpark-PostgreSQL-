# etl/extract.py

from etl.utils import create_spark_session
from config.config import DATA_PATHS

def extract_data():
    spark = create_spark_session()

    customers_df = spark.read.csv(DATA_PATHS['customers'], header=True, inferSchema=True)
    products_df = spark.read.csv(DATA_PATHS['products'], header=True, inferSchema=True)
    orders_df = spark.read.csv(DATA_PATHS['orders'], header=True, inferSchema=True)
    order_items_df = spark.read.csv(DATA_PATHS['order_items'], header=True, inferSchema=True)

    return customers_df, products_df, orders_df, order_items_df
