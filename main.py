from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import Agent

app = FastAPI()
agent = Agent()


class GoalRequest(BaseModel):
    goal: str


@app.get("/")
def home():
    return {"message": "Agentic AI running 🚀"}


@app.post("/run-agent")
def run_agent(request: GoalRequest):
    try:
        return agent.run(request.goal)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
