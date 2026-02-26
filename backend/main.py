from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    response = agent.run(request.question)
    return {"response": response}