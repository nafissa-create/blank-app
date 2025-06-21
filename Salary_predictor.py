import pandas as pd
# We import pandas to load our data

df = pd.read_csv("salaryData.csv")
# We read our csvfile

print(df.describe())
# Summary statistics
## OUTPUT
#       Age             Years of Experience                 Salary
#count  373.000000           373.000000     373.000000
#mean    37.431635            10.030831  100577.345845
#std      7.069073             6.557007   48240.013482
#min     23.000000             0.000000     350.000000
#25%     31.000000             4.000000   55000.000000
#50%     36.000000             9.000000   95000.000000
#75%     44.000000            15.000000  140000.000000
#max     53.000000            25.000000  250000.000000

print(df.isnull().sum())
# check for missing values their number
## OUTPUT
#Age                    2
#Gender                 2
#Education Level        2
#Job Title              2
#Years of Experience    2
#Salary                 2
## There are two missing values for each feature in our dataset

df.dropna(inplace=True)
<<<<<<< HEAD
# The missing values are removed
=======
# The rows with missing values are removed
>>>>>>> 78f5274a9d7ac19ef865af13fa3f0a6b93ac8abb

df_converted = pd.get_dummies(df, columns=["Gender", "Education Level", "Job Title"], drop_first=True)
# We converte categorical features into numbers
# This line of code looks at the original dataframe(df) then finds the listed colums and replace them with numeric columns(0 or 1)
x = df_converted.drop("Salary", axis=1)
# x takes the new dataframe with all features in our dataset except salary 
# axis=1 specify that we drop a column
y = df_converted["Salary"]
# y represent the value that we want to predict which is the 

from sklearn.model_selection import train_test_split
# Split our dataset into two sets (one for training and another one for testing)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=20)
# 70% of our dataset is used for training and 30% used for testing
# Setting random_state to a fixed constant helps us get the same sets every time the dataset is shuffled

from sklearn.ensemble import RandomForestRegressor
# import a machine learning model (RandomForestRegressor that creates decision trees to make prediction)
model = RandomForestRegressor(n_estimators=75, random_state=20)
# The model create 75 trees 
# Setting random_state to 20 helps get the same result every time
model.fit(x_train,y_train)
# The model learns how x_train (features in our dataset except salary) relates to y_train(salary)
y_predictor = model.predict(x_test)
# The model predicts salaries (y_salaries) for the testing set (x_test)

from sklearn.metrics import r2_score
# Metrics are used to evaluate model performance
print(r2_score(y_test, y_predictor))
# Determine the quality of prediction 
## OUTPUT = 0.9116655427773879 which is close to 1. Our prediction model is good

import joblib
# Save our Salary predictor model
joblib.dump((model, x.columns), 'salary_predictor_model.pkl')
# Saves our model in a file named salary_predictor_model.pkl