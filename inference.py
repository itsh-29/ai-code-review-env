from environment import CodeReviewEnv
import os

API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "")
HF_TOKEN = os.getenv("HF_TOKEN")


env = CodeReviewEnv()

tasks = ["easy", "medium", "hard"]
scores = {}

for difficulty in tasks:
    total_reward = 0
    steps = 0

    print(f"[START] task={difficulty}", flush=True)

    for _ in range(3):  # run few samples
        obs = env.reset()

        # simple baseline agent
        if obs["difficulty"] == "easy":
            action = {
                "label": "syntax_error",
                "explanation": "missing syntax",
                "fix": "add colon"
            }
        elif obs["difficulty"] == "medium":
            action = {
                "label": "logic_error",
                "explanation": "wrong logic",
                "fix": "correct operator"
            }
        else:
            action = {
                "label": "optimization_suggestion",
                "explanation": "can be optimized",
                "fix": "use list comprehension"
            }

        _, reward, done, info = env.step(action)

        steps += 1
        total_reward += reward

        print(f"[STEP] step={steps} reward={reward}", flush=True)

    avg_score = total_reward / steps if steps > 0 else 0
    scores[difficulty] = avg_score

    print(f"[END] task={difficulty} score={avg_score} steps={steps}", flush=True)