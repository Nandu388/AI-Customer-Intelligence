import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(

    page_title="Analytics",

    page_icon="📈",

    layout="wide"
)

with open("assets/styles.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("📈 Customer Analytics")

# LOAD DATA
data = pd.read_csv("data/customers.csv")

# ==========================
# CREATE CUSTOMER SEGMENTS
# ==========================

data['segment'] = pd.cut(
    data['spending_score'],
    bins=[0,40,70,100],
    labels=[
        "Low Spending",
        "Medium Spending",
        "High Spending"
    ]
)

# ==========================
# SEGMENT DISTRIBUTION
# ==========================

st.subheader("📊 Spending Segments")

segment = data['segment'].value_counts().reset_index()

segment.columns = [
    'segment',
    'count'
]

fig1 = px.bar(
    segment,
    x='segment',
    y='count',
    color='segment',
    title='Customer Spending Categories'
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.divider()

# ==========================
# AGE DISTRIBUTION
# ==========================

st.subheader("👥 Customer Age Distribution")

fig2 = px.histogram(
    data,
    x='age',
    color='gender',
    nbins=20,
    title='Age Group Analysis'
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# ==========================
# CITY REVENUE ANALYSIS
# ==========================

st.subheader("🏙 Revenue by City")

city = data.groupby(
    'city'
)['income'].sum().reset_index()

fig3 = px.bar(
    city,
    x='city',
    y='income',
    color='city',
    title='City Revenue Analysis'
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()

# ==========================
# SPENDING ANALYSIS
# ==========================

st.subheader("💰 Spending Score Analysis")

fig4 = px.box(
    data,
    x='gender',
    y='spending_score',
    color='gender',
    title='Customer Spending Behavior'
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.divider()

# ==========================
# HIGH VALUE CUSTOMERS
# ==========================

st.subheader("💎 High Value Customers")

high_value = data[
    data['income'] > 100000
]

st.dataframe(
    high_value.head(50)
)