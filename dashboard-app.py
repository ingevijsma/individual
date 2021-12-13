#Import streamlit
import streamlit as st

#Import required packages
import pandas as pd
import plotly.express as px
import statsmodels.api as sm

# Primary accent for interactive elements
primaryColor = '#7792E3'

# Background color for the main content area
backgroundColor = '#273346'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#B9F1C0'

# Color used for almost all text
textColor = '#FFFFFF'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace) 
# Default: "sans serif"
font = "sans serif"

#Insert title
st.title('Aviation and weather in the Netherlands')

#Insert information
st.info("This research looked at aviation and weather in the Netherlands over the years, from the year 2000 to the year 2021 to be precise. Three different sub-studies were conducted. The first sub-study only looked at the summer months, July and August, and looked at whether the weather in the summer has an impact on the passengers' behaviour, i.e. whether more or fewer passengers arrive or depart. The second study looked at a slightly different period, namely the average number of passengers in the summer period, but did look at the weather during that entire year. This way, it can be examined whether the weather throughout the year has an impact on, for example, passengers who book their tickets early, which is often the case for vacationers in the summer period. The last and third study looked at both year-round aviation and the weather. Hereby, it can be examined whether the weather has an impact on the behaviour of passengers throughout the year and whether a good year in terms of weather has more or less arriving and departing passengers.")

#Insert warning
st.warning("Disclaimer: The years 2020 and 2021 are also included but these figures in terms of total, arriving and departing passengers are heavily influenced by the COVID-19 pandemic.")

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
		      help = 'Select the desired period for the examination here. The first option is the study in which only the aviation and the weather in the months July and August are investigated. The second option is the study in which only the average aviation in the months July and August was examined and thereby the average weather of that particular year. The third option is the study that looks at the whole year for both aviation and weather.')

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
		     help = 'Select the desired type of passenger here. The first option is to look at both arriving and departing passengers. The second option is to look only at arriving passengers. The third option is to only look at departing passengers.')

	y = st.multiselect(label = "Select weather factor:", 
			   options = ['SQ (July, August)', 'TX (July, August)', 'TG (July, August)'], 
			   help = 'Select the desired weather factor(s) here. A previous study looked at which weather factors have the most impact on aviation per period. This resulted in a top three per period, in total seven different weather factors per period were examined. The order of the weather factors to be selected, from left to right, is therefore also important because the weather factor on the left has the greatest impact on aviation and the one on the right has the least impact.')

if period == july_august_all:	
	x = st.radio(label = "Select type of passengers:", 
		     options = ['Total number of passengers (July, August - All)', 
				'Total passengers arriving (July, August - All)', 
				'Total passengers departing (July, August - All)'], 
		     help = 'Select the desired type of passenger here. The first option is to look at both arriving and departing passengers. The second option is to look only at arriving passengers. The third option is to only look at departing passengers.')

	y = st.multiselect(label = "Select weather factor:", 
			   options = ['SQ (July, August - All)', 'TX (July, August - All)', 'TG (July, August - All)'], 
			   help = 'Select the desired weather factor(s) here. A previous study looked at which weather factors have the most impact on aviation per period. This resulted in a top three per period, in total seven different weather factors per period were examined. The order of the weather factors to be selected, from left to right, is therefore also important because the weather factor on the left has the greatest impact on aviation and the one on the right has the least impact.')

if period == all:	
	x = st.radio(label = "Select type of passengers:", 
		     options = ['Total number of passengers (All)', 
				'Total passengers arriving (All)', 
				'Total passengers departing (All)'], 
		     help = 'Select the desired type of passenger here. The first option is to look at both arriving and departing passengers. The second option is to look only at arriving passengers. The third option is to only look at departing passengers.')

	y = st.multiselect(label = "Select weather factor:", 
			   options = ['TX (All)', 'TG (All)', 'TN (All)'], 
			   help = 'Select the desired weather factor(s) here. A previous study looked at which weather factors have the most impact on aviation per period. This resulted in a top three per period, in total seven different weather factors per period were examined. The order of the weather factors to be selected, from left to right, is therefore also important because the weather factor on the left has the greatest impact on aviation and the one on the right has the least impact.')

st.markdown('***')
st.markdown("<h3 style='text-align: center; color: black;'>Number of passengers (arriving/departing) versus weather factors</h3>", unsafe_allow_html = True)
st.markdown('***')

fig_scatterplot_trendline = st.checkbox('Trendline', value = False)
if fig_scatterplot_trendline == True:
  fig1 = px.scatter(data_frame = df, 
                    x = x, 
                    y = y, 
                    trendline = 'ols', 
                    trendline_scope = 'trace', 
		    rename = {'value': 'Value', 'variable': 'Variable:')
  
if fig_scatterplot_trendline == False:
  fig1 = px.scatter(data_frame = df, 
                    x = x, 
                    y = y, 
		    rename = {'value': 'Value', 'variable': 'Variable:')

st.plotly_chart(fig1)

with st.expander('More information:'):
	st.subheader('Tekst')
	st.markdown('''Tekst''')
