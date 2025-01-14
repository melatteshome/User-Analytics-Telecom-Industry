import  streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pages = {
    "Teleocme Data":[
        st.Page('user_overview_analysis.py', title="Overview Analysis"
                ),
        st.Page('user_engagement_analysis.py', title= 'Engagment Analysis'),
        st.Page('user_experience_analysis.py', title='Experience Analysis'),
        st.Page('user_satisfaction_analysis.py', title='Satisfaction Analysis')


    ]
}

naviagtion_pg = st.navigation(pages)
naviagtion_pg.run()