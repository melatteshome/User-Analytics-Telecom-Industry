import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import altair as alt
import plotly.express as px


os.chdir('..')

from database.database_connection import DatabaseConnection
from database.database import DatabaseProcessor 
from src.plot_utils import plot_count



db_connection = DatabaseConnection()
db_processor = DatabaseProcessor()
connection =db_connection.connect()

query = '   SELECT * From user_scores'
dataframe = db_connection.execute_query(query= query)

st.write('User Satisfaction Analysis')

st.write(dataframe)

st.write('User Satisfaction Analysis')






# Sample DataFrame with user metrics.

df = pd.DataFrame(dataframe)

st.title("User Metrics Scatter Plot")

# Let the user choose a satisfaction threshold.
threshold = st.slider("Select satisfaction threshold", min_value=0, max_value=100, value=70)

# Add a boolean column to indicate if the user is satisfied.
df["satisfied"] = df["satisfaction_score"] >= threshold

# Count the number of satisfied users.
satisfied_count = df["satisfied"].sum()
st.write(f"**Number of satisfied users:** {satisfied_count}")

# Create a scatter plot: Engagement Score vs Experience Score.
scatter_chart = alt.Chart(df).mark_circle(size=100).encode(
    x=alt.X("engagement_score", title="Engagement Score"),
    y=alt.Y("experience_score", title="Experience Score"),
    color=alt.Color("satisfied:N", 
                    scale=alt.Scale(domain=[True, False], range=["green", "red"]),
                    title="Satisfied"),
    tooltip=["user_id", "engagement_score", "experience_score", "satisfaction_score"]
).properties(
    width=600,
    height=400,
    title="Scatter Plot of Engagement vs Experience"
)

st.altair_chart(scatter_chart, use_container_width=True)






max_satisfaction_score = df['satisfaction_score'].max()

# Define thresholds relative to the maximum score.
low_satisfaction_threshold = 0.10 * max_satisfaction_score        # 10% of max (not used directly in classification below)
moderate_satisfaction_threshold = 0.25 * max_satisfaction_score     # 25% of max
high_satisfaction_threshold = 0.50 * max_satisfaction_score         # 50% of max

# Classification function based on thresholds:
# - "Low Satisfied": score < moderate threshold.
# - "Moderately Satisfied": moderate threshold <= score < high threshold.
# - "Highly Satisfied": score >= high threshold.
def classify_satisfaction(score):
    if score < moderate_satisfaction_threshold:
        return "Low Satisfied"
    elif score < high_satisfaction_threshold:
        return "Moderately Satisfied"
    else:
        return "Highly Satisfied"

# Apply the classification to create a new column.
df['satisfaction_category'] = df['satisfaction_score'].apply(classify_satisfaction)

# Aggregate counts for each satisfaction category.
category_counts = df['satisfaction_category'].value_counts().reset_index()
category_counts.columns = ['satisfaction_category', 'count']

# Create a pie chart using Plotly Express.
fig = px.pie(
    category_counts,
    names='satisfaction_category',
    values='count',
    title='Percentage of Users by Satisfaction Category',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

# Display percentage and label inside the pie slices.
fig.update_traces(textposition='inside', textinfo='percent+label')



st.title("User Satisfaction Pie Chart")
st.plotly_chart(fig, use_container_width=True)

