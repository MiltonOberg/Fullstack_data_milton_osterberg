from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st 

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)

# create more graphs here
class CountryViews:
    def __init__(self) -> None:
        self.df= QueryDatabase(f"SELECT * FROM marts.views_per_country").df
    
    def display_plot(self):
        fig= px.bar(self.df, x= "Geografi", y= "Visningar")
        fig.update_xaxes(title= "Countries")
        st.markdown("## Antal visningar per land")
        st.plotly_chart(fig)
        
class Top5MostWatchedVideos:
    def __init__(self) -> None:
        self.df= QueryDatabase(f"SELECT * FROM marts.top5_watched_videos").df
        
    def display_plot(self):
        fig= px.bar(self.df, x= "Videotitel", y= "Visningar")
        fig.update_xaxes(titlefont= dict(size= 20), 
                         tickfont= dict(size= 15))
        fig.update_yaxes(titlefont= dict(size= 20),
                         range= [0, self.df["Visningar"].max()])
        st.markdown("## Top 5 most watched videos")
        st.plotly_chart(fig)
        
    
class Top5ClickExposure:
    def __init__(self) -> None:
        self.df= QueryDatabase(f"SELECT * FROM marts.top5_click_exposure").df
    
    def display_plot(self):
        fig= px.bar(self.df, x= "Videotitel", y= "click%")
        fig.update_xaxes(title= "Click percentage",
                         titlefont= dict(size= 20), 
                         tickfont= dict(size= 15))
        fig.update_yaxes(titlefont= dict(size= 20))
        st.markdown("## Click percentage of exposure")
        st.plotly_chart(fig)
    

