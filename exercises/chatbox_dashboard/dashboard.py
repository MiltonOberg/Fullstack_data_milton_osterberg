import streamlit as st
from components.bot_interface import Bot_interface
from components.styling.read_css import Read_css


interface= Bot_interface()
read_css= Read_css()

def layout():
    st.markdown("# Chatbox")

    interface.display_message_history()
    interface.user_input()
    
    read_css.read_css()
    
    
    
if __name__ == "__main__":
    interface.start_session_state()
    layout()