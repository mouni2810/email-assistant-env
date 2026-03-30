from env import EmailEnv
from baseline import simple_agent, prioritize_agent, reply_agent

def evaluate():
    env = EmailEnv()

    total_score = 0
    episodes = 5

    # TASK 1: classification
    for _ in range(episodes):
        state = env.reset(task="classification")
        action = simple_agent(state["email_text"])
        _, reward, _, _ = env.step(action)
        total_score += reward

    # TASK 2: prioritization
    for _ in range(episodes):
        state = env.reset(task="prioritization")
        action = prioritize_agent(state["emails"])
        _, reward, _, _ = env.step(action)
        total_score += reward

    # TASK 3: reply
    for _ in range(episodes):
        state = env.reset(task="reply")
        action = reply_agent(state["email_text"])
        _, reward, _, _ = env.step(action)
        total_score += reward

    final_score = total_score / (episodes * 3)
    return final_score


if __name__ == "__main__":
    print("Final Score:", evaluate())