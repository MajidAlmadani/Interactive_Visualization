import streamlit as st
import plotly.express as px

def render_plot(df):
    st.sidebar.header("Violin Plot Options")

    category_columns = [col for col in df.columns if df[col].dtype == object]
    numeric_columns = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]

    x_column = st.sidebar.selectbox("X-axis (categorical)", category_columns)
    y_column = st.sidebar.selectbox("Y-axis (numerical)", numeric_columns)

    color_column = st.sidebar.select
