#Import streamlit
import streamlit as st

#Import required packages
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import plotly.graph_objects as go

#Insert title
st.title('Aviation and Weather in the Netherlands')
st.subheader('From 2000 to 2019')

#Insert warning
st.warning("*Disclaimer: The years 2020 and 2021 are excluded due to the COVID-19 pandemic!*")

#Insert information
st.info("""
Three different studies:\n
1. **Summer holiday period (July and August)**: Investigate whether the weather during the summer influences the behaviour of (arriving/departing) (holiday) passengers during the summer period.\n
2. **Summer holiday period (July and August) and the weather during the year**: Investigate whether the weather during the year influences the behaviour of (arriving/departing) (early booking) (holiday) passengers in the summer period.\n 
3. **Year-round weather**: Investigate whether the weather during the year influences the behaviour of (arriving/departing) passengers all year round.\n
""")

#Upload dataframe
df = pd.read_csv('data.csv')

#Make selectbox of the different studies
period = st.selectbox(label = 'Select study:', 
		      options = ['Study 1', 'Study 2', 'Study 3'], 
		      help = 'Select the desired period for the examination here. The first option is the study in which only the aviation and the weather in the months July and August are investigated. The second option is the study in which only the average aviation in the months July and August was examined and thereby the average weather of that particular year. The third option is the study that looks at the whole year for both aviation and weather.')

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
       
if period == 'Study 1':	
	x = st.radio(label = "Select type of passengers:", 
		     options = ['Total number of passengers (1)', 
				'Total passengers arriving (1)', 
				'Total passengers departing (1)'], 
		     help = 'Select the desired type of passenger here. The first option is to look at both arriving and departing passengers. The second option is to look only at arriving passengers. The third option is to only look at departing passengers.')

	y = st.multiselect(label = "Select weather factor:", 
			   options = ['SQ (1)', 'TX (1)', 'TG (1)'], 
			   help = 'Select the desired weather factor(s) here. A previous study looked at which weather factors have the most impact on aviation per period. This resulted in a top three per period, in total seven different weather factors per period were examined. The order of the weather factors to be selected, from left to right, is therefore also important because the weather factor on the left has the greatest impact on aviation and the one on the right has the least impact.')

if period == 'Study 2':	
	x = st.radio(label = "Select type of passengers:", 
		     options = ['Total number of passengers (2)', 
				'Total passengers arriving (2)', 
				'Total passengers departing (2)'], 
		     help = 'Select the desired type of passenger here. The first option is to look at both arriving and departing passengers. The second option is to look only at arriving passengers. The third option is to only look at departing passengers.')

	y = st.multiselect(label = "Select weather factor:", 
			   options = ['SQ (2)', 'TX (2)', 'TG (2)'], 
			   help = 'Select the desired weather factor(s) here. A previous study looked at which weather factors have the most impact on aviation per period. This resulted in a top three per period, in total seven different weather factors per period were examined. The order of the weather factors to be selected, from left to right, is therefore also important because the weather factor on the left has the greatest impact on aviation and the one on the right has the least impact.')

if period == 'Study 3':	
	x = st.radio(label = "Select type of passengers:", 
		     options = ['Total number of passengers (3)', 
				'Total passengers arriving (3)', 
				'Total passengers departing (3)'], 
		     help = 'Select the desired type of passenger here. The first option is to look at both arriving and departing passengers. The second option is to look only at arriving passengers. The third option is to only look at departing passengers.')

	y = st.multiselect(label = "Select weather factor:", 
			   options = ['TX (3)', 'TG (3)', 'TN (3)'], 
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
	
#--------------------
# # Create the base figure
# fig = go.Figure()

# # Add the bar graph of daily temperatures
# fig.add_trace(
# 	go.Bar(x = df['Periods'], y = df['Total number of passengers (1)'], name = 'Passengers'))

# # Add the monthly average line graph
# fig.add_trace(
# 	go.Scatter(x = df['Periods'], y = df['TG (1)'], name = 'Weather'))

# fig.update_yaxes(type = "log")

# # Show the plot
# fig.show()
