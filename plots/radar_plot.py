import streamlit as st
import plotly.graph_objects as go
import numpy as np

def render_plot(df):
    st.sidebar.header("Radar Chart Options")

    numeric_columns = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
    selected_columns = st.sidebar.multiselect("Select Columns", numeric_columns)

    num_categories = st.sidebar.slider("Number of Categories", 3, len(numeric_columns), 3)

    plot_title = st.sidebar.text_input("Plot Title", value="My Radar Chart")

    if len(selected_columns) < num_categories:
        st.warning("Please select at least the number of categories specified.")
        return

    values = df[selected_columns].iloc[0].values.flatten().tolist()
    values += values[:1]
    angles = [n / float(num_categories) * 2 * np.pi for n in range(num_categories)]
    angles += angles[:1]

    fig = go.Figure(data=go.Scatterpolar(r=values, theta=selected_columns + [selected_columns[0]], fill='toself'))
    fig.update_layout(title={'text': plot_title, 'x': 0.5}, polar=dict(radialaxis=dict(visible=True)))

    st.plotly_chart(fig)

    save_button = st.button("Save Radar Chart as Image")
    if save_button:
        fig.write_image("radar_plot_image.png")
        st.success("Plot saved as 'radar_plot_image.png'")
