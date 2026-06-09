import streamlit as st
import pandas as pd
import plotly.express as px
# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(

    page_title="Dashboard",

    page_icon="📊",

    layout="wide"
)

# ==========================
# LOAD CSS
# ==========================

with open("assets/styles.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================
# PAGE TITLE
# ==========================

st.title("📊 Executive Dashboard")

# LOAD DATA
data = pd.read_csv("data/customers.csv")

# KPI CARDS
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Customers",
    len(data)
)

col2.metric(
    "Revenue",
    f"${data['income'].sum():,}"
)

col3.metric(
    "Avg Spending",
    round(data['spending_score'].mean(),2)
)

col4.metric(
    "Retention",
    f"{round((1-data['churn'].mean())*100,2)}%"
)

st.divider()

# ==========================
# REVENUE BY CITY
# ==========================

st.subheader("🏙 Revenue by City")

city = data.groupby("city")["income"].sum().reset_index()

fig1 = px.bar(
    city,
    x="city",
    y="income",
    color="city",
    title="City Revenue Analysis"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ==========================
# SPENDING TREND
# ==========================

st.subheader("📈 Customer Spending Trend")

fig2 = px.line(
    data.head(100),
    x="customer_id",
    y="spending_score",
    title="Customer Spending Pattern"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================
# GENDER DISTRIBUTION
# ==========================

st.subheader("👥 Gender Distribution")

gender = data['gender'].value_counts()

fig3 = px.pie(
    values=gender.values,
    names=gender.index,
    title="Customer Demographics"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================
# AGE VS SPENDING
# ==========================

st.subheader("💰 Age vs Spending")

fig4 = px.scatter(
    data,
    x="age",
    y="spending_score",
    color="gender",
    size="income",
    hover_data=["city"],
    title="Customer Behavior Analysis"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)