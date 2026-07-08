import streamlit as st
import pandas as pd

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ------------------------------
# Sample Dataset
# ------------------------------
funds = pd.DataFrame({
    "Fund": [
        "HDFC Top 100",
        "SBI Bluechip",
        "ICICI Bluechip",
        "Axis Bluechip",
        "Kotak Bluechip"
    ],
    "Category": [
        "Equity",
        "Equity",
        "Equity",
        "Equity",
        "Equity"
    ],
    "Return (%)": [
        18.5,
        16.2,
        21.3,
        17.4,
        19.8
    ],
    "Risk Score": [
        4,
        3,
        5,
        4,
        4
    ],
    "Rating": [
        4.5,
        4.2,
        5.0,
        4.4,
        4.6
    ]
})

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("📊 Navigation")

page = st.sidebar.selectbox(
    "Select a Page",
    [
        "Home",
        "Fund Performance",
        "Risk Analysis",
        "Top Funds",
        "About"
    ]
)

category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(funds["Category"].unique().tolist())
)

if category != "All":
    filtered_df = funds[funds["Category"] == category]
else:
    filtered_df = funds.copy()

# ------------------------------
# HOME
# ------------------------------
if page == "Home":

    st.title("📈 Mutual Fund Analytics Dashboard")

    st.write(
        """
        Welcome to the **Bluestock Mutual Fund Analytics Dashboard**.

        This dashboard provides:
        - Mutual Fund Performance
        - Risk Analysis
        - Top Performing Funds
        - Interactive Data Visualization
        """
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Funds", len(filtered_df))

    col2.metric(
        "Average Return",
        f"{filtered_df['Return (%)'].mean():.2f}%"
    )

    col3.metric(
        "Average Rating",
        f"{filtered_df['Rating'].mean():.2f}"
    )

    st.subheader("Dataset")

    st.dataframe(filtered_df, width="stretch")

# ------------------------------
# FUND PERFORMANCE
# ------------------------------
elif page == "Fund Performance":

    st.title("📈 Fund Performance")

    st.dataframe(filtered_df, width="stretch")

    st.subheader("Returns Comparison")

    chart = filtered_df.set_index("Fund")["Return (%)"]

    st.bar_chart(chart)

# ------------------------------
# RISK ANALYSIS
# ------------------------------
elif page == "Risk Analysis":

    st.title("⚠ Risk Analysis")

    st.dataframe(filtered_df, width="stretch")

    st.subheader("Risk Scores")

    chart = filtered_df.set_index("Fund")["Risk Score"]

    st.bar_chart(chart)

# ------------------------------
# TOP FUNDS
# ------------------------------
elif page == "Top Funds":

    st.title("🏆 Top Performing Funds")

    top = filtered_df.sort_values(
        "Return (%)",
        ascending=False
    )

    st.dataframe(top, width="stretch")

    st.subheader("Top Returns")

    st.bar_chart(
        top.set_index("Fund")["Return (%)"]
    )

# ------------------------------
# ABOUT
# ------------------------------
elif page == "About":

    st.title("ℹ About")

    st.markdown("""
### Bluestock Mutual Fund Analytics Project

This project was developed using:

- Python
- Pandas
- Streamlit
- SQLite
- Power BI

### Features

- Mutual Fund Analysis
- Fund Performance Comparison
- Risk Analysis
- Dashboard Visualization
- Investment Insights

### Developer

Ungarala Ramya

B.Tech Computer Science Engineering

Bluestock Internship Project
""")