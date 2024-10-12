import streamlit as st
import plotly.express as px

def render_plot(df):
    st.sidebar.header("Box Plot Options")

    category_columns = [col for col in df.columns if df[col].dtype == object]
    numeric_columns = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]

    x_column = st.sidebar.selectbox("X-axis (categorical)", category_columns)
    y_column = st.sidebar.selectbox("Y-axis (numerical)", numeric_columns)

    color_column = st.sidebar.selectbox("Color by", [None] + category_columns)

    plot_title = st.sidebar.text_input("Plot Title", value="My Box Plot")

    fig = px.box(df, x=x_column, y=y_column, color=color_column, title=plot_title)
    fig.update_layout(title={'text': plot_title, 'x': 0.5})

    st.plotly_chart(fig)

    save_button = st.button("Save Box Plot as Image")
    if save_button:
        fig.write_image("box_plot_image.png")
        st.success("Plot saved as 'box_plot_image.png'")
