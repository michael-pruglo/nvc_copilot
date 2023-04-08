import tkinter as tk
from tkinter import ttk
import tkinter.font
from typing import Callable

FG_COLOR = "#ddd"
PLACEHOLDER = "Your draft here..."

def add_placeholder(text_widget):
    text_widget.insert("1.0", PLACEHOLDER)
    text_widget.config(fg="gray")
    def on_click(event):
        if text_widget.get("1.0", "end-1c") == PLACEHOLDER:
            text_widget.delete("1.0", "end-1c")
            text_widget.config(fg=FG_COLOR)

    def on_focus_out(event):
        if not text_widget.get("1.0", "end-1c"):
            text_widget.insert("1.0", PLACEHOLDER)
            text_widget.config(fg="gray")

    text_widget.bind("<FocusIn>", on_click)
    text_widget.bind("<FocusOut>", on_focus_out)


class MyGUI:
    BTN_H = 0.15

    def __init__(self, get_response_cb:Callable[[str],str], refine_response_cb:Callable[[str],str]):
        self.get_response_cb = get_response_cb
        self.refine_response_cb = refine_response_cb
        self.create_gui()

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("NVC assistant")
        self.root.geometry("1000x600")
        self.root.bind("<Control-Return>", lambda e: self.show_suggestions())

        self.inp_text = tk.Text(self.root, fg=FG_COLOR, bg="#222",
                                font=("Arial", 14, "bold"),
                                insertbackground="#ddd", insertwidth=4)
        add_placeholder(self.inp_text)
        self.outp_label = tk.Label(self.root, fg=FG_COLOR, bg="#222", anchor="nw",
                                   font=("Arial", 14, "bold"),
                                   justify="left", wraplength=450)
        self.button = tk.Button(self.root, command=self.show_suggestions,
                                fg=FG_COLOR, bg="#252",
                                font=("Arial", 19), text="make suggestions")

        self.inp_text.place(relwidth=0.5, relheight=1-self.BTN_H)
        self.outp_label.place(relwidth=0.5, relheight=1-self.BTN_H, relx=0.5)
        self.button.place(relwidth=1, relheight=self.BTN_H, rely=1-self.BTN_H)

    def show_suggestions(self):
        usr_input = self.inp_text.get("1.0", "end-1c").strip()
        if (not usr_input or usr_input == PLACEHOLDER):
            return
        print(f"request for '{usr_input}'")
        response = self.get_response_cb(usr_input)
        self.outp_label.config(text=response)

    def run(self):
        self.root.mainloop()
