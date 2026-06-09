import streamlit as st
import pandas as pd
import plotly.express as px
import random

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(

    page_title="Recommendations",

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
    "Smart Recommendations"
)

st.caption(
    "Generate AI-powered product recommendations based on customer income and behavior."
)

st.divider()

# ======================================================
# INPUT SECTION
# ======================================================

st.subheader(
    "Customer Recommendation Engine"
)

income = st.slider(

    "Select Customer Income",

    10000,

    200000,

    50000
)

st.divider()

# ======================================================
# FILTER CUSTOMERS
# ======================================================

similar_customers = df[

    (df["income"] >= income - 10000)

    &

    (df["income"] <= income + 10000)

]

# ======================================================
# KPI SECTION
# ======================================================

k1, k2, k3 = st.columns(3)

with k1:

    st.metric(
        "Similar Customers",
        len(similar_customers)
    )

with k2:

    avg_spending = round(

        similar_customers[
            "spending_score"
        ].mean(),

        2
    )

    st.metric(
        "Average Spending",
        avg_spending
    )

with k3:

    avg_visits = round(

        similar_customers[
            "monthly_visits"
        ].mean(),

        2
    )

    st.metric(
        "Monthly Visits",
        avg_visits
    )

st.divider()

# ======================================================
# PRODUCT LOGIC
# ======================================================

if income > 100000:

    products = [

        "MacBook Pro",
        "iPhone 15 Pro",
        "Gaming Laptop",
        "Luxury Watch",
        "Smart Home Devices"
    ]

elif income > 60000:

    products = [

        "Smartphone",
        "Tablet",
        "Headphones",
        "Sneakers",
        "Smart Watch"
    ]

else:

    products = [

        "Budget Smartphone",
        "Accessories",
        "Discount Coupons",
        "Backpacks",
        "Basic Electronics"
    ]

# ======================================================
# ROW 1
# ======================================================

col1, col2 = st.columns([1,1])

# ======================================================
# PRODUCT RECOMMENDATIONS
# ======================================================

with col1:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Recommended Products"
    )

    product_df = pd.DataFrame({

        "Products": products,

        "Recommendation Score": [

            random.randint(70,100)

            for _ in products
        ]
    })

    fig1 = px.bar(

        product_df,

        x="Products",

        y="Recommendation Score",

        color="Products"
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
# PURCHASE CATEGORY
# ======================================================

with col2:

    st.markdown(
        "<div class='chart-card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Purchase Category Analysis"
    )

    categories = pd.DataFrame({

        "Category": [

            "Electronics",
            "Fashion",
            "Accessories",
            "Home",
            "Sports"
        ],

        "Score": [

            random.randint(50,100)

            for _ in range(5)
        ]
    })

    fig2 = px.pie(

        categories,

        values="Score",

        names="Category",

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
# CUSTOMER ANALYSIS
# ======================================================

st.markdown(
    "<div class='chart-card'>",
    unsafe_allow_html=True
)

st.subheader(
    "Customer Spending Analysis"
)

fig3 = px.scatter(

    similar_customers,

    x="income",

    y="spending_score",

    color="gender",

    size="monthly_visits",

    hover_data=["age","city"]
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

st.divider()

# ======================================================
# RECOMMENDED PRODUCTS TABLE
# ======================================================

st.subheader(
    "Recommended Product List"
)

recommend_df = pd.DataFrame({

    "Product": products,

    "Expected Interest": [

        random.randint(70,100)

        for _ in products
    ],

    "Purchase Probability": [

        random.randint(60,99)

        for _ in products
    ]
})

st.dataframe(

    recommend_df,

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
        "High-income customers prefer premium electronic products."
    )

with i2:

    st.info(
        "Frequent visitors show stronger recommendation engagement."
    )

with i3:

    st.warning(
        "Lower spending customers respond better to discounts."
    )