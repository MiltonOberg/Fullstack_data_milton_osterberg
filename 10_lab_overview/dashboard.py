import streamlit as st 
from frontend.kpi import ContentKPI, DeviceKPI, CountryViews
from frontend.graphs import ViewsTrend
from frontend.graphs_dictionary import graph_options
from frontend.read_css import read_css


# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
device_kpi= DeviceKPI()
country_views= CountryViews()
views_graph = ViewsTrend()
country_views= CountryViews()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    
    content_kpi.display_content()
    device_kpi.display_content()
    
    choice= st.selectbox("## Select graph", options= graph_options.keys())
    graph_options[choice].display_plot()

    country_views.display_content()
    
    read_css()
    
if __name__ == "__main__":
    layout()