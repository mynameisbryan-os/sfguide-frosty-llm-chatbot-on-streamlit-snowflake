import streamlit as st
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint = "https://openai-asc-dev.openai.azure.com/",
    api_key="13a0000b5e89459da486d992d6048b74",
     api_version="2024-02-15-preview"
     )

completion = client.chat.completions.create(
  model="gpt35turbo-osdemo",
  messages=[
    {"role": "user", "content": "What is Streamlit?"}
  ]
)

st.write(completion.choices[0].message.content)


conn = st.connection("snowflake")
df = conn.query("select current_warehouse()")
st.write(df)