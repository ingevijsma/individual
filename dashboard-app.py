#Import streamlit
import streamlit as st

#Import required packages
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

#Insert title
st.title("Aviation and weather in the Netherlands")

#Insert text
st.markdown("""
Tekst
""")

Aviation_and_weather_in_July_and_August = pd.read_csv('Aviation and weather in July and August.csv')
Average_aviation_July_and_August_and_weather_all_year = pd.read_csv('Average aviation July and August and weather all year.csv')
Aviation_and_weather_all_year = pd.read_csv('Aviation and weather all year.csv')

#Choose page
st.sidebar.title("Select period:")
df = st.sidebar.radio(label = "", 
                       options = [Aviation_and_weather_in_July_and_August, 
                                  Average_aviation_July_and_August_and_weather_all_year, 
                                  Aviation_and_weather_all_year])

#----------
#Code voor spreidingsdiagram met keuze menu
if nav == "Histogram":  
# df = st.radio(label = "Select period:", 
#               options = [Aviation_and_weather_in_July_and_August, 
#                          Average_aviation_July_and_August_and_weather_all_year, 
#                          Aviation_and_weather_all_year])

df = pd.read_csv('ALL2.csv')
              
x = st.radio(label = "Select type of passengers:", 
             options = ['Total number of passengers (July, August)', 
                        'Total passengers arriving (July, August)', 
                        'Total passengers departing (July, August)', 
                        'Total number of passengers (July, August - All)', 
                        'Total passengers arriving (July, August - All)', 
                        'Total passengers departing (July, August - All)', 
                        'Total number of passengers (All)', 
                        'Total passengers arriving (All)', 
                        'Total passengers departing (All)'])

y = st.radio(label = "Select weather factor:", 
             options = ['TG (July, August)', 
                        'TN (July, August)', 
                        'TX (July, August)', 
                        'SQ (July, August)', 
                        'DR (July, August)', 
                        'RH (July, August)', 
                        'RHX (July, August)', 
                        'TG (July, August - All)', 
                        'TN (July, August - All)', 
                        'TX (July, August - All)', 
                        'SQ (July, August - All)', 
                        'DR (July, August - All)', 
                        'RH (July, August - All)', 
                        'RHX (July, August - All)', 
                        'TG (All)', 
                        'TN (All)', 
                        'TX (All)', 
                        'SQ (All)', 
                        'DR (All)', 
                        'RH (All)', 
                        'RHX (All)'])

fig1 = px.scatter(data_frame = df, 
                  x = x, 
                  y = y, 
                  trendline = 'ols', 
                  trendline_scope = 'trace', 
                  title = 'Number of passengers (arriving/departing) versus weather factors')

st.plotly_chart(fig1)
