import streamlit as st
from backend.constants import CSS_PATH


def read_css():
    with open(CSS_PATH) as css:
        st.markdown(
            f"<style>{css.read()}<style>", unsafe_allow_html= True
                    )
