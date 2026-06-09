import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(

    page_title="Churn Analysis",

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
    "Customer Churn Analysis"
)

st.caption(
    "Analyze customer retention, churn risks, and engagement behavior."
)

st.divider()

# ======================================================
# CHURN METRICS
# ======================================================

total_customers = len(df)

churned = df["churn"].sum()

retained = total_customers - churned

retention_rate = round(
    (retained / total_customers) * 100,
    1
)

churn_rate = round(
    (churned / total_customers) * 100,
    1
)

# ======================================================
# KPI SECTION
# ======================================================

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Total Customers",
        total_customers
    )

with k2:

    st.metric(
        "Retained Customers",
        retained
    )

with k3:

    st.metric(
        "Churned Customers",
        churned
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

col1, col2 = st.columns([1,1])

# ======================================================
# CHURN DISTRIBUTION
# ======================================================

with col1:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Churn Distribution"
    )

    churn_df = pd.DataFrame({

        "Status": [
            "Retained",
            "Churned"
        ],

        "Count": [
            retained,
            churned
        ]
    })

    fig1 = px.pie(

        churn_df,

        values="Count",

        names="Status",

        hole=0.5,

        color="Status",

        color_discrete_map={

            "Retained": "#06B6D4",

            "Churned": "#EF4444"
        }
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
# RETENTION GAUGE
# ======================================================

with col2:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Retention Gauge"
    )

    fig2 = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=retention_rate,

            gauge={

                "axis": {
                    "range": [0,100]
                },

                "bar": {
                    "color": "#2563EB"
                },

                "steps": [

                    {
                        "range":[0,50],
                        "color":"#1E293B"
                    },

                    {
                        "range":[50,75],
                        "color":"#334155"
                    },

                    {
                        "range":[75,100],
                        "color":"#06B6D4"
                    }
                ]
            }
        )
    )

    fig2.update_layout(

        paper_bgcolor="#111827",

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
# INCOME VS CHURN
# ======================================================

with c1:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Income vs Churn"
    )

    fig3 = px.scatter(

        df,

        x="income",

        y="spending_score",

        color=df["churn"].astype(str),

        size="monthly_visits",

        hover_data=["age","city"]
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
# MONTHLY VISITS
# ======================================================

with c2:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Monthly Visits Analysis"
    )

    visit_df = df.groupby(
        "age"
    )["monthly_visits"].mean().reset_index()

    fig4 = px.line(

        visit_df,

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
# RISK ANALYSIS
# ======================================================

st.markdown(
    "<div class='chart-card'>",
    unsafe_allow_html=True
)

st.subheader(
    "Customer Churn Risk"
)

risk_levels = pd.DataFrame({

    "Risk Level": [

        "Low Risk",
        "Medium Risk",
        "High Risk"
    ],

    "Customers": [

        random.randint(100,200),

        random.randint(50,120),

        random.randint(20,80)
    ]
})

fig5 = px.bar(

    risk_levels,

    x="Risk Level",

    y="Customers",

    color="Risk Level",

    color_discrete_map={

        "Low Risk": "#06B6D4",

        "Medium Risk": "#F59E0B",

        "High Risk": "#EF4444"
    }
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

st.divider()

# ======================================================
# CUSTOMER TABLE
# ======================================================

st.subheader(
    "Customer Retention Dataset"
)

st.dataframe(

    df.head(25),

    use_container_width=True
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
        "High-income customers demonstrate stronger retention patterns."
    )

with i2:

    st.info(
        "Frequent monthly visits reduce churn probability."
    )

with i3:

    st.warning(
        "Low engagement users require retention campaigns."
    )