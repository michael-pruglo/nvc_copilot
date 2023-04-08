#!/usr/bin/env python3

from view import MyGUI
from generator import get_message_suggestion

if __name__ == "__main__":
   MyGUI(get_message_suggestion).run()
