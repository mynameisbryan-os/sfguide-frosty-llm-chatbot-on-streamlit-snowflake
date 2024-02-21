#from openai import OpenAI
from openai import AzureOpenAI
import re
import streamlit as st
from prompts import get_system_prompt

st.title("👨‍💻 Finn")

# Initialize the chat messages history
client = AzureOpenAI(
    azure_endpoint = "https://openai-asc-dev.openai.azure.com/", 
    api_key="13a0000b5e89459da486d992d6048b74",
    api_version="2024-02-15-preview")

if "messages" not in st.session_state:
    # system prompt includes table information, rules, and prompts the LLM to produce
    # a welcome message to the user.
    st.session_state.messages = [{"role": "system", "content": get_system_prompt()}]
    
# Prompt for user input and save
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

# display the existing chat messages
for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "results" in message:
            st.dataframe(message["results"])