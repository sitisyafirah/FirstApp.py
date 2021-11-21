import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.header("Heart Disease Prediction Analysis")
st.write("In this dataset, there are many cases  with their ASCVDs."
         
st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/sitisyafirah/FirstApp.py/main/heartRisk.csv)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep = ',')
    st.table(df)
else
    st.write("Please upload again")
         
option = st.sidebar.selectbox(
    'Select count plot'
     ['Age','Cholestrol','HDL'])

if option=='Age':
    b = sns.displot(x = 'Age', data = df, bins = 40)
    st.write(" Count vs Age")
    st.write(b)

elif option=='Cholestrol'
    c = sns.displot(x = 'Cholesterol', data = df)
    st.write(" Count vs Cholestrol")
    st.write(c)
  
elif option=='HDL'
    d = sns.displot(x = 'HDL', data = df)
    st.write("Count vs HDL")    
    st.write(d)  

else:
    st.write(df)

X = df.drop('Risk', axis = 1)
y = df['Risk']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7))

option = st.sidebar.selectbox(
    'Select a classifier',
     ['Linear Regression','Random Forest'])

if option=='Linear Regression':
    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr_pred = lr.predict(X_test)
    lr_mae = mean_absolute_error(y_test, lr_pred)
    lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
    st.write("Mean absolute error : ",lr_mae)
    st.write("Mean squared error", lr_rmse)


elif option=='Random Forest':
    from sklearn.ensemble import RandomForestRegressor
    rfr = RandomForestRegressor(n_estimators=200)
    rfr.fit(X_train, y_train)
    rfr_pred = rfr.predict(X_test)
    rfr_mae = mean_absolute_error(y_test, rfr_pred)
    rfr_rmse = np.sqrt(mean_squared_error(y_test, rfr_pred))
    st.write("Mean absolute error : ",rfr_mae)
    st.write("Mean squared error", rfr_rmse)

else:
     st.write(df)
        
