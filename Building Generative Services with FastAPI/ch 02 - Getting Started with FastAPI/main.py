from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI() 
openai_client = OpenAI(api_key=api_key)

@app.get("/", include_in_schema=False)
def docs_redirect_controller():
    return RedirectResponse(url="/docs", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/status")
def root_controller():
    return {"status":"Healthy"}

@app.get("/chat")
def chat_controller(prompt: str = "Inspire me"):
    
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages = [
            {"role":"system", "content": "You are a helpful assistant."},
            {"role":"user", "content":prompt},
        ],
    )

    statement = response.choices[0].message.content
    return {"statement": statement}
