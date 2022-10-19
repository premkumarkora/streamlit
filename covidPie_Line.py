import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Covid Dashboard",
    page_icon="✅",
    layout="wide",
)


df = pd.read_csv("covidData.csv")


dff = df.groupby(['countriesAndTerritories',"year"], as_index=False)[['deaths','cases']].sum()

df_filterd = dff[dff['countriesAndTerritories'].isin(['China','Iran','Spain','Italy','India', 'USA'])]


col1, col2, col3 = st.columns(3)

with col1:
    st.dataframe(df_filterd)

with col2:

    CHOICES = {"deaths": "Fatality", "cases": "Cases"}
    option = st.selectbox(
        "You want to see data for",
         CHOICES.keys(), format_func=lambda x:CHOICES[ x ])



    pie_chart = px.pie(
        data_frame=df_filterd,
        names='countriesAndTerritories',
        values=option,
        hole=.3,
        labels={'countriesAndTerritories': 'Country'},
        width = 350,
        height = 350

    )

    st.plotly_chart(pie_chart)

with col3:

    line_chart = px.line(
        data_frame=df_filterd,
        x="deaths",
        y="cases",
        color='countriesAndTerritories',
        labels={'countriesAndTerritories': 'Countries'},
        width=400,
        height = 350
    )
    st.plotly_chart(line_chart)











