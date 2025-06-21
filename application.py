import streamlit as st
import pandas as pd
import joblib

df = pd.read_csv("salaryData.csv")
st.title("Salary predictor 🔮")
# Displays Salary predictor in a title format
st.write("Hi, welcome...do you want to know your estimated monthly salary? Let's start😊🤗")
# This line of code write arguments to our app

first_name = st.text_input("First Name")
last_name = st.text_input("Last name")
# These two lines allow the user to input his/her information
gender = st.selectbox("Gender", ["Male", "Female"])# This line displays a box with gender option to choose
age = st.number_input("Your age", 20, 75, 30, 1)
# This line allows the user to input his age. The minimum age is 20 and max_age is 75. The default age is 30 and the difference between ages is 1
marital_status = st.pills("Marital status", ["Single", "Married" ,"Divorced"])
# This line allows a single select option
level_of_studies = st.selectbox("Level of studies", ["Bachelor", "Master", "PhD"])
# This displays a box with study level options
years_of_experience = st.slider("Years of experience", 0.0, 25.0, step=0.5)
# This display a slider to select the years of experience in the range 0-25
job_titles = sorted(df["Job Title"].dropna().unique())
job_title = st.selectbox("Job title", job_titles)
# Job tiltes are extracted from the csv file then creates a dropdown menu of job titles
model, model_columns = joblib.load('salary_predictor_model.pkl')
# Loads salary predictor model 
inputs = pd.DataFrame([{"Age": age,"Gender": gender,"Education Level": level_of_studies,"Job Title": job_title,"Years of Experience": years_of_experience}])
# User data uses same frame as the training data
data = pd.concat([inputs,df], axis=0)
# inputs row is combined with original dataset
data_converted = pd.get_dummies(data, columns=["Gender", "Education Level", "Job Title"], drop_first=True)
# Categorical features are converted into numerical
inputs_converted = data_converted.iloc[0:1]
# Select converted user input row to feed into the model

for col in model_columns:
    if col not in inputs_converted:
       inputs_converted[col] = 0
# Checks if the user inputs all features present in the training data set
inputs_converted = inputs_converted[model_columns]
# Update the model columns

currency_rates = {"INR": 1, "USD": 0.012, "EUR": 0.01, "KES": 1.51, "JPY":1.69, "GBP":0.0086 ,"AUD":0.018 , "CAD":0.016}
currency = st.selectbox("Choose your preferred currency", list(currency_rates.keys()))

if st.button("Generate the output"):
# This line displays a buttosn 
    monthly_estimated_salary_in_INR =model.predict(inputs_converted)[0]
    converted_salary =  monthly_estimated_salary_in_INR * currency_rates[currency]

    st.write(f"The monthly salary is estimated to: **{converted_salary:.4f}{currency}**")

st.markdown("---")
st.markdown(
    """
<style>
.stApp{
    background-color: #fff8dc;
}
</style>
""",
unsafe_allow_html=True
)
st.badge("⭐ Enjoyed the experience? We'd love to hear your feedback!💖")
# displays a small colored badge
feedback = st.feedback("stars")
# displays stars for rating
if st.button("Submit Feedback"):
    st.write ("Made with love❤️ and care🤗 by team SKYSHIELD")
