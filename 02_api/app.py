from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(
    title="LangServe Demo",
    version="1.0",
    description="A simple API Server"
)

model = ChatOpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY"),
    model="google/gemma-3n-e4b-it"
)

prompt = ChatPromptTemplate.from_template(
    "Write a poem about {topic} expressing deep feelings in 100 words with proper ryming."
)

add_routes(
    app,
    prompt | model,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)