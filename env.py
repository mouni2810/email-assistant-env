from dataset import get_random_email, get_multiple_emails

class EmailEnv:
    def __init__(self):
        self.current_email = None
        self.email_list = None
        self.task = "classification"
        self.done = False

    def reset(self, task="classification"):
        self.task = task
        self.done = False

        if task == "classification":
            self.current_email = get_random_email()
        elif task == "prioritization":
            self.email_list = get_multiple_emails(3)
        elif task == "reply":
            self.current_email = get_random_email()
        return self.state()

    def state(self):
        if self.task == "classification":
            return {
                "email_text": self.current_email["text"]
            }

        elif self.task == "prioritization":
            return {
                "emails": [e["text"] for e in self.email_list]
            }
        elif self.task == "reply":
            return {
            "email_text": self.current_email["text"]
            }

    def step(self, action):
        reward = 0

        # TASK 1: classification
        if self.task == "classification":
            correct_label = self.current_email["label"]

            if action == correct_label:
                reward = 1
            else:
                reward = -0.2

            self.done = True
            return self.state(), reward, self.done, {"correct": correct_label}

        # TASK 2: prioritization
        elif self.task == "prioritization":
            # correct order: important > normal > spam
            priority_map = {"important": 3, "normal": 2, "spam": 1}

            correct_order = sorted(
                range(len(self.email_list)),
                key=lambda i: priority_map[self.email_list[i]["label"]],
                reverse=True
            )

            # action = list of indices
            score = 0
            for i in range(len(action)):
                if action[i] == correct_order[i]:
                    score += 1

            reward = score / len(action)  # partial reward
            self.done = True

            return self.state(), reward, self.done, {
                "correct_order": correct_order
            }
        elif self.task == "reply":
            correct_reply = self.current_email["reply"]

            # simple similarity check
            if action.lower() in correct_reply.lower():
                reward = 1
            elif any(word in action.lower() for word in correct_reply.lower().split()):
                reward = 0.5
            else:
                reward = -0.2

            self.done = True

            return self.state(), reward, self.done, {
                "expected_reply": correct_reply
            }