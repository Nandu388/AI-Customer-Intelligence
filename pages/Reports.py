import streamlit as st
import pandas as pd
import plotly.express as px
import io

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(

    page_title="Reports",

    layout="wide"
)

# ======================================================
# LOAD CSS
# ======================================================

with open("assets/styles.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.image(
        "assets/logo.png",
        width=140
    )

   

    st.caption(
        "Customer Analytics Platform"
    )

    st.divider()

# ======================================================
# LOAD DATA
# ======================================================

@st.cache_data
def load_data():

    return pd.read_csv(
        "data/customers.csv"
    )

df = load_data()

# ======================================================
# HEADER
# ======================================================

st.title(
    "Business Reports"
)

st.caption(
    "Generate downloadable reports and business summaries from customer analytics."
)

st.divider()

# ======================================================
# KPI SECTION
# ======================================================

total_customers = len(df)

avg_income = round(
    df["income"].mean(),
    2
)

avg_spending = round(
    df["spending_score"].mean(),
    2
)

retention_rate = round(
    (1 - df["churn"].mean()) * 100,
    1
)

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Customers",
        total_customers
    )

with k2:

    st.metric(
        "Average Income",
        f"${avg_income}"
    )

with k3:

    st.metric(
        "Average Spending",
        avg_spending
    )

with k4:

    st.metric(
        "Retention Rate",
        f"{retention_rate}%"
    )

st.divider()

# ======================================================
# ROW 1
# ======================================================

col1, col2 = st.columns(2)

# ======================================================
# CUSTOMER SUMMARY
# ======================================================

with col1:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Customer Summary"
    )

    summary = pd.DataFrame({

        "Metric": [

            "Total Customers",

            "Average Age",

            "Average Income",

            "Average Spending",

            "Monthly Visits",

            "Retention Rate"
        ],

        "Value": [

            total_customers,

            round(df["age"].mean(),1),

            avg_income,

            avg_spending,

            round(df["monthly_visits"].mean(),1),

            f"{retention_rate}%"
        ]
    })

    st.dataframe(

        summary,

        use_container_width=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# ======================================================
# CITY REVENUE
# ======================================================

with col2:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Revenue by City"
    )

    revenue_df = df.groupby(
        "city"
    )["income"].sum().reset_index()

    fig1 = px.bar(

        revenue_df,

        x="city",

        y="income",

        color="city"
    )

    fig1.update_layout(

        paper_bgcolor="#111827",

        plot_bgcolor="#111827",

        font_color="white",

        height=400
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

st.divider()

# ======================================================
# CUSTOMER DATASET
# ======================================================

st.markdown(
    "<div class='chart-card'>",
    unsafe_allow_html=True
)

st.subheader(
    "Customer Dataset"
)

st.dataframe(

    df,

    use_container_width=True
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

st.divider()

# ======================================================
# DOWNLOAD SECTION
# ======================================================

st.subheader(
    "Download Reports"
)

# ======================================================
# CSV DOWNLOAD
# ======================================================

csv = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(

    label="Download Customer CSV Report",

    data=csv,

    file_name="customer_report.csv",

    mime="text/csv"
)

# ======================================================
# SUMMARY REPORT
# ======================================================

report_text = f"""

AI CUSTOMER INTELLIGENCE REPORT

======================================

Total Customers: {total_customers}

Average Income: ${avg_income}

Average Spending Score: {avg_spending}

Retention Rate: {retention_rate}%

Average Monthly Visits:
{round(df['monthly_visits'].mean(),1)}

======================================

BUSINESS INSIGHTS

1. High-income customers generate strong revenue.

2. Customers aged 25-35 show strongest engagement.

3. Frequent monthly visits improve retention.

4. Low engagement customers may churn.

======================================

Generated by PulseIQ Analytics Platform
"""

st.download_button(

    label="Download Business Summary",

    data=report_text,

    file_name="business_summary.txt",

    mime="text/plain"
)

st.divider()

# ======================================================
# AI INSIGHTS
# ======================================================

st.subheader(
    "AI Insights"
)

i1, i2, i3 = st.columns(3)

with i1:

    st.success(
        "Revenue growth is strongest among premium customers."
    )

with i2:

    st.info(
        "Frequent visitors demonstrate stronger retention patterns."
    )

with i3:

    st.warning(
        "Low engagement users require targeted campaigns."
    )