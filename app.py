import streamlit as st
st.set_page_config(
    page_title="Amazon Sales ML Suite",
    page_icon="📦",
    layout="wide"
)
st.image("https://etimg.etb2bimg.com/photo/114184053.cms")

# Custom CSS
st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:#1E88E5;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:gray;
}

.feature-box{
    padding:20px;
    border-radius:15px;
    background-color:#f5f5f5;
    text-align:center;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<p class="main-title">📦 Amazon Sales Analytics Suite</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Machine Learning & Data Analytics Dashboard</p>',
    unsafe_allow_html=True
)

st.divider()

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Projects", "6")

with col2:
    st.metric("ML Models", "4")

with col3:
    st.metric("Dataset", "Amazon Sales")

st.divider()

st.subheader("🚀 Explore Modules")

col1, col2 = st.columns(2)

with col1:

    st.page_link(
        "pages/1_Dashboard.py",
        label=" Dashboard",
        icon="📊"
    )

    st.page_link(
        "pages/2_Amount_Prediction.py",
        label=" Amount Prediction",
        icon="💰"
    )

    st.page_link(
        "pages/3_Order_Status_Prediction.py",
        label=" Order Status",
        icon="🚚"
    )

with col2:

    st.page_link(
        "pages/4_Cancellation_Prediction.py",
        label=" Cancellation Prediction",
        icon="🚫"
    )

    st.page_link(
        "pages/5_Customer.py",
        label=" Customer Segmentation",
        icon="👥"
    )

    st.page_link(
        "pages/6_Sales_forecasting.py",
        label=" Sales Forecasting",
        icon="📈"
    )

st.divider()

st.info("""
This project demonstrates:
- Data Analysis
- Machine Learning
- Customer Segmentation
- Sales Forecasting
- Interactive Streamlit Dashboard
""")
