import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import numpy as np
st.set_page_config(

    page_title="Churn",

    page_icon="⚠️",

    layout="wide"
)

with open("assets/styles.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("⚠️ Churn Analytics")
# LOAD DATA
data = pd.read_csv("data/customers.csv")

# LOAD MODEL
model = joblib.load(
    "models/churn_model.pkl"
)

# ==========================
# USER INPUT
# ==========================

st.subheader("🔍 Customer Churn Prediction")

col1, col2 = st.columns(2)

with col1:

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

with col2:

    tenure = st.slider(
        "Tenure (Months)",
        1,
        60,
        12
    )

# ==========================
# PREDICTION BUTTON
# ==========================

if st.button("Predict Churn"):

    input_data = np.array([
        [income, spending, tenure]
    ])

    prediction = model.predict(
        input_data
    )[0]

    probability = model.predict_proba(
        input_data
    )[0][1]

    st.divider()

    st.subheader("📊 Prediction Result")

    st.metric(
        "Churn Probability",
        f"{round(probability*100,2)}%"
    )

    # RESULT
    if prediction == 1:

        st.error("""
        ⚠️ High Risk Customer
        """)

    else:

        st.success("""
        ✅ Customer Likely to Stay
        """)

# ==========================
# CHURN ANALYTICS
# ==========================

st.divider()

st.subheader("📈 Churn Analytics")

churn = data['churn'].value_counts()

fig1 = px.pie(
    values=churn.values,
    names=["Active","Churned"],
    title="Customer Retention"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ==========================
# TENURE ANALYSIS
# ==========================

fig2 = px.box(
    data,
    x='churn',
    y='tenure',
    color='churn',
    title='Tenure vs Churn'
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================
# SPENDING ANALYSIS
# ==========================

fig3 = px.scatter(
    data,
    x='spending_score',
    y='income',
    color='churn',
    title='Spending vs Churn'
)

st.plotly_chart(
    fig3,
    use_container_width=True
)