from dotenv import load_dotenv
load_dotenv()
import streamlit as st
# 1. Update the import to match the new engine.py
from src.orchestrator.engine import run_gideon 

st.title("Gideon SRS - Sovereign Research Swarm")

# Initialize session state for memory if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Analyze CSE stocks or Insurance trends...")

if user_input:
    # Add user message to UI
    st.session_state.messages.append(("user", user_input))
    
    with st.spinner("Gideon is thinking..."):
        # 2. Call the new function 'run_gideon' instead of an Orchestrator class
        # We pass the history to maintain the 'Sliding Window' memory
        result = run_gideon(user_input, st.session_state.messages)
        
        # 3. Extract the final message from the result
        final_response = result["messages"][-1].content
        st.session_state.messages.append(("assistant", final_response))

# Display the chat history
for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content)