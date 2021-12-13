#Import streamlit
import streamlit as st

#Import required packages
import pandas as pd
import plotly.express as px
import statsmodels.api as sm

#Insert title
st.title('Aviation and weather in the Netherlands')

#Upload dataframe
df = pd.read_csv('ALL2.csv')

#Make three lists for different periods
july_august = ['Total number of passengers (July, August)', 
	       'Total passengers arriving (July, August)', 
	       'Total passengers departing (July, August)', 
	       'TG (July, August)', 
	       'TN (July, August)', 
	       'TX (July, August)', 
	       'SQ (July, August)', 
	       'DR (July, August)', 
	       'RH (July, August)', 
	       'RHX (July, August)']

july_august_all = ['Total number of passengers (July, August - All)', 
		   'Total passengers arriving (July, August - All)', 
		   'Total passengers departing (July, August - All)', 
		   'TG (July, August - All)', 
		   'TN (July, August - All)', 
		   'TX (July, August - All)', 
		   'SQ (July, August - All)', 
		   'DR (July, August - All)', 
		   'RH (July, August - All)', 
		   'RHX (July, August - All)']

all = ['Total number of passengers (All)', 
       'Total passengers arriving (All)', 
       'Total passengers departing (All)', 
       'TG (All)', 
       'TN (All)', 
       'TX (All)', 
       'SQ (All)', 
       'DR (All)', 
       'RH (All)', 
       'RHX (All)']

#Make selectbox of the different periods
period = st.selectbox(label = 'Select period:', 
		      options = [july_august, july_august_all, all], 
		      help = 'Tekst')

#--------------------
# Aviation_and_weather_in_July_and_August = pd.read_csv('Aviation and weather in July and August.csv')
# Average_aviation_July_and_August_and_weather_all_year = pd.read_csv('Average aviation July and August and weather all year.csv')
# Aviation_and_weather_all_year = pd.read_csv('Aviation and weather all year.csv')

#Scatterplot code
# df = st.radio(label = "Select period:", 
#               options = [Aviation_and_weather_in_July_and_August, 
#                          Average_aviation_July_and_August_and_weather_all_year, 
#                          Aviation_and_weather_all_year])
#--------------------
              
if period == july_august:	
	x = st.radio(label = "Select type of passengers:", 
		     options = ['Total number of passengers (July, August)', 
				'Total passengers arriving (July, August)', 
				'Total passengers departing (July, August)'], 
		     help = 'Tekst')

	y = st.multiselect(label = "Select weather factor:", 
			   options = ['SQ (July, August)', 'TX (July, August)', 'TG (July, August)'], 
			   help = 'Tekst')

if period == july_august_all:	
	x = st.radio(label = "Select type of passengers:", 
		     options = ['Total number of passengers (July, August - All)', 
				'Total passengers arriving (July, August - All)', 
				'Total passengers departing (July, August - All)'], 
		     help = 'Tekst')

	y = st.multiselect(label = "Select weather factor:", 
			   options = ['SQ (July, August - All)', 'TX (July, August - All)', 'TG (July, August - All)'], 
			   help = 'Tekst')

if period == all:	
	x = st.radio(label = "Select type of passengers:", 
		     options = ['Total number of passengers (All)', 
				'Total passengers arriving (All)', 
				'Total passengers departing (All)'], 
		     help = 'Tekst')

	y = st.multiselect(label = "Select weather factor:", 
			   options = ['TX (All)', 'TG (All)', 'TN (All)'], 
			   help = 'Tekst')

st.markdown('***')
st.markdown("<h3 style='text-align: center; color: black;'>Number of passengers (arriving/departing) versus weather factors</h3>", unsafe_allow_html = True)
st.markdown('***')

fig_scatterplot_trendline = st.checkbox('Trendline', value = False)
if fig_scatterplot_trendline == True:
  fig1 = px.scatter(data_frame = df, 
                    x = x, 
                    y = y, 
                    trendline = 'ols', 
                    trendline_scope = 'trace')
  
if fig_scatterplot_trendline == False:
  fig1 = px.scatter(data_frame = df, 
                    x = x, 
                    y = y)

st.plotly_chart(fig1)

with st.expander('More information:'):
	st.subheader('Tekst')
	st.markdown('''Tekst''')
