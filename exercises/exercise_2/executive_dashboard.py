import streamlit as st   
import pandas as pd
from pathlib import Path
import plotly.express as px


def read_data():
    data_path= Path(__file__).parents[2]/"data"
    print(data_path)
    df= pd.read_csv(data_path/"exercises/supahcoolsoft.csv")
    return df


def layout():
    df= read_data()
    
    
    st.markdown("# Employees")
    
    average_age= round(df["Age"].mean())
    total_employees= df["EmployeeID"].count()
    average_salary= round(df["Salary_SEK"].mean())

    st.markdown(f"""
                Total employee count: {total_employees}\n
                Average employee age: {average_age}\n
                Average salary: {average_salary}SEK""")

    st.dataframe(df)
    department_employees= df["Department"].value_counts().reset_index()
    print(department_employees)
    fig= px.bar(department_employees, x=department_employees["Department"],  y= department_employees["count"])
    st.plotly_chart(fig)
    
    
    fig= px.histogram(df, y= "Salary_SEK")
    st.plotly_chart(fig)
    
    
    fig= px.box(df, x= "Position", y= "Salary_SEK", labels= {"Salary": "Lön(sek)", "Position": "Position"})
    st.plotly_chart(fig)
    
    fig= px.histogram(df, y= "Age")
    st.plotly_chart(fig)
    
    fig= px.box(df, x= "Department", y= "Age", labels= {"Age": "Ålder", "Department": "Avdelning"})
    st.plotly_chart(fig)

if __name__ == '__main__':
    layout()