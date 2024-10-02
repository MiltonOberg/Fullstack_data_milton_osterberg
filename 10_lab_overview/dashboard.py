import streamlit as st 
from frontend.read_css import read_css
from frontend.pages_dictionary import page_option


def layout():

    page= st.sidebar.radio("# Sidor", page_option.keys())
    page_option[page]()
    
    read_css()
    
if __name__ == "__main__":
    layout()