import streamlit as st
from components.bot_interface import Bot_interface



interface= Bot_interface()

def layout():
    st.markdown("# Chatbox")

    interface.display_message_history()
    interface.user_input()
    
    
    
    
    
if __name__ == "__main__":
    interface.start_session_state()
    layout()