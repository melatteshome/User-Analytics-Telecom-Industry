import os
import psycopg2
from psycopg2 import sql, connect
from dotenv import load_dotenv

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
                database=self.database_name
            )
            if self.conn.closed()== 0:
                print('connection is open')
            else :
                print('connection failed or is closed')

            print(f"Successfully connected to the database '{self.database_name}'.")

        except Exception as e:
            print(f"Error connecting to the database: {e}")
            
    
    def close_connection(self):
        try:
            self.conn.close()
            print('connection closed successfully')
        except Exception as e:
            print('connection is not closed {e}')


