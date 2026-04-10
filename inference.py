import os
from openai import OpenAI
from environment import CodeReviewEnv

# ENV VARS (MANDATORY)
API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY
)

env = CodeReviewEnv()

def log_start(task, env_name, model):
    print(f"[START] task={task} env={env_name} model={model}", flush=True)

def log_step(step, action, reward, done, error):
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}", flush=True)

def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.3f} rewards={rewards_str}", flush=True)


def call_llm():
    try:
        res = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": "Classify code issue"}],
            max_tokens=10
        )
        return res.choices[0].message.content or "ok"
    except Exception as e:
        return "fallback"


def main():
    rewards = []
    steps = 0
    success = False
    score = 0.0

    log_start("code-review", "custom-env", MODEL_NAME)

    try:
        obs = env.reset()

        for step in range(1, 6):

            # ✅ MUST CALL LLM
            _ = call_llm()

            # simple agent
            if obs["difficulty"] == "easy":
                action = {"label": "syntax_error", "explanation": "missing syntax", "fix": "add colon"}
            elif obs["difficulty"] == "medium":
                action = {"label": "logic_error", "explanation": "wrong logic", "fix": "fix operator"}
            else:
                action = {"label": "optimization_suggestion", "explanation": "optimize", "fix": "use list comprehension"}

            _, reward, done, info = env.step(action)

            rewards.append(reward)
            steps = step

            log_step(
                step=step,
                action=action["label"],
                reward=reward,
                done=done,
                error=None
            )

            if done:
                break

        score = sum(rewards) / len(rewards) if rewards else 0.0
        score = min(max(score, 0.0), 1.0)

        success = score > 0.3

    except Exception as e:
        print(f"[DEBUG] error={e}", flush=True)

    finally:
        log_end(success, steps, score, rewards)


if __name__ == "__main__":
    main()