import streamlit as st
import plotly.express as px

def render_plot(df):
    st.sidebar.header("Histogram Plot Options")

    # Select column for x-axis
    numeric_columns = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
    x_column = st.sidebar.selectbox("X-axis", numeric_columns)

    # Number of bins and KDE option
    nbins = st.sidebar.slider("Number of Bins", 10, 100, 30)
    kde = st.sidebar.checkbox("Show Kernel Density Estimate", False)

    # Additional options
    plot_title = st.sidebar.text_input("Plot Title", value="My Histogram")

    # Create the histogram
    fig = px.histogram(df, x=x_column, nbins=nbins, title=plot_title)

    # Add KDE if selected
    if kde:
        fig.add_trace(px.histogram(df, x=x_column, nbins=nbins, marginal="violin").data[0])

    st.plotly_chart(fig)

    # Button to save plot as image
    save_button = st.button("Save Histogram as Image")
    if save_button:
        fig.write_image("histogram_plot_image.png")
        st.success("Plot saved as 'histogram_plot_image.png'")
