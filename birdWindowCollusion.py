import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(
    page_title="Birds Collussion",
    page_icon="✅",
    layout="wide",
)
st.markdown('<div style="text-align: center;"><h1>Bird collusion on Windows</H1></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;"><p>Year-round monitoring reveals prevalence of fatal bird-window collisions</p>', unsafe_allow_html=True)


df = pd.read_csv("bird-window-collision-death.csv")

col5, col6 = st.columns(2)


with col5:
    st.write(df)
with col6:
    st.write("Visual A - Visual representation of collusion with respect to building")
    fig = px.pie(df, values='Deaths', names='Bldg #', color="Side", hole=0.3, width=400, height=500)
    fig.update_traces(textinfo="label+percent", insidetextfont=dict(color="white"))
    #fig.update_layout(legend={"itemclick": False})
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)

col1, col2 = st.columns(2)



with col1:
   st.write("Visual B - Visual representation of collusion with respect to Month")
   fig1 = px.pie(df, values='Deaths', names='MONTH', color="Side", hole=0.3, width=400, height=400)
   fig1.update_traces(textinfo="label+percent", insidetextfont=dict(color="white"))
   fig1.update_layout(legend={"itemclick": False})
   st.plotly_chart(fig1)

with col2:
   st.write("Visual B - Visual representation of collusion with Year/Species/Fatality")
   line_chart = px.bar(
       data_frame=df,
       x="YEAR",
       y="Deaths",
       color='Common Name',
       labels={'Common Name': 'Bird Name'},
       width=400,
       height=400
   )
   st.plotly_chart(line_chart)