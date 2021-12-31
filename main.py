import tkinter as tk

import api

window = tk.Tk()

title = tk.Label(text="Code Decks")
title.pack()

sub_title = tk.Label(text="Add a Code Snippet")
sub_title.pack()

#####
# The Form
#####
problem_lbl = tk.Label(text="The Task")
problem_lbl.pack()
problem_txtfld = tk.Entry()
problem_txtfld.pack()

code_lbl = tk.Label(text="The Code")
code_lbl.pack()
code_txtfld = tk.Text()
code_txtfld.pack()

output = tk.Label(text="")

submit_btn = tk.Button(
    text="Add code snippet",
    command=api.add_code_deck(
        output, task=problem_txtfld.get(), code=code_txtfld.get("1.0", tk.END)
    ),
)
submit_btn.pack()

window.mainloop()
