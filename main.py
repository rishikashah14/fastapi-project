from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My first API 🚀"}

@app.get("/health")
def health():
    return {"status": "working"}