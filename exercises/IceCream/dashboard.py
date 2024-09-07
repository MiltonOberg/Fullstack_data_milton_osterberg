import streamlit as st   
import pandas as pd
import numpy as np
from pathlib import Path
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def read_data():
    data_path= Path(__file__).parents[2]/"data"
    print(data_path)
    df= pd.read_csv(data_path/"exercises/IceCreamData.csv")
    return df



def layout():
    
    st.markdown("# Ice cream revenue prediction")
    data = read_data()

    X = data[["Temperature"]]
    y = data["Revenue"]


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)



    input= st.slider("Skriv temperatur: ", min_value= data["Temperature"].min(), max_value= data["Temperature"].max())
    formatted_input= np.array([[input]])
    y_pred = model.predict(formatted_input)
    
    st.markdown(f"Förutspådd intäckt temp:({input}) \nIntäckt {y_pred}")
    
if __name__ == '__main__':
    layout()
    