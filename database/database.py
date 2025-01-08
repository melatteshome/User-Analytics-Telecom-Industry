import pandas as pd
import numpy as np
import psycopg2 


class DatabaseProcessor:
    def __init__(self):
        pass

    def get_data_from_database(self , database_path , query ):
        connection = psycopg2.connect(database_path)
        df = pd.read_sql_query(query, connection)
        connection.close()
        return df
    

  




