import streamlit as st
import pandas as pd
import plotly.express as px
import random
import time
st.set_page_config(

    page_title="Prediction",

    page_icon="🧠",

    layout="wide"
)

with open("assets/styles.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🧠 AI Purchase Prediction")

# ==========================
# KPI CARDS
# ==========================

k1, k2, k3 = st.columns(3)

with k1:

    st.metric(
        "Prediction Accuracy",
        "94%"
    )

with k2:

    st.metric(
        "Customers Analyzed",
        "500+"
    )

with k3:

    st.metric(
        "AI Confidence",
        "96%"
    )

st.divider()

# ==========================
# USER INPUT
# ==========================

st.subheader("📋 Customer Information")

c1, c2 = st.columns(2)

with c1:

    age = st.slider(
        "Age",
        18,
        60,
        25
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    tenure = st.slider(
        "Customer Tenure",
        1,
        60,
        12
    )

with c2:

    income = st.slider(
        "Income",
        20000,
        150000,
        50000
    )

    spending = st.slider(
        "Spending Score",
        1,
        100,
        50
    )

    visits = st.slider(
        "Monthly Visits",
        1,
        50,
        10
    )

st.divider()

# ==========================
# PREDICTION BUTTON
# ==========================

if st.button("🚀 Predict Purchases"):

    # ==========================
    # LOADING
    # ==========================

    with st.spinner(
        "Running AI behavioral analysis..."
    ):

        time.sleep(2)

        # ==========================
        # PREMIUM CUSTOMERS
        # ==========================

        if income > 100000:

            predicted_products = [

                "MacBook Pro",
                "iPhone 15 Pro",
                "Gaming Laptop",
                "Luxury Watch",
                "4K Smart TV",
                "Premium Membership"

            ]

            category = "Premium Electronics"

            purchase_probability = random.randint(88,98)

        # ==========================
        # MID CUSTOMERS
        # ==========================

        elif income > 60000:

            predicted_products = [

                "Smartphone",
                "Tablet",
                "Shoes",
                "Wireless Earbuds",
                "Fitness Band",
                "Smart Watch"

            ]

            category = "Mid-Level Shopping"

            purchase_probability = random.randint(75,90)

        # ==========================
        # LOW CUSTOMERS
        # ==========================

        else:

            predicted_products = [

                "Budget Smartphone",
                "Discount Coupons",
                "Affordable Fashion",
                "Combo Deals",
                "Wallet Cashback",
                "Basic Accessories"

            ]

            category = "Budget Shopping"

            purchase_probability = random.randint(60,80)

        engagement = random.randint(65,98)

        retention = random.randint(70,96)

# ==========================
# RESULTS
# ==========================

    st.divider()

    st.subheader("🧠 AI Prediction Results")

    r1, r2, r3 = st.columns(3)

    with r1:

        st.metric(
            "Purchase Probability",
            f"{purchase_probability}%"
        )

    with r2:

        st.metric(
            "Engagement Score",
            f"{engagement}%"
        )

    with r3:

        st.metric(
            "Retention Score",
            f"{retention}%"
        )

    st.divider()

# ==========================
# CUSTOMER ANALYSIS
# ==========================

    st.subheader("👤 Customer Analysis")

    if income > 100000:

        st.success("""
        💎 Premium customer with
        high purchasing power and
        strong engagement.
        """)

    elif income > 60000:

        st.info("""
        🛍 Medium spending customer
        interested in electronics,
        fashion, and smart devices.
        """)

    else:

        st.warning("""
        💰 Budget customer likely
        to purchase discounted
        and affordable products.
        """)

# ==========================
# RECOMMENDED PRODUCTS
# ==========================

    st.divider()

    st.subheader("🎁 Predicted Purchases")

    p1, p2 = st.columns(2)

    for i, item in enumerate(predicted_products):

        if i % 2 == 0:

            p1.success(item)

        else:

            p2.info(item)

# ==========================
# GRAPH 1
# ==========================

    st.divider()

    st.subheader("📊 Customer Behavior Analysis")

    graph_df = pd.DataFrame({

        "Metric":[
            "Age",
            "Income",
            "Spending",
            "Visits",
            "Tenure"
        ],

        "Value":[
            age,
            income,
            spending,
            visits,
            tenure
        ]
    })

    fig1 = px.bar(

        graph_df,

        x="Metric",

        y="Value",

        color="Metric",

        title="Customer Analytics"
    )

    fig1.update_layout(
        height=500
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

# ==========================
# GRAPH 2
# ==========================

    st.divider()

    st.subheader("🛒 Purchase Interest Distribution")

    purchase_df = pd.DataFrame({

        "Category":[
            "Electronics",
            "Fashion",
            "Gaming",
            "Fitness",
            "Accessories"
        ],

        "Purchases":[
            random.randint(20,40),
            random.randint(10,30),
            random.randint(5,20),
            random.randint(5,15),
            random.randint(5,10)
        ]
    })

    fig2 = px.pie(

        purchase_df,

        values="Purchases",

        names="Category",

        title="Predicted Purchase Interests"
    )

    fig2.update_layout(
        height=500
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ==========================
# GRAPH 3
# ==========================

    st.divider()

    st.subheader("📈 Predicted Buying Trend")

    trend_df = pd.DataFrame({

        "Month":[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],

        "Purchases":[
            10,
            15,
            20,
            28,
            35,
            random.randint(40,60)
        ]
    })

    fig3 = px.line(

        trend_df,

        x="Month",

        y="Purchases",

        markers=True,

        title="Future Buying Trend"
    )

    fig3.update_layout(
        height=500
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# ==========================
# GRAPH 4
# ==========================

    st.divider()

    st.subheader("📉 AI Radar Analysis")

    radar_df = pd.DataFrame(dict(

        r=[
            spending,
            engagement,
            purchase_probability,
            retention,
            visits
        ],

        theta=[
            'Spending',
            'Engagement',
            'Purchase',
            'Retention',
            'Visits'
        ]
    ))

    fig4 = px.line_polar(

        radar_df,

        r='r',

        theta='theta',

        line_close=True,

        title="AI Customer Profile"
    )

    fig4.update_traces(
        fill='toself'
    )

    fig4.update_layout(
        height=550
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# ==========================
# FINAL AI INSIGHTS
# ==========================

    st.divider()

    st.subheader("🤖 AI Insights")

    st.success(f"""
    Customers aged {age} with
    income around ${income}
    are highly interested in
    {category}.
    """)

    st.info("""
    AI predicts strong interest
    in electronics and lifestyle
    products.
    """)

    st.warning("""
    Personalized marketing
    campaigns can significantly
    increase customer purchases.
    """)

# ==========================
# DOWNLOAD REPORT
# ==========================

    st.divider()

    st.download_button(

        label="📥 Download Prediction Report",

        data=graph_df.to_csv(
            index=False
        ),

        file_name="prediction_report.csv",

        mime="text/csv"
    )