from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
root=Tk()
root.title("AIRPORT REGISTRAION")
root.geometry('300x250')
root.configure(bg="skyBlue")
b="INDIA"
selected=IntVar()

def name():
    userx=str(enum2.get())
    # lres.config(text=str(), bg='Orange')

def king():
    userz = str(enum4.get())
    users = str(enum5.get())
    usery = str(enum3.get())
    usern = str(enum7.get())
def myfun():
    user=str(combo.get())
    try:
        a="INDIA"
        if a==user:
            messagebox.showinfo("message","!!!!!PADHARO MHARE DESH!!!!!")
        else:
            messagebox.showerror("message","You are Not From India")
    except ValueError:
        messagebox.showerror("Error","Enter Only Numbers")


lnum7=Label(root,text="SELECT CLASS",font=("Arial",12,"bold"))
lnum7.place(x=45,y=5)
combo= Combobox(root,font=("Arial",12,"bold"))
combo['value']=("ECONOMY","PREMIUM ECONOMY","BUSINESS")
combo.place(x=250,y=5)

lnum7=Label(root,text="Travellers",font=("Arial",12,"bold"))
lnum7.place(x=490,y=5)
combo= Combobox(root,font=("Arial",12,"bold"))
combo['value']=(1,2,3,4,5,6,7)
combo.place(x=600,y=5)

lnum7=Label(root,text="DATE",font=("Arial",12,"bold"))
lnum7.place(x=490,y=35)
enum7=Entry(root,font=("Arial",12,"bold"))
enum7.place(x=600,y=35)

lnum3=Label(root,text="YOUR FIRST NAME",font=("Arial",12,"bold"))
lnum3.place(x=20,y=35)
enum3=Entry(root,font=("Arial",12,"bold"))
enum3.place(x=250,y=35)

lnum2=Label(root,text="YOUR MIDDLE NAME",font=("Arial",12,"bold"))
lnum2.place(x=7,y=65)
enum2=Entry(root,font=("Arial",12,"bold"))
enum2.place(x=250,y=65)

lnum4=Label(root,text="YOUR LAST NAME",font=("Arial",12,"bold"))
lnum4.place(x=23,y=95)
enum4=Entry(root,font=("Arial",12,"bold"))
enum4.place(x=250,y=95)

lnum5=Label(root,text="ENTER YOUR AGE",font=("Arial",12,"bold"))
lnum5.place(x=25,y=125)
enum5=Entry(root,font=("Arial",12,"bold"))
enum5.place(x=250,y=125)

lnum1=Label(root,text="ENTER COUNTRY",font=("Arial",12,"bold"))
lnum1.place(x=27,y=155)
combo=Combobox(root,font=("Arial",12,"bold"))
combo['value']=("INDIA","PAKISTAN","AFGANISTAN","USA")
combo.place(x=250,y=155)
#
lnum1=Label(root,text="ENTER GENDER",font=("Arial",12,"bold"))
lnum1.place(x=37,y=185)
rad1=Radiobutton(root,text='Male',value=1,variable=selected)
rad1.place(x=250,y=185)
rad2=Radiobutton(root,text='Female',value=2,variable=selected)
rad2.place(x=350,y=185)

btn=Button(root,text="SUBMIT",command=myfun)
btn.place(x=300,y=220)


lres=Label(root,text="")


root.mainloop()