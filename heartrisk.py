import streamlit as st
import numpy as np
import pandas as pd
import datetime
import math

st.header("My first Streamlit App")
st.title("Let's Count")
st.write('Before you continue, please read the [terms and conditions](I promise to stay healthy everyday')
show = st.checkbox('I agree the terms and conditions')
if show:
    st.write('Welcome to Lets Count')

option = st.sidebar.selectbox('Select one symbol', ( 'CALENDAR', 'BMI CALCULATOR','CALORIE CALCULATOR'))

if option=='CALENDAR':
    today = datetime.date.today()
    start_date = st.date_input('Start date', today)
    st.write(start_date)

#BMI CALCULATOR

elif option=='BMI CALCULATOR':
      height = st.number_input("Enter your height in m: ")
      weight = st.number_input("Enter your weight in kg: ")
	
      BMI = weight/((height)**2)
      st.write('Your BMi is: ',BMI)
      if BMI <= 18.5:
      	st.write("You are underweight.")
      elif BMI <= 24.9:
      	st.write("You are healthy.")
      elif BMI <= 29.9:
      	st.write("You are overweight.")
      else:
      	st.write("You are obese.")
      
elif option=='CALORIE CALCULATOR':
      #def user_info():
       age = st.number_input("What is your age: ")
       gender = st.text_input("What is your gender (male/female): ")
       weight = st.number_input("What is your weight: ")
       height = st.number_input("What is your height in inches: ")
       bmr_result = float(bmr_result)
       if gender == 'male':
          bmr_result = 66 + (6.2*height) + (12.7*weight) - (6.76*age)
	
       elif gender == 'female':
	  bmr_result = 655.1+(4.35*height)+(4.7*weight)-(4.7*age)
        #BMR = 665 + (9.6 X 69) + (1.8 x 178) – (4.7 x 27)
       

    #def calculate_activity(bmr_result): 
       activity_level = st.text_input("What is your activity level (none, light, moderate, heavy, or extreme): ")
       
       if activity_level == 'none':
            activity_level = 1.2 * bmr_result
       elif activity_level == 'light':
            activity_level = 1.375 * bmr_result
       elif activity_level == 'moderate':
            activity_level = 1.55 * bmr_result
       elif activity_level == 'heavy':
            activity_level = 1.725 * bmr_result
       elif activity_level == 'extreme':
            activity_level = 1.9 * bmr_result

    	#return(int(activity_level))

     #def gain_or_lose(activity_level):
       goals = st.text_input("Do you want to lose, maintain, or gain weight: ")

       if goals == 'lose':
           calories = activity_level - 500
           st.write('in order to ', goals, 'weight, your daily caloric goals should be', calories, '!')
       elif goals == 'maintain':
           calories = activity_level
            st.write('in order to ', goals, 'weight, your daily caloric goals should be', calories, '!')
       elif goals == 'gain':
           gain = st.text_input("Gain 1 or 2 pounds per week? Enter 1 or 2: ")
      	
       if gain == 1: 
           calories = activity_level + 500
           st.write('in order to ', goals, 'weight, your daily caloric goals should be', calories, '!')
       elif gain == 2:
           calories = activity_level + 1000
	   st.write('in order to ', goals, 'weight, your daily caloric goals should be', calories, '!')

       #st.write('in order to ', goals, 'weight, your daily caloric goals should be', calories, '!')
		#gain_or_lose(calculate_activity(user_info()))
