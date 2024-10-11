# Loan Approval Prediction App

## Description
The Loan Approval Prediction App is a web application that predicts whether a loan application will be approved based on various input features. This app utilizes machine learning algorithms to analyze applicant data and provide instant predictions.

## Features
- User-friendly interface to input loan application details.
- Predicts loan approval status (Approved/Not Approved).
- Built with Streamlit for an interactive web experience.
- Trained model using XGBoost for efficient and accurate predictions.

## Technologies Used
- **Python**: Programming language used for building the app.
- **Streamlit**: Framework for creating the web application.
- **XGBoost**: Machine learning library used for model training.
- **Pandas**: Data manipulation and analysis library.
- **Scikit-learn**: For model evaluation and validation.

## How to Use the App
1. Enter the following details:
   - Gender (0 = Female, 1 = Male)
   - Married (0 = No, 1 = Yes)
   - Dependents (0, 1, 2, 3+)
   - Education (0 = Graduate, 1 = Not Graduate)
   - Self Employed (0 = No, 1 = Yes)
   - Applicant Income (enter amount)
   - Coapplicant Income (enter amount)
   - Loan Amount (enter amount)
   - Loan Amount Term (in months)
   - Credit History (0 = No, 1 = Yes)
   - Property Area (0 = Urban, 1 = Semiurban, 2 = Rural)
   
2. Click the **Predict** button to see the result.

   git clone https://github.com/Gopinathd1/loan-prediction-app.git
   cd loan-prediction-app
