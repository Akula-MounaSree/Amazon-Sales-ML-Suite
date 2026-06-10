import pandas as pd
import streamlit as st
import plotly.express as px
st.title("Sales Dashboard")
st.image("https://eu-central-1-enterprise-euc1.graphassets.com/AAg7wOEyuSfq2w8Bzgd1Xz/qDzTq7U6SfeMqXMaTy9I")
df=pd.read_csv("Amazon Sale Report.csv.gz", low_memory=False)
df['Amount']=pd.to_numeric(df['Amount'], errors='coerce')
st.subheader("Sales by Category")
st.metric("Total Orders", len(df))
st.metric("Total Revenue", f"₹{df['Amount'].sum():,.0f}")
category_sales=df.groupby('Category')['Amount'].sum().reset_index()
fig=px.bar(category_sales, x='Category', y='Amount', title="Sales by Category", labels={'Amount':'Total Sales (₹)'})
st.plotly_chart(fig, use_container_width=True)
