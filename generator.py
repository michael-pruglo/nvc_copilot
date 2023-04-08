import openai

openai.api_key = "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"

CONTEXTUAL_PROMPT = """
You are an expert in non-violent communication.
I will give you drafts of messages and your task is to
offer edits to make the messages conform to non-violent communication style.
"""

VIOLENT_EXAMPLES = [
    "You disappointed me by not coming over last week - I had to rewatch the same movie again",
]

def refine_prompt(part):
    return f"Reword the part of the message '{part}' please."


class Generator:
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.chat_hist = [{"role": "system", "content": CONTEXTUAL_PROMPT}]

    def get_message_suggestion(self, draft_msg:str) -> str:
        return f"dummy to '{draft_msg}'"
        self.reset()
        return self._ask_gpt(draft_msg)

    def refine_suggestion(self, part:str) -> str:
        return f"refined dummy to '{part}'"
        return self._ask_gpt(refine_prompt(part))

    def _ask_gpt(self, prompt:str) -> str:
        self.chat_hist.append({"role": "user", "content": prompt})
        completions = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.chat_hist,
        )
        assistant_answer = completions.choices[0].message.content
        self.chat_hist.append({"role": "assistant", "content": assistant_answer})
        return completions
