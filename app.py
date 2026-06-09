import streamlit as st
import pandas as pd
import plotly.express as px
import time

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(

    page_title="AI Customer Intelligence",

    page_icon="📊",

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

    st.markdown(
        "## AI Customer Intelligence"
    )

    st.caption(
        "Advanced Customer Analytics Platform"
    )

    st.divider()

# ======================================================
# LOADING ANIMATION
# ======================================================

with st.spinner(
    "Loading AI analytics platform..."
):

    time.sleep(1)

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
# HERO SECTION
# ======================================================

hero1, hero2 = st.columns(
    [1,7],
    gap="small"
)

# ======================================================
# LOGO
# ======================================================

with hero1:

    st.markdown(
        """
        <div style="
            display:flex;
            justify-content:center;
            align-items:flex-start;
            padding-top:10px;
        ">
        """,
        unsafe_allow_html=True
    )

    st.image(
        "assets/logo.png",
        width=110
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# ======================================================
# TITLE CONTENT
# ======================================================

with hero2:

    st.markdown(
        """
        <div style="
            padding-top:15px;
        ">
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h1 style="
            margin-bottom:8px;
            font-size:48px;
            color:white;
            font-weight:700;
        ">

        AI Customer Intelligence Dashboard

        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="
            font-size:20px;
            color:#38BDF8;
            margin-top:0px;
            margin-bottom:16px;
            font-weight:500;
        ">

        Advanced Customer Analytics & Prediction System

        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="
            font-size:16px;
            color:#D1D5DB;
            line-height:1.8;
            max-width:950px;
        ">

        Transform customer data into actionable insights using AI-powered analytics,
        intelligent purchase prediction, recommendation systems,
        churn analysis, and business reporting.

        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

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

col1, col2 = st.columns([2,1])

# ======================================================
# REVENUE ANALYSIS
# ======================================================

with col1:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Revenue Analysis"
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

        height=420,

        transition_duration=1000
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
# GENDER DISTRIBUTION
# ======================================================

with col2:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Gender Distribution"
    )

    gender = df["gender"].value_counts()

    fig2 = px.pie(

        values=gender.values,

        names=gender.index,

        hole=0.55
    )

    fig2.update_layout(

        paper_bgcolor="#111827",

        plot_bgcolor="#111827",

        font_color="white",

        height=420,

        transition_duration=1000
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
# FEATURES SECTION
# ======================================================

st.subheader(
    "Platform Features"
)

f1, f2, f3 = st.columns(3)

with f1:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.markdown("""

    ### 📈 Analytics

    Analyze customer demographics,
    spending behavior, and engagement patterns.

    """)

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

with f2:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.markdown("""

    ### 🧠 AI Prediction

    Predict customer purchasing behavior
    using intelligent AI analytics.

    """)

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

with f3:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.markdown("""

    ### 🎁 Recommendations

    Generate personalized product
    recommendations using customer insights.

    """)

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

st.divider()

# ======================================================
# CUSTOMER INSIGHTS
# ======================================================

st.subheader(
    "AI Business Insights"
)

i1, i2, i3 = st.columns(3)

with i1:

    st.success(
        "High-income customers generate stronger revenue performance."
    )

with i2:

    st.info(
        "Customers aged 25-35 show highest engagement patterns."
    )

with i3:

    st.warning(
        "Low monthly visits may indicate future churn risk."
    )

st.divider()

# ======================================================
# CUSTOMER TABLE
# ======================================================

st.subheader(
    "Customer Dataset Preview"
)

st.dataframe(

    df.head(20),

    use_container_width=True
)

st.divider()

# ======================================================
# FOOTER
# ======================================================

st.markdown("""

<center>

### AI Customer Intelligence Platform

Built with Streamlit, Machine Learning,
and AI-driven Business Analytics.

</center>

""", unsafe_allow_html=True)