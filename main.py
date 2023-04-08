#!/usr/bin/env python3

from view import MyGUI
from generator import Generator

if __name__ == "__main__":
    g = Generator()
    MyGUI(g.get_message_suggestion, g.refine_suggestion).run()
