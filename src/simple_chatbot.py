from openai import AzureOpenAI
import streamlit as st

client = AzureOpenAI(
    azure_endpoint = "https://openai-asc-dev.openai.azure.com/",
    api_key="13a0000b5e89459da486d992d6048b74",
     api_version="2024-02-15-preview"
     )

st.title("☃️ Finn")

# Initialize the chat messages history
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How can I help?"}]

# Prompt for user input and save
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

# display the existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, we need to generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    # Call LLM
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            r = client.chat.completions.create(
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                model="gpt35turbo-osdemo",
            )
            response = r.choices[0].message.content
            st.write(response)

    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
