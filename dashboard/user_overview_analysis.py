import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 

os.chdir('..')

from database.database_connection import DatabaseConnection
from database.database import DatabaseProcessor
from src.plot_utils import plot_count


#initialize database connection and fetch the data to be visualized
db_connection = DatabaseConnection()
db_processor = DatabaseProcessor()
connection =db_connection.connect()
query = '   SELECT * From xdr_data'

dataframe = db_connection.execute_query(query= query)


st.write('User Engagement Analysis')

# show top ten handsets used by customers 

top_10_handsets = dataframe['Handset Type'].value_counts().head(10)
st.write('Top 10 Handsets Used by Customers')
st.write(top_10_handsets)

top_3_manufacturers = dataframe['Handset Manufacturer'].value_counts().head(3)
st.write('Top 3 Handset Manufacturers')
st.write(top_3_manufacturers)


#read the data with numerical values only to analyze the number of sessions per user    
# numerical_data_only = pd.read_csv('columns_with_numerical_values.csv')
xdr_sessions_per_user = dataframe.groupby('MSISDN/Number')['Bearer Id'].count().reset_index(name='Number_of_xDR_sessions')


#plot the number of sessions per user
st.write('Number of sessions per user')
st.bar_chart(xdr_sessions_per_user['Number_of_xDR_sessions'].value_counts(), use_container_width=True)