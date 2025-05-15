import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Sales Dashboard")
st.write("Analyze trends and insights for continuous improvement.")

# Sample Sales Data
data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Revenue": [500, 700, 1200, 1500, 1800]
})

# Sales Line Chart
fig = px.line(data, x="Month", y="Revenue", title="Monthly Revenue Growth")
st.plotly_chart(fig)
