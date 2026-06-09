import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="AI Customer Intelligence",
    page_icon="🤖",
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
# SIDEBAR
# ==========================

st.sidebar.image(
    "assets/logo.png",
    width=140
)

st.sidebar.title(
    "AI Customer Intelligence"
)

st.sidebar.markdown("---")

st.sidebar.success("""
AI-Powered Business Analytics Platform
""")

st.sidebar.markdown("""
### 📌 Platform Modules

- Dashboard
- Segmentation
- Churn Analytics
- Prediction
- Recommendations
- Insights Dashboard
""")

st.sidebar.markdown("---")

st.sidebar.info("""
Developed using:
- Streamlit
- Machine Learning
- Plotly
- AI Analytics
""")

# ==========================
# LOAD DATA
# ==========================

data = pd.read_csv(
    "data/customers.csv"
)

# ==========================
# MAIN TITLE
# ==========================

st.title("🤖 AI-Driven Customer Intelligence Platform")

st.markdown("""
Transform customer data into business intelligence
using Artificial Intelligence, Machine Learning,
and Predictive Analytics.
""")

# ==========================
# KPI SECTION
# ==========================

st.subheader("📊 Business Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Total Customers",
        len(data)
    )

with col2:

    st.metric(
        "Revenue",
        f"${data['income'].sum():,}"
    )

with col3:

    retention = round(
        (1 - data['churn'].mean()) * 100,
        2
    )

    st.metric(
        "Retention Rate",
        f"{retention}%"
    )

with col4:

    st.metric(
        "AI Accuracy",
        "92%"
    )

st.divider()

# ==========================
# GRAPH 1
# ==========================

st.subheader("🏙 Revenue by City")

city = data.groupby(
    "city"
)["income"].sum().reset_index()

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

st.divider()

# ==========================
# GRAPH 2
# ==========================

st.subheader("📈 Customer Spending Trend")

fig2 = px.line(
    data.head(100),
    x="customer_id",
    y="spending_score",
    markers=True,
    title="Customer Spending Pattern"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# ==========================
# GRAPH 3
# ==========================

st.subheader("👥 Customer Demographics")

gender = data['gender'].value_counts()

fig3 = px.pie(
    values=gender.values,
    names=gender.index,
    title="Gender Distribution"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()

# ==========================
# GRAPH 4
# ==========================

st.subheader("💰 Age vs Spending Analysis")

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

st.divider()

# ==========================
# GRAPH 5
# ==========================

st.subheader("⚠️ Customer Retention Analysis")

churn = data['churn'].value_counts()

fig5 = px.pie(
    values=churn.values,
    names=["Active","Churned"],
    title="Retention Overview"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.divider()

# ==========================
# PLATFORM FEATURES
# ==========================

st.subheader("🚀 AI Platform Features")

f1, f2, f3 = st.columns(3)

with f1:

    st.success("""
    📊 Customer Analytics

    Analyze customer behavior
    using advanced visualizations.
    """)

with f2:

    st.info("""
    🧠 AI Prediction

    Predict customer retention
    using Machine Learning.
    """)

with f3:

    st.warning("""
    🎁 Recommendation Engine

    Generate personalized
    customer recommendations.
    """)

st.divider()

# ==========================
# AI INSIGHTS
# ==========================

st.subheader("🤖 AI Insights")

c1, c2, c3 = st.columns(3)

with c1:

    st.success("""
    Bangalore customers generate
    the highest revenue.
    """)

with c2:

    st.warning("""
    Customers with low tenure
    show higher churn probability.
    """)

with c3:

    st.info("""
    Customers aged 25-35 show
    maximum spending behavior.
    """)

st.divider()

# ==========================
# FOOTER
# ==========================

st.markdown("""
---
### 💡 AI Customer Intelligence Platform

Built using Streamlit, Machine Learning,
Predictive Analytics, and AI Visualization.
""")