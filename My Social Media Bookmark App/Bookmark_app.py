import tkinter as tk
import webbrowser

def github(event):
    webbrowser.open_new_tab('https://github.com/ashwinjoy')
def linkedin(event):
    webbrowser.open_new_tab('https://www.linkedin.com/in/ashwinjoy/')
def facebook(event):
    webbrowser.open_new_tab('https://m.facebook.com/ashwin.joy.12')
window=tk.Tk()
window.geometry("300x200")
window.title("Social Media Bookmark App")

label1=tk.Label(text="My Social Media")
label1.grid(column=0,row=0)

button1=tk.Button(window,text="GitHub",bg="yellow")
button1.grid(column=1,row=1)
button2=tk.Button(window,text="Linkedin",bg="orange")
button2.grid(column=3,row=1)
button3=tk.Button(window,text="Facebook",bg="pink")
button3.grid(column=5,row=1)

button1.bind("<Button-1>",github)
button2.bind("<Button-1>",linkedin)
button3.bind("<Button-1>",facebook)

window.mainloop()
    
