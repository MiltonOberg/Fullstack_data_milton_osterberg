
import streamlit as st   
import pandas as pd
import numpy as np
from pathlib import Path
import plotly.express as px

def read_data():
    
    data_path= Path(__file__).parents[2]/"data"
    data= Path(data_path/"exercises"/"OECD PISA data.csv")
    df= pd.read_csv(data)
    return df

def run_dashboard():
    df= read_data()
    
    st.markdown("# PISA Scores")
    st.dataframe(df)
    basic_stats= pd.DataFrame({"Records": [df["index"].count()], 
                               "Locations": [df["LOCATION"].count()], 
                               "Subjects": [df["SUBJECT"].count()],
                               "Average time": [round(df["TIME"].mean())]
                               })
    st.dataframe(basic_stats)
    
    score_location= df.groupby("LOCATION")["Value"].mean().reset_index()
    fig= px.bar(score_location, x= "LOCATION", y= "Value", title= "Avg score per country")
    st.plotly_chart(fig)
    
    country= st.selectbox("Choose a Country", score_location["LOCATION"])
    
    country_df= df[df["LOCATION"]== country]
    time_value= country_df.groupby("TIME", as_index= False)["Value"].mean()
        
    fig= px.line(time_value, x= "TIME", y= "Value")
    st.plotly_chart(fig)
    
if __name__ == "__main__":
    run_dashboard()