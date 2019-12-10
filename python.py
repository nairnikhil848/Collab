from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("450x450")
test=Label(window ,text="")
name=Label(window ,text="Name").grid(row=1,column=4)
name_in=Entry(window)
name_in.grid(row=1,column=5)
mob=Label(window,text="MobileNO" ).grid(row=2,column=4)
mob_in=Entry(window)
mob_in.grid(row=2,column=5)
add=Label(window,text="Address" ).grid(row=3,column=4)
add_in=Entry(window)
add_in.grid(row=3,column=5)
email=Label(window,text="Email.ID" ).grid(row=4,column=4)
email_in=Entry(window)
email_in.grid(row=4,column=5)

def check():
    if name_in.get()=="":
        messagebox.showinfo(title="Ohh boi", message="Enter name")
        return
    else:
        print(name_in.get()) 

    if mob_in.get()=="":
        messagebox.showinfo(title="Ohh boi", message="Enter Mobile no")  
        return    
    if mob_in.get().isdigit():
        if len(mob_in.get())==10:
            print(mob_in.get())
        else:
            messagebox.showinfo(title="Ohh boi", message="Enter a valid number")
            return   
    else:
        messagebox.showinfo(title="Ohh boi", message="Number not text")
        return


    print(add_in.get())

    if email_in.get().endswith("gmail.com"):
        print(email_in.get())      
    else:
        messagebox.showinfo(title="Ohh boi", message="Enter valid mail")
        return
def fndelete():
    name_in.delete(first=0,last=END)
    add_in.delete(first=0,last=END)
    mob_in.delete(first=0,last=END)
    email_in.delete(first=0,last=END)


botton=Button(window,text="Submit" ,fg="white",bg="black",bd="5px" ,command=check).grid(row=5,column=5)
botton1=Button(window,text="Clear" ,fg="white",bg="black",bd="5px" ,command=fndelete).grid(row=5,column=6)
window.mainloop()