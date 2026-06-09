import streamlit as st
import pandas as pd
import plotly.express as px

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(

    page_title="Dashboard",

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
    "AI Customer Intelligence Dashboard"
)

st.caption(
    "Transform customer data into intelligent business insights using AI and predictive analytics."
)

st.divider()

# ======================================================
# KPI SECTION
# ======================================================

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Customers",
        len(df)
    )

with k2:

    revenue = df["income"].sum()

    st.metric(
        "Revenue",
        f"${round(revenue/1000,2)}K"
    )

with k3:

    retention = round(
        (1 - df["churn"].mean()) * 100,
        1
    )

    st.metric(
        "Retention",
        f"{retention}%"
    )

with k4:

    st.metric(
        "Avg Spend",
        round(
            df["spending_score"].mean(),
            2
        )
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

    city_income = df.groupby(
        "city"
    )["income"].sum().reset_index()

    fig1 = px.bar(

        city_income,

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
# INCOME VS SPENDING
# ======================================================

with c1:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Income vs Spending"
    )

    fig3 = px.scatter(

        df,

        x="income",

        y="spending_score",

        color="gender",

        size="monthly_visits",

        hover_data=["age", "city"]
    )

    fig3.update_layout(

        paper_bgcolor="#111827",

        plot_bgcolor="#111827",

        font_color="white",

        height=450
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

    visits = df.groupby(
        "age"
    )["monthly_visits"].mean().reset_index()

    fig4 = px.line(

        visits,

        x="age",

        y="monthly_visits",

        markers=True
    )

    fig4.update_layout(

        paper_bgcolor="#111827",

        plot_bgcolor="#111827",

        font_color="white",

        height=450
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
# AI INSIGHTS
# ======================================================

st.subheader(
    "AI Insights"
)

i1, i2, i3 = st.columns(3)

with i1:

    st.success(
        "High-income customers generate maximum revenue."
    )

with i2:

    st.info(
        "Customers aged 25-35 show strongest engagement."
    )

with i3:

    st.warning(
        "Low visit customers may churn soon."
    )

st.divider()

# ======================================================
# CUSTOMER TABLE
# ======================================================

st.subheader(
    "Customer Dataset"
)

st.dataframe(
    df.head(20),
    use_container_width=True
)