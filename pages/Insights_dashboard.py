import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(

    page_title="Insights",

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
    "AI Business Insights"
)

st.caption(
    "Generate intelligent business insights using customer analytics and behavioral patterns."
)

st.divider()

# ======================================================
# KPI SECTION
# ======================================================

high_income = len(
    df[df["income"] > 80000]
)

high_spending = len(
    df[df["spending_score"] > 70]
)

frequent_visitors = len(
    df[df["monthly_visits"] > 15]
)

retention = round(
    (1 - df["churn"].mean()) * 100,
    1
)

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "High Income Customers",
        high_income
    )

with k2:

    st.metric(
        "High Spending Customers",
        high_spending
    )

with k3:

    st.metric(
        "Frequent Visitors",
        frequent_visitors
    )

with k4:

    st.metric(
        "Retention Rate",
        f"{retention}%"
    )

st.divider()

# ======================================================
# ROW 1
# ======================================================

col1, col2 = st.columns(2)

# ======================================================
# REVENUE BY CITY
# ======================================================

with col1:

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

        height=420
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# ======================================================
# CUSTOMER SEGMENTS
# ======================================================

with col2:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Customer Segments"
    )

    segments = pd.DataFrame({

        "Segment": [

            "Premium",
            "Regular",
            "Budget"
        ],

        "Customers": [

            len(df[df["income"] > 100000]),

            len(df[
                (df["income"] > 50000)
                &
                (df["income"] <= 100000)
            ]),

            len(df[df["income"] <= 50000])
        ]
    })

    fig2 = px.pie(

        segments,

        values="Customers",

        names="Segment",

        hole=0.5
    )

    fig2.update_layout(

        paper_bgcolor="#111827",

        plot_bgcolor="#111827",

        font_color="white",

        height=420
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

st.divider()

# ======================================================
# ROW 2
# ======================================================

c1, c2 = st.columns(2)

# ======================================================
# CORRELATION HEATMAP
# ======================================================

with c1:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Customer Correlation Analysis"
    )

    corr = df[

        [
            "age",
            "income",
            "spending_score",
            "monthly_visits",
            "churn"
        ]

    ].corr()

    fig3 = px.imshow(

        corr,

        text_auto=True,

        color_continuous_scale="Blues"
    )

    fig3.update_layout(

        paper_bgcolor="#111827",

        plot_bgcolor="#111827",

        font_color="white",

        height=500
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# ======================================================
# CUSTOMER ENGAGEMENT
# ======================================================

with c2:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Customer Engagement"
    )

    engagement = df.groupby(
        "age"
    )["monthly_visits"].mean().reset_index()

    fig4 = px.line(

        engagement,

        x="age",

        y="monthly_visits",

        markers=True
    )

    fig4.update_layout(

        paper_bgcolor="#111827",

        plot_bgcolor="#111827",

        font_color="white",

        height=500
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

st.divider()

# ======================================================
# AI BUSINESS INSIGHTS
# ======================================================

st.subheader(
    "AI Generated Business Insights"
)

i1, i2, i3 = st.columns(3)

with i1:

    st.success(
        "High-income customers contribute significantly to total revenue generation."
    )

with i2:

    st.info(
        "Customers aged 25-35 demonstrate strongest engagement and spending behavior."
    )

with i3:

    st.warning(
        "Low monthly engagement may indicate potential churn risk."
    )

st.divider()

# ======================================================
# STRATEGIC INSIGHTS
# ======================================================

st.markdown(
    "<div class='chart-card'>",
    unsafe_allow_html=True
)

st.subheader(
    "Strategic Recommendations"
)

recommendations = pd.DataFrame({

    "Business Strategy": [

        "Increase Premium Marketing",

        "Launch Customer Loyalty Program",

        "Improve Retention Campaigns",

        "Target Frequent Visitors",

        "Expand High Revenue Cities"
    ],

    "Expected Impact": [

        "High",

        "Medium",

        "High",

        "Medium",

        "High"
    ]
})

st.dataframe(

    recommendations,

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

st.subheader(
    "Customer Insights Dataset"
)

st.dataframe(

    df.head(25),

    use_container_width=True
)