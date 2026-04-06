from fastapi import FastAPI
import uvicorn
from environment import CodeReviewEnv

app = FastAPI()
env = CodeReviewEnv()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)

# ✅ REQUIRED main function
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

# ✅ REQUIRED for validator
if __name__ == "__main__":
    main()