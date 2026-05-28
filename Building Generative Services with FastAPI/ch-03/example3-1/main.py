from fastapi import FastAPI
from models import load_text_model, generate_text

app = FastAPI()

@app.get("/generate/text")
def server_llm_controller(prompt: str) -> str:
    pipe = load_text_model()
    print(pipe)
    output = generate_text(pipe, prompt)
    return output