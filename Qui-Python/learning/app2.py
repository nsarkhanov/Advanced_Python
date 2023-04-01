import tkinter as tk
from tkinter import ttk
def print_fucntion():
    print("Sent data")


#create window
windows=tk.Tk()
windows.title("Widgets")
windows.geometry("800x700")

#create widget
label=ttk.Label(master=windows,text="My label")
label.pack(pady=5)
# adding big text box 
text_box=tk.Text(master=windows)
text_box.pack()                 
# addinf label 
lable_b=ttk.Label(master=windows,text="My label")
lable_b.pack(pady=5)
# adding entry line 
input_=tk.StringVar()
input_text=ttk.Entry(master=windows,textvariable=input_)
input_text.pack(pady=5)
# adding button 
button=ttk.Button(master=windows,text="Send",command=print_fucntion)
button.pack(pady=1)
#run 
windows.mainloop()