from environment import CodeReviewEnv

env = CodeReviewEnv()

def reset():
    return env.reset()

def step(action):
    return env.step(action)

def state():
    return env.state()