import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random
import time

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(

    page_title="Prediction",

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
    "AI Purchase Prediction"
)

st.caption(
    "Predict customer purchasing behavior using AI-driven analytics."
)

st.divider()

# ======================================================
# INPUT SECTION
# ======================================================

st.subheader(
    "Customer Information"
)

c1, c2, c3 = st.columns(3)

with c1:

    age = st.slider(
        "Age",
        18,
        70,
        30
    )

with c2:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with c3:

    income = st.number_input(
        "Annual Income",
        10000,
        200000,
        50000
    )

c4, c5 = st.columns(2)

with c4:

    spending = st.slider(
        "Spending Score",
        1,
        100,
        50
    )

with c5:

    visits = st.slider(
        "Monthly Visits",
        1,
        30,
        10
    )

st.divider()

# ======================================================
# PREDICTION BUTTON
# ======================================================

if st.button(
    "Predict Customer Purchases"
):

    with st.spinner(
        "Analyzing customer behavior..."
    ):

        time.sleep(2)

        # ======================================================
        # PURCHASE LOGIC
        # ======================================================

        score = (
            income * 0.35
            + spending * 300
            + visits * 800
        )

        probability = min(
            round(score / 100000 * 100, 1),
            99.9
        )

        if probability > 75:

            prediction = "High Purchase Probability"

            products = [

                "MacBook Pro",
                "iPhone 15 Pro",
                "Luxury Watch",
                "Gaming Laptop"

            ]

        elif probability > 50:

            prediction = "Moderate Purchase Probability"

            products = [

                "Smartphone",
                "Tablet",
                "Shoes",
                "Headphones"

            ]

        else:

            prediction = "Low Purchase Probability"

            products = [

                "Budget Smartphone",
                "Accessories",
                "Discount Coupons"

            ]

# ======================================================
# KPI SECTION
# ======================================================

        st.divider()

        k1, k2, k3 = st.columns(3)

        with k1:

            st.metric(
                "Purchase Probability",
                f"{probability}%"
            )

        with k2:

            st.metric(
                "Customer Segment",
                prediction
            )

        with k3:

            estimated = round(
                income * (spending / 100),
                2
            )

            st.metric(
                "Estimated Spending",
                f"${estimated}"
            )

# ======================================================
# GAUGE CHART
# ======================================================

        col1, col2 = st.columns([1,1])

        with col1:

            st.markdown(
                "<div class='chart-card'>",
                unsafe_allow_html=True
            )

            st.subheader(
                "Purchase Probability Gauge"
            )

            fig = go.Figure(

                go.Indicator(

                    mode="gauge+number",

                    value=probability,

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

            fig.update_layout(

                paper_bgcolor="#111827",

                font_color="white",

                height=400
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

# ======================================================
# PRODUCT RECOMMENDATIONS
# ======================================================

        with col2:

            st.markdown(
                "<div class='chart-card'>",
                unsafe_allow_html=True
            )

            st.subheader(
                "Recommended Products"
            )

            rec_df = pd.DataFrame({

                "Products": products,

                "Interest Score": [

                    random.randint(70,100)

                    for _ in products
                ]
            })

            fig2 = px.bar(

                rec_df,

                x="Products",

                y="Interest Score",

                color="Products"
            )

            fig2.update_layout(

                paper_bgcolor="#111827",

                plot_bgcolor="#111827",

                font_color="white",

                height=400
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

# ======================================================
# PURCHASE TREND
# ======================================================

        st.divider()

        st.markdown(
            "<div class='chart-card'>",
            unsafe_allow_html=True
        )

        st.subheader(
            "Predicted Purchase Trend"
        )

        months = [

            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ]

        values = [

            random.randint(40,100)

            for _ in months
        ]

        trend_df = pd.DataFrame({

            "Month": months,

            "Purchases": values
        })

        fig3 = px.line(

            trend_df,

            x="Month",

            y="Purchases",

            markers=True
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
# AI INSIGHTS
# ======================================================

        st.divider()

        st.subheader(
            "AI Insights"
        )

        i1, i2, i3 = st.columns(3)

        with i1:

            st.success(
                "Higher income customers show stronger buying behavior."
            )

        with i2:

            st.info(
                "Customers with frequent visits are more likely to purchase."
            )

        with i3:

            st.warning(
                "Low spending score may reduce purchase probability."
            )