import streamlit as st
import matplotlib.pyplot as plt

def render_plot(df):
    st.sidebar.header("Hexbin Plot Options")

    numeric_columns = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
    x_column = st.sidebar.selectbox("X-axis", numeric_columns)
    y_column = st.sidebar.selectbox("Y-axis", numeric_columns)

    nbins = st.sidebar.slider("Number of Bins", 10, 100, 30)

    plot_title = st.sidebar.text_input("Plot Title", value="My Hexbin Plot")

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.hexbin(df[x_column], df[y_column], gridsize=nbins, cmap='viridis')
    ax.set_title(plot_title)

    st.pyplot(fig)

    save_button = st.button("Save Hexbin Plot as Image")
    if save_button:
        fig.savefig("hexbin_plot_image.png")
        st.success("Plot saved as 'hexbin_plot_image.png'")
