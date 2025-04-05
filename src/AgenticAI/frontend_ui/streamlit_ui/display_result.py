import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        """Initialize with use case, graph, and current user message."""
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

        # Initialize chat history in session state if not already present
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

    def display_result_on_ui(self):
        """Display the complete chat history and process new messages."""
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        # Add the new user message to chat history
        if user_message:
            st.session_state.chat_history.append({"role": "user", "content": user_message})

        # Display the entire chat history
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Process new message and append assistant response if applicable
        if user_message and usecase == "Basic Chatbot":
            for event in graph.stream({'messages': ("user", user_message)}):
                for value in event.values():
                    assistant_response = value["messages"].content
                    # Add assistant response to chat history
                    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
                    # Display the new assistant response immediately
                    with st.chat_message("assistant"):
                        st.write(assistant_response)