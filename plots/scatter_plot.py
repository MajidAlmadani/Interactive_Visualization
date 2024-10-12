import streamlit as st
import plotly.express as px

def render_plot(df):
    st.sidebar.header("Scatter Plot Options")

    # Select columns for x-axis and y-axis
    numeric_columns = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
    x_column = st.sidebar.selectbox("X-axis", numeric_columns)
    y_column = st.sidebar.selectbox("Y-axis", numeric_columns)

    # Color selection for the scatter plot
    color_column = st.sidebar.selectbox("Color by", [None] + df.columns.tolist())

    # Additional options
    plot_title = st.sidebar.text_input("Plot Title", value="My Scatter Plot")

    # Create the scatter plot
    fig = px.scatter(df, x=x_column, y=y_column, color=color_column, title=plot_title)

    st.plotly_chart(fig)

    # Button to save plot as image
    save_button = st.button("Save Scatter Plot as Image")
    if save_button:
        fig.write_image("scatter_plot_image.png")
        st.success("Plot saved as 'scatter_plot_image.png'")
