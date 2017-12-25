import tkinter as tk

def fruit(event):
    print("Mangoes are juicier than tomatoes ")

window=tk.Tk()
window.geometry("300x300")

newlabel=tk.Label(text=" Mangoes are juicy ")
newlabel.grid(column=3,row=5)

button=tk.Button(text="  Smash! ")
button.grid(column=3)



button.bind("<Button-1>",fruit)


window.mainloop()
