from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from environment import CodeReviewEnv

app = FastAPI()
env = CodeReviewEnv()

@app.get("/", response_class=HTMLResponse)
def home():
    task = env.reset()

    return f"""
    <h2>AI Code Review Environment</h2>
    <pre>{task['code']}</pre>

    <form action="/step_ui" method="post">
        Label: <input name="label"><br>
        Explanation: <input name="explanation"><br>
        Fix: <input name="fix"><br>
        <button type="submit">Submit</button>
    </form>
    """

@app.post("/step_ui", response_class=HTMLResponse)
def step_ui(label: str = Form(...), explanation: str = Form(...), fix: str = Form(...)):
    action = {
        "label": label,
        "explanation": explanation,
        "fix": fix
    }

    _, reward, _, info = env.step(action)

    return f"""
    <h3>Result</h3>
    <p>Reward: {reward}</p>
    <p>Correct: {info['correct']}</p>
    <a href="/">Try Another</a>
    """