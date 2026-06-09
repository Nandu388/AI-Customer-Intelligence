import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(

    page_title="Recommendations",

    page_icon="🎁",

    layout="wide"
)

with open("assets/styles.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🎁 Smart Recommendations")

# ==========================
# LOAD DATA
# ==========================

data = pd.read_csv(
    "data/customers.csv"
)

# ==========================
# INCOME INPUT
# ==========================

st.subheader("💰 Enter Customer Income")

income = st.number_input(
    "Income",
    min_value=20000,
    max_value=150000,
    value=50000,
    step=5000
)

# ==========================
# FIND SIMILAR CUSTOMERS
# ==========================

similar_customers = data[
    (data['income'] >= income - 10000) &
    (data['income'] <= income + 10000)
]

st.divider()

# ==========================
# SHOW CUSTOMERS
# ==========================

st.subheader("👥 Similar Customers")

st.dataframe(
    similar_customers[
        [
            'name',
            'age',
            'gender',
            'city',
            'income',
            'favorite_product',
            'favorite_category'
        ]
    ].head(20),
    use_container_width=True
)

st.divider()

# ==========================
# MOST COMMON PRODUCTS
# ==========================

st.subheader("🛒 Frequently Purchased Products")

top_products = similar_customers[
    'favorite_product'
].value_counts().reset_index()

top_products.columns = [
    'Product',
    'Count'
]

fig1 = px.bar(
    top_products,
    x='Product',
    y='Count',
    color='Product',
    title='Most Frequently Purchased Products'
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.divider()

# ==========================
# CATEGORY ANALYSIS
# ==========================

st.subheader("📦 Favorite Categories")

top_categories = similar_customers[
    'favorite_category'
].value_counts().reset_index()

top_categories.columns = [
    'Category',
    'Count'
]

fig2 = px.pie(
    top_categories,
    values='Count',
    names='Category',
    title='Customer Interest Categories'
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# ==========================
# AI RECOMMENDATIONS
# ==========================

st.subheader("🎁 Recommended Products")

recommendations = top_products[
    'Product'
].head(5).tolist()

c1, c2 = st.columns(2)

for i, item in enumerate(recommendations):

    if i % 2 == 0:

        c1.success(item)

    else:

        c2.info(item)

st.divider()

# ==========================
# CUSTOMER ENGAGEMENT GRAPH
# ==========================

st.subheader("📈 Customer Engagement Analysis")

graph_df = pd.DataFrame({

    "Metric":[
        "Average Spending",
        "Average Visits",
        "Average Tenure",
        "Average Purchase Frequency"
    ],

    "Value":[
        similar_customers[
            'spending_score'
        ].mean(),

        similar_customers[
            'monthly_visits'
        ].mean(),

        similar_customers[
            'tenure'
        ].mean(),

        similar_customers[
            'purchase_frequency'
        ].mean()
    ]
})

fig3 = px.bar(
    graph_df,
    x='Metric',
    y='Value',
    color='Metric',
    title='Customer Behavior Analysis'
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()

# ==========================
# INCOME DISTRIBUTION
# ==========================

st.subheader("💰 Similar Customer Income Distribution")

fig4 = px.histogram(
    similar_customers,
    x='income',
    nbins=20,
    color='gender',
    title='Income Distribution'
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.divider()

# ==========================
# AI INSIGHTS
# ==========================

st.subheader("🤖 AI Insights")

if len(similar_customers) > 0:

    top_product = top_products.iloc[0]['Product']

    top_category = top_categories.iloc[0]['Category']

    st.success(f"""
    Customers with income around ${income}
    frequently purchase {top_product}.
    """)

    st.info(f"""
    Most popular category:
    {top_category}
    """)

    st.warning("""
    AI recommends personalized marketing
    campaigns based on customer income
    and purchasing behavior.
    """)

else:

    st.error("""
    No customers found for this income range.
    """)