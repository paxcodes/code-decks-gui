import tkinter as tk


def add_code_deck(output: tk.Label, *, task: str, code: str):
    def add_to_api():
        print(task)
        print(code)

    return add_to_api
