import random

emails = [
    {
        "text": "Win $1000 now!!! Click here",
        "label": "spam",
        "reply": "This looks like spam. Ignoring."
    },
    {
        "text": "Meeting scheduled at 5 PM",
        "label": "important",
        "reply": "Got it, I will attend the meeting."
    },
    {
        "text": "Hey, how are you?",
        "label": "normal",
        "reply": "I am good, thanks for asking!"
    },
    {
        "text": "Your bank account needs verification",
        "label": "spam",
        "reply": "This seems suspicious. Not responding."
    },
    {
        "text": "Project deadline tomorrow",
        "label": "important",
        "reply": "I will complete the project before deadline."
    },
]

def get_random_email():
    return random.choice(emails)
def get_multiple_emails(n=3):
    return random.sample(emails, n)