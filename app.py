from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from environment import CodeReviewEnv

app = FastAPI()
env = CodeReviewEnv()

# 🖥️ UI HOME
@app.get("/", response_class=HTMLResponse)
def home():
    task = env.reset()

    return f"""
    <h2>AI Code Review Environment</h2>
    <p>Difficulty: {task['difficulty']}</p>
    <pre>{task['code']}</pre>

    <form action="/step_ui" method="post">
        Label: <input name="label" placeholder="syntax_error / logic_error"><br>
        Explanation: <input name="explanation" placeholder="explain the issue"><br>
        Fix: <input name="fix" placeholder="suggest corrected code"><br>
        <button type="submit">Submit</button>
    </form>
    """

# 🧠 UI STEP
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
    <p>Difficulty: {info['difficulty']}</p>
    <a href="/">Try Another</a>
    """

# 🤖 OPENENV API (IMPORTANT FOR VALIDATION)

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)