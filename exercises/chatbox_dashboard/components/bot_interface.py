import streamlit as st
from components.chatbox import Bot

class Bot_interface:
    def start_session_state(self):
        if "message" not in st.session_state:
            st.session_state.messages= []
        if "bot" not in st.session_state:
            st.session_state.bot= Bot()
    
    def display_message_history(self):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(st.chat_message(message["message"]))
    
    
    def user_input(self):
        
        if prompt := st.chat_input("Write message"):
            
            with st.chat_message("user"):
                st.markdown(prompt)
                
            st.session_state.messages.append({"role": "user", "message": prompt})
            
            response= st.session_state.bot.chat(prompt)
            
            with st.chat_message("Bot"):
                st.markdown(response)
            
            st.session_state.messages.append({"role": "bot", "message": response})