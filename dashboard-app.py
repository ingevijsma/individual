#Import streamlit
import streamlit as st

#Import required packages
import pandas as pd
import plotly.express as px
import statsmodels.api as sm

#Insert title
st.title('Aviation and weather in the Netherlands from 2000 to 2019')

#Insert warning
st.warning("*Disclaimer: The years 2020 and 2021 are excluded due to the COVID-19 pandemic!*")

#Insert information
st.info("""
Three different studies:\n 
1. **Summer holiday period (July and August)**: To see if the weather in summer influences the behaviour of (arriving/departing) passengers during the summer holidays.\n 
2. **Summer holiday period (July and August) and weather during the year**: To see if the weather throughout the year influences the behaviour of (arriving/departing) early booking passengers.\n 
3. **Year-round**: To see if the weather throughout the year influences the behaviour of (arriving/departing) passengers throughout the year.
""")

#Upload dataframe
df = pd.read_csv('data.csv')

#Make selectbox of the different studies
period = st.selectbox(label = 'Select study:', 
		      options = ['july_august', 'july_august_all', 'all'], 
		      help = 'Select the desired period for the examination here. The first option is the study in which only the aviation and the weather in the months July and August are investigated. The second option is the study in which only the average aviation in the months July and August was examined and thereby the average weather of that particular year. The third option is the study that looks at the whole year for both aviation and weather.')

#Make three lists for different studies
if period == 'july_august':
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

if period == 'july_august_all':
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

if period == 'all':
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
       
if period == 'july_august':	
	x = st.radio(label = "Select type of passengers:", 
		     options = ['Total number of passengers (July, August)', 
				'Total passengers arriving (July, August)', 
				'Total passengers departing (July, August)'], 
		     help = 'Select the desired type of passenger here. The first option is to look at both arriving and departing passengers. The second option is to look only at arriving passengers. The third option is to only look at departing passengers.')

	y = st.multiselect(label = "Select weather factor:", 
			   options = ['SQ (July, August)', 'TX (July, August)', 'TG (July, August)'], 
			   help = 'Select the desired weather factor(s) here. A previous study looked at which weather factors have the most impact on aviation per period. This resulted in a top three per period, in total seven different weather factors per period were examined. The order of the weather factors to be selected, from left to right, is therefore also important because the weather factor on the left has the greatest impact on aviation and the one on the right has the least impact.')

if period == 'july_august_all':	
	x = st.radio(label = "Select type of passengers:", 
		     options = ['Total number of passengers (July, August - All)', 
				'Total passengers arriving (July, August - All)', 
				'Total passengers departing (July, August - All)'], 
		     help = 'Select the desired type of passenger here. The first option is to look at both arriving and departing passengers. The second option is to look only at arriving passengers. The third option is to only look at departing passengers.')

	y = st.multiselect(label = "Select weather factor:", 
			   options = ['SQ (July, August - All)', 'TX (July, August - All)', 'TG (July, August - All)'], 
			   help = 'Select the desired weather factor(s) here. A previous study looked at which weather factors have the most impact on aviation per period. This resulted in a top three per period, in total seven different weather factors per period were examined. The order of the weather factors to be selected, from left to right, is therefore also important because the weather factor on the left has the greatest impact on aviation and the one on the right has the least impact.')

if period == 'all':	
	x = st.radio(label = "Select type of passengers:", 
		     options = ['Total number of passengers (All)', 
				'Total passengers arriving (All)', 
				'Total passengers departing (All)'], 
		     help = 'Select the desired type of passenger here. The first option is to look at both arriving and departing passengers. The second option is to look only at arriving passengers. The third option is to only look at departing passengers.')

	y = st.multiselect(label = "Select weather factor:", 
			   options = ['TX (All)', 'TG (All)', 'TN (All)'], 
			   help = 'Select the desired weather factor(s) here. A previous study looked at which weather factors have the most impact on aviation per period. This resulted in a top three per period, in total seven different weather factors per period were examined. The order of the weather factors to be selected, from left to right, is therefore also important because the weather factor on the left has the greatest impact on aviation and the one on the right has the least impact.')

#Add black line
st.markdown('***')
st.markdown("<h3 style='text-align: center; color: black;'>Number of passengers (arriving/departing) versus weather factors</h3>", unsafe_allow_html = True)
st.markdown('***')

#Code scatterplot with trendline
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
	st.subheader('Abbreviation of weather factors with units:')
	st.markdown("""TG = Daily mean temperature (in degrees Celsius)\n
TN = Minimum temperature (in degrees Celsius)\n
TX = Maximum temperature (in degrees Celsius)\n
SQ = Sunshine duration (in hour)""")
