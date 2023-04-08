import os
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

def prompt_refine(part): return f"Reword the part of the message '{part}' please"
def prompt_make_terse(): return f"Make it more concise - use about 5% fewer words"


class Generator:
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.chat_hist = [{"role": "system", "content": CONTEXTUAL_PROMPT}]

    def get_message_suggestion(self, draft_msg:str) -> str:
        if os.getenv("DUMMY"):
            return f"Dummy suggestion for '{draft_msg}'"
        self.reset()
        return self._ask_gpt(draft_msg)

    def reword_part(self, part:str) -> str:
        if os.getenv("DUMMY"):
            return f"Dummy reword for '{part}'"
        return self._ask_gpt(prompt_refine(part))

    def make_terse(self) -> str:
        if os.getenv("DUMMY"):
            return f"Dummy terser"
        return self._ask_gpt(prompt_make_terse())

    def _ask_gpt(self, prompt:str) -> str:
        self.chat_hist.append({"role": "user", "content": prompt})
        completions = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.chat_hist,
        )
        assistant_answer = completions.choices[0].message.content
        self.chat_hist.append({"role": "assistant", "content": assistant_answer})
        print(completions, "\n\n")
        return assistant_answer


if __name__ == "__main__":
    g = Generator()
    g.get_message_suggestion(VIOLENT_EXAMPLES[0])
    g.reword_part(input(">"))
