import streamlit as st
import pandas as pd
import numpy as np

# Set page title and icon
st.set_page_config(page_title="Streamlit Quick Demo", page_icon="🌟")

# Page title
st.title("🎉 Streamlit Quick Demo")

# Input box
name = st.text_input("Please enter your name:", "")

# Display input content
if name:
    st.write(f"👋 Hello, {name}!")

# Slider
age = st.slider("Please select your age:", 0, 100, 25)

# Display slider value
st.write(f"🧓 Your age is: {age}")

# Data table
st.subheader("📊 Data Table Display")
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["Column 1", "Column 2", "Column 3"]
)
st.dataframe(data)

# Chart
st.subheader("📈 Line Chart")
st.line_chart(data)

# Sidebar
st.sidebar.header("Sidebar Options")
selected_option = st.sidebar.selectbox(
    "Select an option:",
    ["Option 1", "Option 2", "Option 3"]
)

st.sidebar.write(f"You selected: {selected_option}")

# File upload
st.subheader("📂 File Upload")
uploaded_file = st.file_uploader("Upload file:", type=["csv", "txt"])

if uploaded_file is not None:
    file_data = pd.read_csv(uploaded_file)
    st.write("File content:")
    st.dataframe(file_data)