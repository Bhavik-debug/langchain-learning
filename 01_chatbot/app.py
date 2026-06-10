from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm = ChatOpenAI(
    model="google/gemma-3n-e4b-it",
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)
output_parser=StrOutputParser() #Converts the model output into a simple string.
chain=prompt|llm|output_parser  #This is LangChain Expression Language (LCEL).
                                # The | operator means:
                                # Prompt
                                #    ↓
                                # LLM
                                #    ↓
                                # Parser

if input_text:
    st.write(
        chain.invoke(
            {'question':input_text}
        )
    )