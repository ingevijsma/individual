#Import streamlit
import streamlit as st

#Import required packages
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import plotly.graph_objects as go

#Set up page configuration
st.set_page_config(layout = 'wide')

#Insert title and subheader
st.title('Aviation and Weather in the Netherlands')

#Set up columns
col1, col2 = st.columns(2)
col1.subheader('From 2000 to 2019')

#Insert warning
col1.write("*Disclaimer: The years 2020 and 2021 are excluded due to the COVID-19 pandemic!*")

#Insert information
col1.write("""
Three different studies:\n
1. **Summer holiday period**: Investigate whether the weather during the summer influences the behaviour of (arriving/departing) (holiday) passengers during the summer period.\n
2. **Aviation during the summer holiday period and weather during the year**: Investigate whether the weather during the year influences the behaviour of (arriving/departing) (early booking) (holiday) passengers in the summer period.\n 
3. **Year-round aviation and weather**: Investigate whether the weather during the year influences the behaviour of (arriving/departing) passengers all year round.\n
""")

#Upload dataframe
df = pd.read_csv('STREAMLIT.csv')

#Make selectbox of the different studies
period = col1.selectbox(label = 'Select study:', 
			options = ['Study 1', 'Study 2', 'Study 3'], 
			help = 'Select the desired study here. Study 1 examines only the months of July and August. Study 2 examines only the months of July and August for aviation and the entire year for weather factors. Study 3 examines the entire year.')

#Make three lists for different studies
if period == 'Study 1':
	july_august = ['Total number of passengers (1)', 
		       'Total passengers arriving (1)', 
		       'Total passengers departing (1)', 
		       'TG (1)', 
		       'TN (1)', 
		       'TX (1)', 
		       'SQ (1)', 
		       'DR (1)', 
		       'RH (1)', 
		       'RHX (1)']

if period == 'Study 2':
	july_august_all = ['Total number of passengers (2)', 
			   'Total passengers arriving (2)', 
			   'Total passengers departing (2)', 
			   'TG (2)', 
			   'TN (2)', 
			   'TX (2)', 
			   'SQ (2)', 
			   'DR (2)', 
			   'RH (2)', 
			   'RHX (2)']

if period == 'Study 3':
	all = ['Total number of passengers (3)', 
	       'Total passengers arriving (3)', 
	       'Total passengers departing (3)', 
	       'TG (3)', 
	       'TN (3)', 
	       'TX (3)', 
	       'SQ (3)', 
	       'DR (3)', 
	       'RH (3)', 
	       'RHX (3)']
       
#Make radio and multiselect per study for different types of passengers and weather factors, respectively
if period == 'Study 1':	
	x = col1.radio(label = "Select type of passengers:", 
		       options = ['Total number of passengers (1)', 
				  'Total passengers arriving (1)', 
				  'Total passengers departing (1)'], 
		       help = 'Select the desired type of passenger here. Option 1 is both arriving and departing. Option 2 is arriving only and option 3 is departing only.')

	y = col1.multiselect(label = "Select weather factor(s):", 
			     options = ['SQ (1)', 'TX (1)', 'RHX (1)', 'TG (1)', 'RH (1)'], 
			     help = 'Select the desired weather factor(s) here. Previous research has determined the five most important weather factors related to passenger volume. These weather factors are listed in order from left to right in the multiselect and from top to bottom in the legend to the figure in terms of importance.')

if period == 'Study 2':	
	x = col1.radio(label = "Select type of passengers:", 
		       options = ['Total number of passengers (2)', 
				  'Total passengers arriving (2)', 
				  'Total passengers departing (2)'], 
		       help = 'Select the desired type of passenger here. Option 1 is both arriving and departing. Option 2 is arriving only and option 3 is departing only.')

	y = col1.multiselect(label = "Select weather factor(s):", 
			     options = ['SQ (2)', 'TX (2)', 'TG (2)', 'RH (2)', 'RHX (2)'], 
			     help = 'Select the desired weather factor(s) here. Previous research has determined the five most important weather factors related to passenger volume. These weather factors are listed in order from left to right in the multiselect and from top to bottom in the legend to the figure in terms of importance.')

if period == 'Study 3':	
	x = col1.radio(label = "Select type of passengers:", 
		       options = ['Total number of passengers (3)', 
				  'Total passengers arriving (3)', 
				  'Total passengers departing (3)'], 
		       help = 'Select the desired type of passenger here. Option 1 is both arriving and departing. Option 2 is arriving only and option 3 is departing only.')

	y = col1.multiselect(label = "Select weather factor(s):", 
			     options = ['TX (3)', 'TG (3)', 'TN (3)', 'SQ (3)', 'DR (3)'],
			     help = 'Select the desired weather factor(s) here. Previous research has determined the five most important weather factors related to passenger volume. These weather factors are listed in order from left to right in the multiselect and from top to bottom in the legend to the figure in terms of importance.')

#Code scatterplot with and without trendline
fig_scatterplot_trendline = col2.checkbox('Trendline', value = False)
if fig_scatterplot_trendline == True:
  fig1 = px.scatter(data_frame = df, 
                    x = x, 
                    y = y, 
		    labels = {'value': 'Value'}, 
		    color_discrete_sequence = ['#5CB9FF', '#9372FF', '#7EFF72', '#FF5CB7', '#F2FF28'],
                    trendline = 'ols', 
                    trendline_scope = 'trace', 
		    log_y = True, 
		    title = 'Number of passengers (arriving/departing) versus weather factors')
  
if fig_scatterplot_trendline == False:
  fig1 = px.scatter(data_frame = df, 
                    x = x, 
                    y = y, 
		    labels = {'value': 'Value'}, 
		    color_discrete_sequence = ['#5CB9FF', '#9372FF', '#7EFF72', '#FF5CB7', '#F2FF28'],
		    log_y = True, 
		    title = 'Number of passengers (arriving/departing) versus weather factors')

col2.plotly_chart(fig1)

#Insert expander
with col2.expander('Abbreviation of weather factors with units:'):
	st.write("""**TG** = Daily mean temperature (in degrees Celsius)\n
**TN** = Minimum temperature (in degrees Celsius)\n
**TX** = Maximum temperature (in degrees Celsius)\n
**SQ** = Sunshine duration (in hours)\n
**DR** = Precipitation duration (in hours)\n
**RH** = Daily precipitation amount (in mm)\n
**RHX** = Maximum hourly precipitation amount (in mm)""")
