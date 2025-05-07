# etl/utils.py

from pyspark.sql import SparkSession
from config.config import SPARK_CONFIG
import os

def create_spark_session():
    # Set JAVA_HOME and SPARK_HOME
    os.environ["JAVA_HOME"] = "/Library/Java/JavaVirtualMachines/temurin-21.jdk/Contents/Home"
    os.environ["SPARK_HOME"] = "/opt/anaconda3/lib/python3.12/site-packages/pyspark"

    # Create Spark Session with PostgreSQL JDBC Driver attached
    spark = SparkSession.builder \
        .appName(SPARK_CONFIG['appName']) \
        .master(SPARK_CONFIG['master']) \
        .config("spark.jars", "/Users/chandanedubilli/Downloads/postgresql-42.7.1.jar") \
        .getOrCreate()

    return spark
