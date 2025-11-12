# Streamlit main application
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import load_data, get_summary


# --- Page Config ---
st.set_page_config(
    page_title="Solar Energy Dashboard",
    page_icon="☀️",
    layout="wide"
)

# --- Title and Description ---
st.title("☀️ Solar Energy Insights Dashboard")
st.markdown("Explore solar potential and key metrics interactively across countries and regions.")

# --- Sidebar Filters ---
st.sidebar.header("Filters")

# Example widgets (you'll connect these later to your data)
selected_country = st.sidebar.selectbox(
    "Select Country",
    options=["Zambia", "Benin", "Ethiopia", "Kenya"],  # Replace with dynamic list later
)

plot_type = st.sidebar.radio(
    "Choose Plot Type",
    options=["Boxplot", "Histogram"]
)

# --- Load Data (stub for now) ---
# When you have real CSVs, connect this with utils.py
df = load_data(selected_country)

# --- KPI Section (Example placeholders) ---
st.subheader(f"Key Metrics for {selected_country}")
col1, col2, col3 = st.columns(3)
col1.metric("Average GHI", "5.6 kWh/m²")
col2.metric("Top Region", "Lusaka")
col3.metric("Records", len(df) if df is not None else "N/A")

# --- Visualization Section ---
st.subheader(f"{plot_type} Visualization")

if df is not None and not df.empty:
    fig, ax = plt.subplots()
    if plot_type == "Boxplot":
        df.boxplot(column=["GHI"], ax=ax)
    elif plot_type == "Histogram":
        df["GHI"].hist(ax=ax, bins=20)
    st.pyplot(fig)
else:
    st.info("No data loaded yet. Connect your dataset in utils.py.")

# --- Table Section ---
st.subheader("Top Regions by Solar Potential")
top_regions = get_summary(df)
st.dataframe(top_regions)

# --- Footer ---
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit")

