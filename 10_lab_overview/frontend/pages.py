import streamlit as st
from frontend.kpi import ContentKPI, DeviceKPI, CountryViewsKPI
from frontend.graph_dictionary import graph_options

def home():
    st.title("The data driven youtuber")
    st.markdown("## Den här dashboarden syftar till att utforska datan i en youtubekanal")
    st.markdown("### Milton Österberg")

content_kpi = ContentKPI()
device_kpi= DeviceKPI()
country_views= CountryViewsKPI()

def kpier():
    st.title("Kpier")
    content_kpi.display_content()
    with st.container():

        col1, col2 = st.columns(2, gap= "medium")

        with col1:
            country_views.display_content()

    
    device_kpi.display_content()


def graphs():
    st.title("Grafer")
    choice= st.selectbox("Select graph", options= graph_options.keys())
    graph_options[choice].display_plot()