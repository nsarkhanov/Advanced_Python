import tkinter as tk
import ttkbootstrap as ttk

def convert():
    miles=input_text.get()
    km=miles*1.61
    output_var.set(km)

#window
#window=tk.Tk() default   tkinter windwos 
window=ttk.Window(themename="superhero")
window.title("Demo")
window.geometry("500x200")


# adding  title in frame 
title=ttk.Label(master=window,text="Miles to Kilometers Convertor",font="Calibri 16")
title.pack(pady=5)
 # adding input  and convertor button  and widget

# input_frame=ttk.Entry(master=window)
input_frame=ttk.Frame(master=window)
input_text=tk.IntVar()
input=ttk.Entry(master=input_frame,textvariable=input_text,)
input.pack(side="left",padx=10)
button=ttk.Button(master=input_frame,text="convert",command=convert)
button.pack(side="left")
input_frame.pack(pady=10)

# output section 

output_var=tk.StringVar()
output_label=ttk.Label(master=window,textvariable=output_var)
output_label.pack()


window.mainloop()