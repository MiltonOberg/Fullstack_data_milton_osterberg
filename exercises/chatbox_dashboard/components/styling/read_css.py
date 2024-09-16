from pathlib import Path
import streamlit as st

class Read_css:
    def read_css(self):
        styling_path= Path(__file__).parent
        css_path= styling_path/"style.css"
        with open(css_path) as css:
            st.markdown(f"<style>{css.read()}<style>", unsafe_allow_html= True)