import streamlit as st
import pandas as pd
import pickle

# Load the trained model (adjust path for Streamlit environment)
model = pickle.load(open(r'C:\Users\gopin\Downloads\Loan Prediction.pkl', 'rb'))


# Function to make predictions
def predict_loan(features):
    columns = ["Gender", "Married", "Dependents", "Education", "Self_Employed",
               "ApplicantIncome", "CoapplicantIncome", "LoanAmount", 
               "Loan_Amount_Term", "Credit_History", "Property_Area"]
    features_df = pd.DataFrame([features], columns=columns)
    return model.predict(features_df)[0]

# Title of the app
st.title("Loan Approval Prediction App")

# Header for user inputs
st.header("Provide the following details:")

# Input fields for each feature
Gender = st.selectbox("Gender", [0, 1], help="0 = Female, 1 = Male")
Married = st.selectbox("Married", [0, 1], help="0 = No, 1 = Yes")
Dependents = st.selectbox("Dependents", [0, 1, 2, 3], help="0 = '0', 1 = '1', 2 = '2', 3 = '3+")
Education = st.selectbox("Education", [0, 1], help="0 = Graduate, 1 = Not Graduate")
Self_Employed = st.selectbox("Self Employed", [0, 1], help="0 = No, 1 = Yes")
ApplicantIncome = st.number_input("Applicant Income", min_value=0)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
LoanAmount = st.number_input("Loan Amount", min_value=0)
Loan_Amount_Term = st.number_input("Loan Amount Term", min_value=0)
Credit_History = st.selectbox("Credit History", [0, 1], help="0 = No, 1 = Yes")
Property_Area = st.selectbox("Property Area", [0, 1, 2], help="0 = Urban, 1 = Semiurban, 2 = Rural")

# Button for prediction
if st.button("Predict"):
    features = [Gender, Married, Dependents, Education, Self_Employed, 
                ApplicantIncome, CoapplicantIncome, LoanAmount, 
                Loan_Amount_Term, Credit_History, Property_Area]
    prediction = predict_loan(features)
    if prediction == 1:
        st.success("Loan Approved!")
    else:
        st.error("Loan Not Approved.")
