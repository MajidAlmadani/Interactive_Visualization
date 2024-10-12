import streamlit as st
import plotly.express as px

def render_plot(df):
    st.sidebar.header("Heatmap Plot Options")

    numeric_columns = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
    x_column = st.sidebar.selectbox("X-axis", numeric_columns)
    y_column = st.sidebar.selectbox("Y-axis", numeric_columns)

    plot_title = st.sidebar.text_input("Plot Title", value="My Heatmap")

    fig = px.density_heatmap(df, x=x_column, y=y_column, title=plot_title)
    fig.update_layout(title={'text': plot_title, 'x': 0.5})

    st.plotly_chart(fig)

    save_button = st.button("Save Heatmap as Image")
    if save_button:
        fig.write_image("heatmap_plot_image.png")
        st.success("Plot saved as 'heatmap_plot_image.png'")
