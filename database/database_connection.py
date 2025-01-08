import os
import psycopg2
from psycopg2 import sql, connect
from dotenv import load_dotenv
import pandas as pd

class DatabaseConnection:
    
    def __init__(self):

        load_dotenv()
        # Get the database connection parameters from environment variables
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database_name = os.getenv("DB_NAME")
        self.conn= None

    def connect(self):
             # 1. Connect to PostgreSQL server
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password= self.password,
                database= self.database_name
            )
            
            print(f"Successfully connected to the database.")
            return self.conn
        except Exception as e:
            print(f"Error connecting to the database: {e}")

        
    
    def close_connection(self):
        try:
            self.conn.close()
            print('connection closed successfully')
        except Exception as e:
            print('connection is not closed {e}')
    

    
    # def excuteQuery(self , query):
    #     try:
    #         with self.conn.cursor() as cursor:
    #            cursor.execute(query)
    #            if cursor.description:
    #              result = cursor.fetchall()
    #              return result
    #         self.conn.commit
    #         return None
    #     except Exception as e:
    #         print('error executing query: {e}')
    #         raise
    #     finally:
    #     # Close the cursor and connection
    #         if 'cursor' in locals():
    #             cursor.close()
    #         if 'connection' in locals():
    #             self.conn.close()


    def execute_query(self, query):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                if cursor.description:  # Check if the query returned data
                    # Fetch all rows
                    result = cursor.fetchall()
                    # Get column names
                    columns = [desc[0] for desc in cursor.description]
                    # Convert to DataFrame
                    df = pd.DataFrame(result, columns=columns)
                    return df
                self.conn.commit()  # Commit for write operations
                return None
        except Exception as e:
            print(f"Error executing query: {e}")
            raise
        finally:
            # Close the connection if it's no longer needed
            if hasattr(self, 'conn') and self.conn:
                self.conn.close()


               


