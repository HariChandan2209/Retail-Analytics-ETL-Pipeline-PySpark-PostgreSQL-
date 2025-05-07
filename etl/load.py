# etl/load.py

from config.config import POSTGRESQL

def load_to_postgres(df, table_name):
    url = f"jdbc:postgresql://{POSTGRESQL['host']}:{POSTGRESQL['port']}/{POSTGRESQL['database']}"
    properties = {
        "user": POSTGRESQL['user'],
        "password": POSTGRESQL['password'],
        "driver": "org.postgresql.Driver"
    }
    
    df.write.jdbc(url=url, table=table_name, mode="append", properties=properties)

