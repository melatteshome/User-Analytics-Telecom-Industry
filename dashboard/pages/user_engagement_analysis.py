import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import plotly.express as px

os.chdir('..')

from database.database import DatabaseProcessor
from database.database_connection import DatabaseConnection

db_connection = DatabaseConnection()
db_processor = DatabaseProcessor()

# initialize databse connection and fetch engagment related data

query = 'SELECT * FROM total_trafic_per_application'

db_connection.connect()

dataframe = db_connection.execute_query(query)



st.write('User Engagement Analysis')
st.write(dataframe)

# top ten users per application 

df = pd.DataFrame(dataframe)

st.title("Top 10 Users per Application")

# Mapping of application display names to DataFrame column names.
applications = {
    'Social Media': 'total_social_media_traffic',
    'Google': 'total_google_traffic',
    'Email': 'total_email_traffic',
    'YouTube': 'total_youtube_traffic',
    'Netflix': 'total_netflix_traffic',
    'Gaming': 'total_gaming_traffic',
    'Other': 'total_other_traffic'
}

# Optionally, use tabs to separate each application table.
tabs = st.tabs(list(applications.keys()))

for idx, (app_name, col_name) in enumerate(applications.items()):
    with tabs[idx]:
        st.subheader(f"Top 10 Users for {app_name}")
        # Sort the DataFrame by the specific traffic column in descending order and take the top 10.
        top_users = df.sort_values(by=col_name, ascending=False).head(10)
        # Display only the user_id and the respective traffic column.
        st.dataframe(top_users[['user_id', col_name]].reset_index(drop=True))





st.title("Top 3 Most Used Applications")

# Mapping of application display names to DataFrame column names.
applications = {
    'Social Media': 'total_social_media_traffic',
    'Google': 'total_google_traffic',
    'Email': 'total_email_traffic',
    'YouTube': 'total_youtube_traffic',
    'Netflix': 'total_netflix_traffic',
    'Gaming': 'total_gaming_traffic',
    'Other': 'total_other_traffic'
}

# Calculate the total traffic for each application.
app_usage = {
    app_name: df[col_name].sum()
    for app_name, col_name in applications.items()
}

# Convert the dictionary into a DataFrame.
usage_df = pd.DataFrame(list(app_usage.items()), columns=['Application', 'Total Traffic'])
usage_df = usage_df.sort_values(by='Total Traffic', ascending=False)

# Select the top 3 most used applications.
top_3 = usage_df.head(3)

# Create a bar chart with Plotly Express.
fig = px.bar(
    top_3,
    x='Application',
    y='Total Traffic',
    title="Top 3 Most Used Applications",
    color='Application',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

st.plotly_chart(fig, use_container_width=True)
