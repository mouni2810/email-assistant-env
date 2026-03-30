from env import EmailEnv

def simple_agent(email_text):
    email_text = email_text.lower()

    if "win" in email_text or "click" in email_text:
        return "spam"
    elif "meeting" in email_text or "deadline" in email_text:
        return "important"
    else:
        return "normal"
def reply_agent(email_text):
    email_text = email_text.lower()

    if "meeting" in email_text:
        return "I will attend the meeting."
    elif "deadline" in email_text:
        return "I will complete it on time."
    elif "win" in email_text or "bank" in email_text:
        return "This seems spam."
    else:
        return "Thanks for your message."
def prioritize_agent(email_list):
    priority_keywords = {
        "important": ["meeting", "deadline"],
        "spam": ["win", "click"],
    }

    scores = []

    for i, email in enumerate(email_list):
        text = email.lower()

        if any(k in text for k in priority_keywords["important"]):
            score = 3
        elif any(k in text for k in priority_keywords["spam"]):
            score = 1
        else:
            score = 2

        scores.append((i, score))

    # sort by score descending
    sorted_emails = sorted(scores, key=lambda x: x[1], reverse=True)

    return [i for i, _ in sorted_emails]
env = EmailEnv()

print("\n---- REPLY TASK ----")
state = env.reset(task="reply")

print("Email:", state["email_text"])

action = reply_agent(state["email_text"])

_, reward, _, info = env.step(action)

print("Reply:", action)
print("Reward:", reward)
print("Expected:", info["expected_reply"])
