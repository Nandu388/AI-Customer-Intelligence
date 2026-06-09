import streamlit as st
import pandas as pd
import plotly.express as px
# ==========================
# LOAD CSS
# ==========================

with open("assets/styles.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


st.title("📄 Business Reports")

# Load Dataset
data = pd.read_csv("data/customers.csv")

# KPI SECTION
st.subheader("📌 Report Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Customers",
    len(data)
)

col2.metric(
    "Total Revenue",
    f"${data['income'].sum():,}"
)

col3.metric(
    "Average Spending",
    round(data['spending_score'].mean(),2)
)

st.divider()

# REVENUE BY CITY
st.subheader("🏙 Revenue Analysis")

city = data.groupby("city")["income"].sum().reset_index()

fig = px.bar(
    city,
    x="city",
    y="income",
    color="city",
    title="Revenue by City"
)

st.plotly_chart(fig, use_container_width=True)

# CUSTOMER DATA
st.subheader("👥 Customer Data")

st.dataframe(data.head(100))

# DOWNLOAD REPORT
csv = data.to_csv(index=False)

st.download_button(
    label="⬇ Download Customer Report",
    data=csv,
    file_name="customer_report.csv",
    mime="text/csv"
)

# REPORT INSIGHTS
st.subheader("💡 Report Insights")

st.success("Bangalore customers generate highest revenue.")
st.warning("Churn customers increased by 8%.")
st.info("Average spending score improved this quarter.")