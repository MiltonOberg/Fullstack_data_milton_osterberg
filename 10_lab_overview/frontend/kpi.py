import streamlit as st
from utils.query_database import QueryDatabase

class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")

        kpis = {
            "videor": len(df),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum(),
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))
        st.dataframe(df)

# create more KPIs here
class DeviceKPI:
    def __init__(self) -> None:
        self._content= QueryDatabase("SELECT * FROM marts.device_summary;").df

    def display_content(self):
        df= self._content
        st.markdown("## Visningar per enheter")
        

        for col, device, views in zip(st.columns(len(df["Enhetstyp"])), df["Enhetstyp"], df["Visningar"]):
            with col:
                st.metric(device, views)
                
class CountryViewsKPI:
    def __init__(self) -> None:
        self.df= QueryDatabase(f"SELECT * FROM marts.views_per_country").df
    
    def display_content(self):
        st.markdown("## Visningar per land")
        
        for col, country, views in zip(st.columns(len(self.df["Geografi"])), self.df["Geografi"], self.df["Visningar"]):
            with col:
                st.metric(country, round(views))