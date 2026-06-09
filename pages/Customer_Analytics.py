import streamlit as st
import pandas as pd
import plotly.express as px

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(

    page_title="Analytics",

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
    "Customer Analytics"
)

st.caption(
    "Analyze customer demographics, spending behavior, and engagement patterns."
)

st.divider()

# ======================================================
# KPI SECTION
# ======================================================

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Total Customers",
        len(df)
    )

with k2:

    st.metric(
        "Average Age",
        round(
            df["age"].mean(),
            1
        )
    )

with k3:

    st.metric(
        "Average Income",
        f"${round(df['income'].mean(),2)}"
    )

with k4:

    st.metric(
        "Average Visits",
        round(
            df["monthly_visits"].mean(),
            1
        )
    )

st.divider()

# ======================================================
# ROW 1
# ======================================================

col1, col2 = st.columns(2)

# ======================================================
# AGE DISTRIBUTION
# ======================================================

with col1:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Age Distribution"
    )

    fig1 = px.histogram(

        df,

        x="age",

        color="gender",

        nbins=20
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
# CUSTOMER BY CITY
# ======================================================

with col2:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Customers by City"
    )

    city = df["city"].value_counts().reset_index()

    city.columns = [
        "city",
        "count"
    ]

    fig2 = px.bar(

        city,

        x="city",

        y="count",

        color="city"
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
# INCOME ANALYSIS
# ======================================================

with c1:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Income Distribution"
    )

    fig3 = px.box(

        df,

        x="gender",

        y="income",

        color="gender"
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
# SPENDING SCORE
# ======================================================

with c2:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Spending Score Analysis"
    )

    fig4 = px.scatter(

        df,

        x="income",

        y="spending_score",

        color="gender",

        size="monthly_visits",

        hover_data=["age", "city"]
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
# ROW 3
# ======================================================

r1, r2 = st.columns(2)

# ======================================================
# MONTHLY VISITS
# ======================================================

with r1:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Monthly Visits Trend"
    )

    visits = df.groupby(
        "age"
    )["monthly_visits"].mean().reset_index()

    fig5 = px.line(

        visits,

        x="age",

        y="monthly_visits",

        markers=True
    )

    fig5.update_layout(

        paper_bgcolor="#111827",

        plot_bgcolor="#111827",

        font_color="white",

        height=450
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# ======================================================
# PURCHASE FREQUENCY
# ======================================================

with r2:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Purchase Frequency"
    )

    freq = df[
        "purchase_frequency"
    ].value_counts().reset_index()

    freq.columns = [
        "frequency",
        "count"
    ]

    fig6 = px.pie(

        freq,

        values="count",

        names="frequency",

        hole=0.5
    )

    fig6.update_layout(

        paper_bgcolor="#111827",

        plot_bgcolor="#111827",

        font_color="white",

        height=450
    )

    st.plotly_chart(
        fig6,
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
        "Customers with higher income show stronger spending behavior."
    )

with i2:

    st.info(
        "Customers aged 25-35 demonstrate highest engagement."
    )

with i3:

    st.warning(
        "Low monthly visits may indicate churn risk."
    )

st.divider()

# ======================================================
# CUSTOMER TABLE
# ======================================================

st.subheader(
    "Customer Dataset"
)

st.dataframe(

    df.head(25),

    use_container_width=True
)