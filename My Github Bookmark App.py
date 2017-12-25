import tkinter as tk
import webbrowser

def github(event):
    webbrowser.open_new_tab('https://github.com/ashwinjoy')

window=tk.Tk()
window.geometry("300x200")

label1=tk.Label(text="Ashwin's Github is here")
label1.grid(column=0,row=0)

button=tk.Button(window,text="GitHub")
button.grid(column=0,row=4)

button.bind("<Button-1>",github)

window.mainloop()
    
