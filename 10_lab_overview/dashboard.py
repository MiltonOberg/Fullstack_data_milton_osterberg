import streamlit as st 
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend, CountryViews
from frontend.graphs_dictionary import graph_options


# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
country_views= CountryViews()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    content_kpi.display_content()
    
    choice= st.selectbox("Select graph", options= graph_options.keys())
    graph_options[choice].display_plot()

if __name__ == "__main__":
    layout()