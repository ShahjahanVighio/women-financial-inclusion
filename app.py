import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# 1. PAGE SETUP
# ---------------------------------------------------------
st.set_page_config(page_title="Financial Inclusion Dashboard", layout="wide")
st.title("📊 Women Financial Inclusion & Alternative Credit Scoring")
st.write("A Business Analytics Dashboard exploring digital lending access and barriers.")

# ---------------------------------------------------------
# 2. LOAD THE DATA
# ---------------------------------------------------------
@st.cache_data
def load_data():
    # Reads the converted data.csv file
    df = pd.read_csv("data.csv")
    return df

# Load the dataframe
df = load_data()

# ---------------------------------------------------------
# 3. SIDEBAR FILTERS
# ---------------------------------------------------------
st.sidebar.header("Filter the Data")

# Create a dropdown to filter by Area of Residence (Urban, Semi-urban, Rural)
residence_options = df["4. Area of Residence"].unique()
selected_residence = st.sidebar.multiselect(
    "Select Area of Residence:", 
    options=residence_options, 
    default=residence_options
)

# Apply the filter to our dataframe
filtered_df = df[df["4. Area of Residence"].isin(selected_residence)]

# ---------------------------------------------------------
# 4. KEY METRICS (Top Row)
# ---------------------------------------------------------
# Create 3 columns for big numbers at the top
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Responses", len(filtered_df))

with col2:
    # Count how many said "Yes" to having a bank account
    bank_acc_yes = len(filtered_df[filtered_df["5. Do you have a bank account?"] == "Yes"])
    st.metric("Have Bank Account", f"{bank_acc_yes}")

with col3:
    # Count how many have used a mobile loan app
    used_app_yes = len(filtered_df[filtered_df["8. Have you ever used a mobile loan app (digital lending app)?"] == "Yes"])
    st.metric("Used Mobile Loan App", f"{used_app_yes}")

st.divider() # Adds a nice horizontal divider line

# ---------------------------------------------------------
# 5. VISUALIZATIONS (Charts)
# ---------------------------------------------------------
# Create a 2-column layout for our charts
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Demographics: Age Group")
    # Group data by Age Group
    age_counts = filtered_df["1. Age Group"].value_counts().reset_index()
    age_counts.columns = ["Age Group", "Count"]
    
    # Create a Bar Chart using Plotly
    fig_age = px.bar(
        age_counts, 
        x="Age Group", 
        y="Count", 
        color="Age Group", 
        title="Respondents by Age Group"
    )
    st.plotly_chart(fig_age, use_container_width=True)

with chart_col2:
    st.subheader("Biggest Barrier to Getting Loans")
    # Group data by the biggest barrier question
    barrier_counts = filtered_df["14. What is the biggest barrier for women to get loans?"].value_counts().reset_index()
    barrier_counts.columns = ["Barrier", "Count"]
    
    # Create a Pie Chart using Plotly
    fig_barrier = px.pie(
        barrier_counts, 
        names="Barrier", 
        values="Count", 
        title="Perceived Barriers for Women", 
        hole=0.3
    )
    st.plotly_chart(fig_barrier, use_container_width=True)

# ---------------------------------------------------------
# 6. RAW DATA VIEW (Bottom)
# ---------------------------------------------------------
st.subheader("Raw Survey Data")
# Allow users to check a box to see the raw table
if st.checkbox("Show raw data"):
    st.dataframe(filtered_df)