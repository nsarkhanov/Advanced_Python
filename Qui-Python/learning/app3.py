import tkinter as tk
from tkinter import ttk

def button_func():
    input_txt=input.get()
    label["text"]=input_txt
    input["state"]="disabled"


def button_activate():
    input["state"]="enabled"
    label["text"]="Label update"



window=tk.Tk()
window.title("Text updater")
window.geometry("400x300")


# add label
label=ttk.Label(master=window,text="Label update")
label.pack()

# input
input=ttk.Entry(master=window)
input.pack()
#button
button=ttk.Button(master=window,text="Send",command=button_func)
button.pack()
# actiavte input
button_active=ttk.Button(master=window,text="activate",command=button_activate)
button_active.pack()
# run 
window.mainloop()
