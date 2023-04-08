#!/usr/bin/env python3

import openai
import os

openai.api_key = "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"

chat_hist = [{"role": "system", "content": "You are an expert in non-violent communication. I will give you drafts of messages and your task is to offer edits to make the messages conform to non-violent communication style."}]
def ask(prompt:str) -> str:
    global chat_hist
    chat_hist.append({"role": "user", "content": prompt})
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_hist,
    )
    assistant_answer = completions.choices[0].message.content
    chat_hist.append({"role": "assistant", "content": assistant_answer})
    return completions

def ask_interactive():
    while True:
        print(ask(input(">")))


violent_examples = [
    "You disappointed me by not coming over last week - I had to rewatch the same movie again",
]

from view import MyGUI

def foo(s):
    
    return "response to " + s

if __name__ == "__main__":
   MyGUI(foo).run()
