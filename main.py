#!/usr/bin/env python3

from view import MyGUI
from generator import gpt_response

if __name__ == "__main__":
   MyGUI(gpt_response).run()
