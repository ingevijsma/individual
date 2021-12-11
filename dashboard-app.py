#Importeer streamlit
import streamlit as st

#Importeer de benodigde packages
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
import plotly.express as px
#import plotly.graph_objects as go
#import statsmodels.api as sm
import seaborn as sns

#Titel toevoegen
st.title("Aviation and weather in the Netherlands")

#Tekst toevoegen
st.markdown("""
Tekst
""")

#----------
#Code voor spreidingsdiagram met keuze menu

#Tekst toevoegen
st.markdown("""
Tekst
""")

Aviation_and_weather_in_July_and_August = pd.read_csv('Aviation and weather in July and August.csv')
Average_aviation_July_and_August_and_weather_all_year = pd.read_csv('Average aviation July and August and weather all year.csv')
Aviation_and_weather_all_year = pd.read_csv('Aviation and weather all year.csv')
  
df = st.radio(label = "Select period:", 
              options = [Aviation_and_weather_in_July_and_August, 
                         Average_aviation_July_and_August_and_weather_all_year, 
                         Aviation_and_weather_all_year]
              
x = st.radio(label = "Select type of passengers:", 
             options = ['Total number of passengers', 
                        'Total passengers arriving', 
                        'Total passengers departing']

y = st.radio(label = "Select weather factor:", 
             options = ['TG', 
                        'TN', 
                        'TX', 
                        'SQ', 
                        'DR', 
                        'RH', 
                        'RHX'])

fig1 = px.scatter(df = df, 
                  x = x, 
                  y = y, 
                  hover_name = 'Periods', 
                  labels = {'variable': 'Weather factor', 'value': 'Value'}, 
                  opacity = 0.8,
                  trendline = 'ols', 
                  trendline_scope = 'trace', 
                  log_y = True, 
                  title = 'Number of passengers (arriving/departing) versus the three main weather factors')

st.plotly_chart(fig1)
