import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Survey Results')
st.header('Survey Results 2023')
st.subheader('Used dummy data!')

###--- Load Data Frame

excel_file = 'Survey_Results.xlsx'
sheet_name = 'DATA'

df=pd.read_excel(excel_file,
                 sheet_name=sheet_name,
                 usecols='B:D',
                 header=3)

df_participants=pd.read_excel(excel_file,
                 sheet_name=sheet_name,
                 usecols='F:G',
                 header=3)
df_participants.dropna(inplace=True)




#stream list selection

department = df['Department'].unique().tolist()
ages = df['Age'].unique().tolist()

age_selection = st.slider('Age :',
                          min_value=min(ages),
                          max_value=max(ages),
                          value=(min(ages),max(ages)))

department_selection = st.multiselect('Department :',
                                      department,
                                      default=department)

mask = (df['Age'].between(*age_selection)) & (df['Department'].isin(department_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

#Group Data frame after selection

df_grouped=df[mask].groupby(by=['Rating']).count()[['Age']]
df_grouped =df_grouped.rename(columns={'Age' : 'Votes'})
df_grouped =df_grouped.reset_index()

#-- Plot Bar chart

barchart = px.bar(df_grouped,
                  x='Rating',
                  y='Votes',
                  text='Votes',
                  color_discrete_sequence =['#F63366']*len(df_grouped),
                  template='plotly_white')

st.plotly_chart(barchart)

#Display Image & Data frame

col1, col2 = st.columns(2)

image = Image.open('images/survey.jpg')

col1.image(image,
        # caption='Designed by slidesgo / Freepik',
         use_container_width=True)

col2.dataframe(df)

##st.dataframe(df_participants)##
pie_chart = px.pie(df_participants,
                  title='Total No. of Participants',
                  values='Participants',
                  names='Departments')

st.plotly_chart(pie_chart)

