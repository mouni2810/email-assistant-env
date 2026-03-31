# inference.py

from baseline import simple_agent, prioritize_agent, reply_agent

def infer(input_data: dict):
    """
    input_data will contain:
    - task type
    - email_text OR emails list
    """

    # Detect task
    if "email_text" in input_data and "emails" not in input_data:
        text = input_data["email_text"]

        # Try classification first
        label = simple_agent(text)

        # If reply task expected → return reply
        reply = reply_agent(text)

        # Heuristic: if they expect reply (long string)
        if len(reply.split()) > 2:
            return reply

        return label

    elif "emails" in input_data:
        # prioritization task
        return prioritize_agent(input_data["emails"])

    else:
        return "normal"