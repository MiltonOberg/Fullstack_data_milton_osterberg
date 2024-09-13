import streamlit as st
from components.data import Medals_summer
from components.metrics import Metrics, Medals_country
from components.data import Countries
from components.graphs import Swedish_summer_graphs

metrics= Metrics()
medals_df= Medals_summer()
countries= Countries()
swedish_graphs= Swedish_summer_graphs()

def layout():
    st.markdown("# Summer olypics")
    st.markdown("""
                This shows 124 years of olympic data, only summer olympics will be shown.
                """)
    
    metrics.country_medals_top5()
    
    
    
    st.dataframe(medals_df.data)
    
    st.markdown("## Medals filtered country")
    selected_country= st.selectbox("Select a country", options= countries.noc)
    Medals_country(selected_country).display_medals()
    
    st.markdown("### Medals per athlete in Sweden")
    swedish_graphs.bar_medals_athletes_top10()
    
    st.markdown("### Medals per sport in Sweden")
    swedish_graphs.bar_medals_sport()
    
    
if __name__ == "__main__":
    layout()