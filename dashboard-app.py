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
  
df = st.radio(label = "Select period", options = [
y = st.radio(label = "Kies gewenste activiteit:", 
             options = ["Totaal aantal vluchten", "Totaal aantal aangekomen vluchten", "Totaal aantal vertrokken vluchten", "Totaal aantal passagiers", 
                          "Totaal aantal aangekomen passagiers", "Totaal aantal vertrokken passagiers"])
  
data1 = pd.read_csv('data_streamlit.csv')

fig1 = px.scatter(df = aw_year_month, 
                  x = 'Total passengers departing', 
                  y = ['SQ', 'TX', 'TG'], 
                  hover_name = 'Periods', 
                  labels = {'variable': 'Weather factor', 'value': 'Value'}, 
                  opacity = 0.8,
                  trendline = 'ols', 
                  trendline_scope = 'trace', 
                  log_y = True, 
                  title = 'Number of passengers (arriving/departing) versus the three main weather factors')

st.plotly_chart(fig1)
