import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Setup app
st.set_page_config(
    page_title="💽 Data Sweeper",
    layout="wide",
)

# Title with Icon
st.markdown("## 💽 Swift Data Formatter 🔄")
st.write("Seamlessly switch between CSV and Excel formats while benefiting from built-in data cleaning and visualization tools.")

# File Uploader
uploaded_files = st.file_uploader("📂 **Upload your files (CSV or Excel)**", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"❌ Unsupported file type: {file_ext}")
            continue
        
        # Display File Details
        st.subheader("📁 File Details")
        st.write(f"**📝 File Name:** {file.name}")
        st.write(f"**📦 File Size:** {file.size / 1024:.2f} KB")

        # Display First Few Rows of Data
        st.subheader("🔍 Data Preview")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("🧹 Data Cleaning Options")
        if st.checkbox(f"✨ Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"🗑️ Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("✅ Removed duplicates successfully!")

            with col2:
                if st.button(f"🛠️ Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("✅ Missing values filled successfully!")

        # Column Selection for Conversion
        st.subheader("📊 Select Columns to Convert")
        columns = st.multiselect(f"📝 Select columns to convert for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Data Visualization (Converted to Bar Chart)
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"📈 Show Visualization for {file.name}"):
            numeric_data = df.select_dtypes(include=["number"])
            if numeric_data.shape[1] >= 1:  # Ensure at least one numeric column exists
                st.bar_chart(numeric_data.iloc[:, :2])  # Changed from Line Chart to Bar Chart
            else:
                st.warning(f"⚠️ No numeric columns available for visualization in {file.name}")

        # File Conversion
        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"📝 Convert {file.name} to", ["CSV", "Excel"], key=file.name)
        
        buffer = BytesIO()
        file_name = file.name.replace(file_ext, f".{conversion_type.lower()}")

        if conversion_type == "CSV":
            df.to_csv(buffer, index=False)
            mime_type = "text/csv"
        elif conversion_type == "Excel":
            df.to_excel(buffer, index=False, engine="openpyxl")
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        buffer.seek(0)

        st.download_button(
            label=f"⬇️ Download {file.name} as {conversion_type}",
            data=buffer,
            file_name=file_name,
            mime=mime_type
        )

        st.success(f"🎉 Successfully converted {file.name} to {conversion_type}!")
