# main.py
import uvicorn
from fastapi import FastAPI
from api import api_router

app = FastAPI(title="Agentic CRM", description="CRM for Travel Agents")

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Agentic CRM!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
