import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Job Market Tracker", layout="wide")
st.title("🧠 AI Job Market Tracker")

df = pd.read_csv("data/cleaned_jobs.csv")
skills = ['python', 'sql', 'machine learning', 'excel', 'tableau', 'aws', 'java', 'r', 'nlp']
skill_counts = df[skills].sum().sort_values(ascending=False)

st.bar_chart(skill_counts)

if 'Location' in df.columns:
    city = st.selectbox("Select a City", df['Location'].dropna().unique())
    st.dataframe(df[df['Location'] == city][['Job Title', 'Company Name', 'Location']].head(10))
else:
    st.dataframe(df[['Job Title', 'Company Name']].head(10))
