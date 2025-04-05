import os
import streamlit as st
from datetime import date
from langchain_core.messages import AIMessage, HumanMessage

from src.AgenticAI.frontend_ui.config_ui import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config() 
        self.user_controls = {}

    def initialize_session(self):
        return {
        "current_step": "requirements",
        "requirements": "",
        "user_stories": "",
        "po_feedback": "",
        "generated_code": "",
        "review_feedback": "",
        "decision": None
    }

    def render_requirements(self):
        st.markdown("## Requirements submission")
        st.session_state.state["requirements"] = st.text_area(
            "Enter your requirements:",
            height=200,
            key="req_input"
        )
        if st.button("Submit Requirements", key="submit_req"):
            st.session_state.state["current_step"] = "generate_user_stories"
            st.session_state.IsSDLC = True


    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False
        with st.sidebar:
            # Get Option from config
            llm_options = self.config.get_llm_option()
            usecase_options = self.config.get_usecase_option()
            groq_model_option = self.config.get_groq_model_option()

            # LLM Selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", groq_model_option)
                # API key Input
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API_KEY", type="password")

                # Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API KEY to proceed. Don't have? refer: https://console.groq.com/keys ")


            # Use case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)
            

        return self.user_controls