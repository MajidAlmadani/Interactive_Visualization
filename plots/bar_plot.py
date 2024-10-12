import streamlit as st
import plotly.express as px

def render_plot(df):
    st.sidebar.header("Bar Plot Options")

    # Filter categorical columns (for x and y axis selection)
    category_columns = [col for col in df.columns if df[col].dtype == object]

    # Select main column (X-axis for vertical, Y-axis for horizontal)
    main_column = st.sidebar.selectbox("Main Category", category_columns)

    # Select effecting column (optional)
    effect_column = st.sidebar.selectbox("Other Effecting Category", [None] + category_columns)

    # Allow users to filter main column values (e.g., filter by days of the week)
    category_values = st.sidebar.multiselect(f"Select categories for {main_column}", options=df[main_column].unique(), default=df[main_column].unique())
    
    # Filter the DataFrame based on selected categories
    df_filtered = df[df[main_column].isin(category_values)]

    # Bar mode selection
    barmode = st.sidebar.radio("Bar Mode", options=['group', 'stack', 'relative'], index=0)

    # Orientation selection
    orientation = st.sidebar.radio("Orientation", options=['Vertical', 'Horizontal'], index=0)
    orientation = 'v' if orientation == 'Vertical' else 'h'

    # Opacity selection
    opacity = st.sidebar.slider("Opacity", 0.1, 1.0, 0.8)

    # Color palette selection
    color_palettes = {
        'Default': px.colors.qualitative.Plotly,
        'Viridis': px.colors.sequential.Viridis,
        'Cividis': px.colors.sequential.Cividis,
        'Inferno': px.colors.sequential.Inferno,
        'Plasma': px.colors.sequential.Plasma,
        'Magma': px.colors.sequential.Magma,
        'Turbo': px.colors.sequential.Turbo,
        'Jet': px.colors.sequential.Jet,
        'Rainbow': px.colors.sequential.Rainbow
    }
    color_palette = st.sidebar.selectbox("Color Palette", list(color_palettes.keys()), index=0)
    palette = color_palettes[color_palette]

    # Plot title
    plot_title = st.sidebar.text_input("Plot Title", value="My Bar Plot")

    # Logic for setting x, y based on orientation and ensuring consistency:
    if orientation == 'v':
        # For vertical: main_column on X, effect_column on Y
        fig = px.bar(
            df_filtered,
            x=main_column,  # Main category on x-axis
            y=None if effect_column is None else effect_column,  # Effect column on y-axis
            color=effect_column if effect_column else main_column,  # Color by effect or main column
            opacity=opacity,
            orientation=orientation,  # Vertical orientation
            barmode=barmode,
            color_discrete_sequence=palette  # Apply selected color palette
        )
    else:
        # For horizontal: main_column on Y, effect_column on X
        fig = px.bar(
            df_filtered,
            x=None if effect_column is None else effect_column,  # Effect column on x-axis
            y=main_column,  # Main category on y-axis
            color=effect_column if effect_column else main_column,  # Color by effect or main column
            opacity=opacity,
            orientation=orientation,  # Horizontal orientation
            barmode=barmode,
            color_discrete_sequence=palette  # Apply selected color palette
        )

    # Center the plot title
    fig.update_layout(title={'text': plot_title, 'x': 0.5})

    # Force legend consistency to ensure correct category-color mapping
    if effect_column:
        fig.update_traces(marker=dict(color=df_filtered[effect_column].astype(str).map({v: palette[i % len(palette)] for i, v in enumerate(df_filtered[effect_column].unique())})))
    
    # Show the plot
    st.plotly_chart(fig)

    # Button to save plot as image
    save_button = st.button("Save Bar Plot as Image")
    if save_button:
        fig.write_image("bar_plot_image.png")
        st.success("Plot saved as 'bar_plot_image.png'")
