from components.data import Swedish_summer_medals
import streamlit as st


class Swedish_summer_graphs:
    def __init__(self) -> None:
        self.swe_medals= Swedish_summer_medals()
    
    def bar_medals_athletes_top10(self):
        data= self.swe_medals.per_athlete.head(10)
        
        st.bar_chart(data, x_label= "Athlete", y_label= "Medals per athlete")
        
    def bar_medals_sport(self):
        data= self.swe_medals.per_sport
        
        st.bar_chart(data, x_label= "Sport", y_label= "Medals per sport")