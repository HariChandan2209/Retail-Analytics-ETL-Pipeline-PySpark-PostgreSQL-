# etl/transform.py

from pyspark.sql.functions import col, when, year, current_date, datediff

# Customers cleaning
def transform_customers(customers_df):
    # Calculate Age
    customers_df = customers_df.withColumn("Age", (datediff(current_date(), col("DOB"))/365).cast("int"))
    # Normalize Gender
    customers_df = customers_df.withColumn("Gender", when(col("Gender").isin("Male", "Female", "Other"), col("Gender")).otherwise("Other"))
    # Drop NULL CustomerIDs
    customers_df = customers_df.dropna(subset=["CustomerID"])
    return customers_df

# Products cleaning
def transform_products(products_df):
    products_df = products_df.dropna(subset=["ProductID"])
    products_df = products_df.withColumn("Price", when(col("Price") > 0, col("Price")).otherwise(10.0))
    return products_df

# Orders cleaning
def transform_orders(orders_df):
    orders_df = orders_df.dropna(subset=["OrderID", "CustomerID"])
    return orders_df

# Order Items cleaning
def transform_order_items(order_items_df):
    order_items_df = order_items_df.dropna(subset=["OrderItemID", "OrderID", "ProductID"])
    order_items_df = order_items_df.withColumn("Quantity", when(col("Quantity") > 0, col("Quantity")).otherwise(1))
    order_items_df = order_items_df.withColumn("UnitPrice", when(col("UnitPrice") > 0, col("UnitPrice")).otherwise(5.0))
    return order_items_df

