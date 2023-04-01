import  tkinter as tk   # basic models 
# from tkinter import ttk  # get widgets
import ttkbootstrap as ttk



def convert():
     ml=1.66*entry_int.get()
     output_int.set(f"{round(ml,1)} km")

#window
window=ttk.Window(themename="darkly")
window.title("Demo")
window.geometry("500x200")


# title
title_label=ttk.Label(master=window,text="Mile to kilometers",font="Calibri 16")
title_label.pack() # addinf to windwos
#input field
input_frame=ttk.Frame(master=window)
entry_int=tk.IntVar()
entry=ttk.Entry(master=input_frame,textvariable=entry_int)
button=ttk.Button(master=input_frame,text="Convert" ,command=convert)
entry.pack(side="left",padx=10)
button.pack(side="left")
input_frame.pack(pady=10)
#output
output_int=tk.StringVar()
output_label=ttk.Label(master=window,text="Output",textvariable=output_int,foreground="red",font="Calibri 14 bold")
output_label.pack(pady=5)
#run
window.mainloop()