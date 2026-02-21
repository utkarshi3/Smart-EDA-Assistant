import streamlit as st
from eda_engine import load_data, get_basic_summary

st.title("Smart Data Cleaning Assistant")

uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.write("Dataset Preview")
    st.dataframe(df.head())

    summary = get_basic_summary(df)
    st.write("Dataset Summary")
    st.write(summary)