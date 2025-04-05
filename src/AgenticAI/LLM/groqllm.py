import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        """Initialize with a dict containing user control inputs"""
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        """Retrieve and initialize the Groq LLM model"""
        try:
            # Get API key from user input or environment
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY", "")
            
            # Fallback to environment variable if user input is empty
            if not groq_api_key:
                groq_api_key = os.environ.get("GROQ_API_KEY", "")
            
            # Get selected model
            selected_groq_model = self.user_controls_input.get("selected_groq_model")
            
            # Validate inputs
            if not groq_api_key:
                st.error("Please enter a valid Groq API Key")
                return None
            if not selected_groq_model:
                st.error("Please select a Groq model")
                return None
                
            # Create and return the LLM instance
            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
            return llm
            
        except KeyError as e:
            raise ValueError(f"Missing required user control input: {e}")
        except Exception as e:
            raise ValueError(f"Error initializing Groq LLM: {e}")