from fastapi import FastAPI
from pydantic import BaseModel
from env import EmailEnv
import uvicorn
from app import app
app = FastAPI()
env = EmailEnv()

class Action(BaseModel):
    action: str

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)
@app.post("/reset")
def reset():
    return {"state": env.reset()}

@app.post("/step")
def step(action: Action):
    state, reward, done, info = env.step(action.action)

    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return {"state": env.state()}