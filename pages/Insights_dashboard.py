import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
st.set_page_config(

    page_title="Insights",

    page_icon="💡",

    layout="wide"
)

with open("assets/styles.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("💡 AI Insights Dashboard")

# ==========================
# LOAD DATA
# ==========================

data = pd.read_csv(
    "data/customers.csv"
)

# ==========================
# KPI CARDS
# ==========================

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "Total Customers",
        len(data)
    )

with c2:

    st.metric(
        "Revenue",
        f"${data['income'].sum():,}"
    )

with c3:

    st.metric(
        "Avg Spending",
        round(
            data['spending_score'].mean(),
            2
        )
    )

with c4:

    retention = round(
        (1 - data['churn'].mean()) * 100,
        2
    )

    st.metric(
        "Retention",
        f"{retention}%"
    )

st.divider()

# ==========================
# AI INSIGHTS
# ==========================

st.subheader("🤖 AI Business Insights")

i1, i2, i3 = st.columns(3)

with i1:

    st.success("""
    High-income customers generate
    maximum business revenue.
    """)

with i2:

    st.info("""
    Customers aged 25-35 are
    highly active buyers.
    """)

with i3:

    st.warning("""
    Low-tenure customers show
    higher churn probability.
    """)

st.divider()

# ==========================
# HEATMAP
# ==========================

st.subheader("🔥 Customer Correlation Heatmap")

fig, ax = plt.subplots(
    figsize=(7,3)
)

sns.heatmap(

    data[
        [
            'age',
            'income',
            'spending_score',
            'tenure',
            'monthly_visits',
            'purchase_frequency'
        ]
    ].corr(),

    annot=True,
    cmap='coolwarm',
    ax=ax
)

# CENTER ALIGN
col1, col2, col3 = st.columns([1,4,1])

with col2:

    st.pyplot(
        fig,
        use_container_width=False
    )

st.divider()

# ==========================
# GRAPH 1
# ==========================

st.subheader("📈 Income vs Spending")

fig1 = px.scatter(

    data,

    x='income',

    y='spending_score',

    color='gender',

    size='monthly_visits',

    hover_data=['city'],

    title='Customer Spending Behavior'
)

fig1.update_layout(
    height=500
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.divider()

# ==========================
# GRAPH 2
# ==========================

st.subheader("🏙 Revenue by City")

city = data.groupby(
    'city'
)['income'].sum().reset_index()

fig2 = px.bar(

    city,

    x='city',

    y='income',

    color='city',

    title='City Revenue Analysis'
)

fig2.update_layout(
    height=450
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# ==========================
# GRAPH 3
# ==========================

st.subheader("🛒 Favorite Product Categories")

category = data[
    'favorite_category'
].value_counts().reset_index()

category.columns = [
    'Category',
    'Count'
]

fig3 = px.pie(

    category,

    values='Count',

    names='Category',

    title='Customer Purchase Interests'
)

fig3.update_layout(
    height=500
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()

# ==========================
# GRAPH 4
# ==========================

st.subheader("📊 Customer Age Distribution")

fig4 = px.histogram(

    data,

    x='age',

    color='gender',

    nbins=20,

    title='Age Demographics'
)

fig4.update_layout(
    height=450
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.divider()

# ==========================
# GRAPH 5
# ==========================

st.subheader("📉 Customer Engagement Trend")

trend = data.groupby(
    'age'
)['monthly_visits'].mean().reset_index()

fig5 = px.line(

    trend,

    x='age',

    y='monthly_visits',

    markers=True,

    title='Age vs Engagement'
)

fig5.update_layout(
    height=450
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.divider()

# ==========================
# FINAL AI INSIGHTS
# ==========================

st.subheader("🧠 Final AI Analysis")

st.success("""
AI analysis indicates that customers
with higher income and higher spending
scores contribute significantly to
overall business revenue.
""")

st.info("""
Customers visiting frequently show
strong engagement and higher purchase
probability.
""")

st.warning("""
Businesses can improve retention by
targeting low-tenure customers with
personalized recommendations.
""")