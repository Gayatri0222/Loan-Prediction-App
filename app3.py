import streamlit as st
import numpy as np
import joblib


st.set_page_config(
    page_title="Loan Status Predictor 💸",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)



model = joblib.load(open('loan_model.pkl', 'rb'))


st.title("Loan Status Prediction App")
st.subheader("Enter the applicant details to predict Loan Approval Status")

age = st.number_input('Age', min_value=18, max_value=100, value=25)
gender = st.selectbox('Gender', ['male', 'female'])
education = st.selectbox('Education Level', ['High School', 'Bachelor', 'Master'])
income = st.number_input('Annual Income', min_value=0, value=50000)
emp_exp = st.number_input('Employment Experience (years)', min_value=0, max_value=50, value=2)
home_ownership = st.selectbox('Home Ownership', ['RENT', 'OWN', 'MORTGAGE', 'OTHER'])
loan_amount = st.number_input('Loan Amount', min_value=500, value=10000)
loan_intent = st.selectbox('Loan Purpose', ['EDUCATION', 'MEDICAL', 'VENTURE', 'PERSONAL', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION'])
interest_rate = st.number_input('Loan Interest Rate (%)', min_value=0.0, value=10.0)
loan_percent_income = st.number_input('Loan % of Income (0-1)', min_value=0.0, max_value=1.0, value=0.2)
credit_length = st.number_input('Credit History Length (years)', min_value=0, value=3)
credit_score = st.number_input('Credit Score', min_value=300, max_value=850, value=600)
previous_defaults = st.selectbox('Previous Loan Defaults on File', ['Yes', 'No'])

def map_inputs():
    gender_map = {'female': 0, 'male': 1}
    education_map = {'High School': 0, 'Bachelor': 1, 'Master': 2}
    home_map = {'RENT': 0, 'OWN': 1, 'MORTGAGE': 2, 'OTHER': 3}
    intent_map = {'EDUCATION': 0, 'MEDICAL': 1, 'VENTURE': 2, 'PERSONAL': 3, 'HOMEIMPROVEMENT': 4, 'DEBTCONSOLIDATION': 5}
    default_map = {'No': 0, 'Yes': 1}

    return [
        age,
        gender_map[gender],
        education_map[education],
        income,
        emp_exp,
        home_map[home_ownership],
        loan_amount,
        intent_map[loan_intent],
        interest_rate,
        loan_percent_income,
        credit_length,
        credit_score,
        default_map[previous_defaults]
    ]


if st.button('Predict Loan Status'):
    input_data = np.array([map_inputs()])
    prediction = model.predict(input_data)[0]
    result = "Approved" if prediction == 1 else "Rejected"
    st.success(f"Prediction Result: {result}")
