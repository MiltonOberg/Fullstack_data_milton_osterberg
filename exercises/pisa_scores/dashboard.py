
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
    basic_stats= pd.DataFrame(data= df, columns=)
    st.dataframe(basic_stats)
    
if __name__ == "__main__":
    run_dashboard()