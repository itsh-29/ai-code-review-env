from environment import CodeReviewEnv

import random

def agent(obs):
    code = obs["code"]

    if "def add(a,b)" in code:
        return {
            "label": "syntax_error",
            "explanation": "missing colon in function definition"
        }

    elif "return a-b" in code:
        return {
            "label": random.choice(["logic_error", "no_issue"]),
            "explanation": "wrong operation used"
        }

    elif "append" in code:
        return {
            "label": "optimization_suggestion",
            "explanation": "can be written faster using list comprehension"
        }

    else:
        return {
            "label": "no_issue",
            "explanation": "code looks fine"
        }

env = CodeReviewEnv()

scores = {"easy": [], "medium": [], "hard": []}

for i in range(10):
    obs = env.reset()
    action = agent(obs)
    _, reward, done, info = env.step(action)

    scores[info["difficulty"]].append(reward)

    print("Code:", obs["code"])
    print("Difficulty:", info["difficulty"])
    print("Prediction:", action)
    print("Correct:", info["correct"])
    print("Reward:", reward)
    print("------")

print("\nFINAL SCORES:")
for level in scores:
    if scores[level]:
        print(level, ":", sum(scores[level]) / len(scores[level]))