import datetime
import tkinter as tk

#window
window=tk.Tk()
window.geometry("620x480")
window.title(" Age Calculator App ")

#labels
nlabel=tk.Label(text="Name")
nlabel.grid(column=0,row=1)
ylabel=tk.Label(text="Year")
ylabel.grid(column=0,row=2)
mlabel=tk.Label(text="Month")
mlabel.grid(column=0,row=3)
ylabel=tk.Label(text="Day")
ylabel.grid(column=0,row=4)

#entry_fields
nentry=tk.Entry()
nentry.grid(column=1,row=1)
yentry=tk.Entry()
yentry.grid(column=1,row=2)
mentry=tk.Entry()
mentry.grid(column=1,row=3)
dentry=tk.Entry()
dentry.grid(column=1,row=4)

def banana():
    name=nentry.get()
    monkey=Person(name,datetime.date(int(yentry.get()),int(mentry.get()),int(dentry.get())))
    print(monkey.age())
    #text
    texter=tk.Text(master=window,height=10,width=25)
    texter.grid(column=1,row=6)
    answer=" {monkey} is {age} years old!!! ".format(monkey=name, age=monkey.age())
    texter.insert(tk.END,answer)

        
#button
button=tk.Button(window,text="Calculate Age",command=banana)
button.grid(column=1,row=5)

class Person:
    def __init__(self,name,birthdate):
        self.name=name
        self.birthdate=birthdate

    def age(self):
        today=datetime.date.today()
        age=today.year-self.birthdate.year
        return age
    


window.mainloop()
