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

def gpt_response(prompt:str) -> str:
    # return f"dummy to '{prompt}'"
    chat_hist = [{"role": "system", "content": CONTEXTUAL_PROMPT}]
    chat_hist.append({"role": "user", "content": prompt})
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_hist,
    )
    assistant_answer = completions.choices[0].message.content
    chat_hist.append({"role": "assistant", "content": assistant_answer})
    return completions
