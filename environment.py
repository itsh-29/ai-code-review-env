import random

class CodeReviewEnv:

    def __init__(self):
        self.tasks = [

            # EASY
            {
                "code": "def add(a,b)\n return a+b",
                "type": "syntax_error",
                "difficulty": "easy"
            },
            {
                "code": "def func()\n print('hello')",
                "type": "syntax_error",
                "difficulty": "easy"
            },

            # MEDIUM
            {
                "code": "def multiply(a,b): return a+b",
                "type": "logic_error",
                "difficulty": "medium"
            },
            {
                "code": "def is_even(n): return n % 2 == 1",
                "type": "logic_error",
                "difficulty": "medium"
            },

            # HARD
            {
                "code": "nums=[]\nfor i in range(1000): nums.append(i)",
                "type": "optimization_suggestion",
                "difficulty": "hard"
            },
            {
                "code": "result=[]\nfor i in data:\n result.append(i*2)",
                "type": "optimization_suggestion",
                "difficulty": "hard"
            }
        ]

    def reset(self):
        self.current_task = random.choice(self.tasks)

        return {
            "code": self.current_task["code"],
            "difficulty": self.current_task["difficulty"],
            "task": "analyze_and_fix"
        }

    def step(self, action):
        correct = self.current_task["type"]

        predicted_label = action.get("label", "").lower()
        explanation = action.get("explanation", "").lower()
        fix = action.get("fix", "").lower()

        reward = 0.0

     
        if predicted_label == correct:
            reward += 0.6
        elif predicted_label in ["syntax_error", "logic_error"]:
            reward += 0.3
        else:
            reward += 0.1

   
        keywords = {
            "syntax_error": ["missing", "syntax", "indent"],
            "logic_error": ["wrong", "incorrect", "bug"],
            "optimization_suggestion": ["faster", "optimize", "efficient"]
        }

        for word in keywords.get(correct, []):
            if word in explanation:
                reward += 0.3
                break

        
        if correct == "logic_error" and ("*" in fix or "correct" in fix):
            reward += 0.2
        elif correct == "syntax_error" and ":" in fix:
            reward += 0.2
        elif correct == "optimization_suggestion" and ("list comprehension" in fix or "[" in fix):
            reward += 0.2

        return {}, min(reward, 1.0), True, {
            "correct": correct,
            "difficulty": self.current_task["difficulty"]
        }

    def state(self):
        return self.current_task