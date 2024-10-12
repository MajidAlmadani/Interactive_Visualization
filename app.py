import streamlit as st
import pandas as pd
import importlib

# Function to dynamically import a module for the selected plot
def load_plot_module(plot_type):
    try:
        return importlib.import_module(f'plots.{plot_type}_plot')
    except ModuleNotFoundError:
        st.error("Plot type not found.")
        return None

# Streamlit app title
st.title("Modular Interactive Plot Application")

# Step 1: File upload
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Detect file type and load the data
    file_extension = uploaded_file.name.split('.')[-1]
    if file_extension == 'csv':
        df = pd.read_csv(uploaded_file)
    elif file_extension == 'xlsx':
        df = pd.read_excel(uploaded_file)

    st.write("Data Preview:")
    st.write(df)

    # Step 2: Select the plot type (which is mapped to different files)
    plot_type = st.sidebar.selectbox("Plot Type", sorted(['bar', 'scatter', 'histogram', 'box', 'hexbin', 'heatmap', 'radar', 'violin']))

    # Load and display the selected plot
    plot_module = load_plot_module(plot_type)
    if plot_module:
        plot_module.render_plot(df)

else:
    st.info("Please upload a CSV or Excel file to start.")
