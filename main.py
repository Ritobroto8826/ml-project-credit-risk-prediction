import streamlit as st
from prediction_helper import predict

# Set page configuration
st.set_page_config(page_title="Smart Loan Risk Assessor", layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>Jojo's Finance</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>🚀 Smart Loan Risk Assessor</h2>", unsafe_allow_html=True)
st.markdown("---")

# Row 1
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
with col2:
    income = st.number_input("Monthly Income (₹)", min_value=0, step=100000000)
with col3:
    loan_amount = st.number_input("Loan Amount (₹)", min_value=0, step=100000000)

# Row 2
col4, col5, col6 = st.columns(3)
with col4:
    loan_tenure_month = st.number_input("Loan Tenure (Months)", min_value=1, max_value=360, step=1)
with col5:
    avg_dpd_per_delinquency = st.number_input("Average Days Past Due", min_value=0, step=1)
with col6:
    delinquency_ratio = st.number_input("Delinquency Ratio", min_value=0.0, max_value=100.0, step=0.01)

# Row 3
col7, col8, col9 = st.columns(3)
with col7:
    credit_utilization_ratio = st.number_input("Credit Utilization Ratio", min_value=0.0, max_value=100.0, step=0.01)
with col8:
    open_loan_accounts = st.number_input("Open Loan Accounts", min_value=0, step=1)
with col9:
    residence_type = st.selectbox("Residence Type", ['Owned', 'Mortgage', 'Rented'])

# Row 4
col10, col11, col12 = st.columns(3)
with col10:
    loan_purpose = st.selectbox("Loan Purpose", ['Home', 'Education', 'Personal', 'Auto'])
with col11:
    loan_type = st.selectbox("Loan Type", ['Secured', 'Unsecured'])

loan_to_income_ratio = loan_amount / income if income > 0 else 0
with col12:
    st.text("Loan to income Ratio:")
    st.text(f"{loan_to_income_ratio:.2f}")

# Display input summary
st.markdown("---")
if st.button("Calculate Risk"):
    probability, credit_score, rating = predict(age,income,loan_amount,loan_tenure_month,avg_dpd_per_delinquency,delinquency_ratio,
                                                credit_utilization_ratio,open_loan_accounts,residence_type,loan_purpose,loan_type)


    st.write(f"Default Probability: {probability:.2%}")
    st.write(f"Credit Score: {credit_score}")
    st.write(f"Rating: {rating}")

