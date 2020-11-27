import tkinter as tk
import dframe as df
import Admin as adm
from tkinter import ttk
from Admin import *
from tkinter import *
from dframe import *

def reg_server(root,frame1,name,sex,zone,city,passw):
    if(passw=='' or passw==' '):
        msg = Message(frame1, text="Error: Missing Fileds", width=500)
        msg.grid(row = 10, column = 0, columnspan = 5)
        return -1

    vid = df.taking_data_voter(name, sex, zone, city, passw)
    for widget in frame1.winfo_children():
        widget.destroy()
    txt = "Registered Voter with\n\n VOTER I.D. = " + str(vid)
    Label(frame1, text=txt, font=('Helvetica', 18, 'bold')).grid(row = 2, column = 1, columnspan=2)


def Register(root,frame1):

    root.title("Register Voter")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Register Voter", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    #Label(frame1, text="Voter ID:      ", anchor="e", justify=LEFT).grid(row = 2,column = 0)
    Label(frame1, text="Name:         ", anchor="e", justify=LEFT).grid(row = 3,column = 0)
    Label(frame1, text="Sex:              ", anchor="e", justify=LEFT).grid(row = 4,column = 0)
    Label(frame1, text="Zone:           ", anchor="e", justify=LEFT).grid(row = 5,column = 0)
    Label(frame1, text="City:             ", anchor="e", justify=LEFT).grid(row = 6,column = 0)
    Label(frame1, text="Password:   ", anchor="e", justify=LEFT).grid(row = 7,column = 0)

    #voter_ID = tk.StringVar()
    name = tk.StringVar()
    sex = tk.StringVar()
    zone = tk.StringVar()
    city = tk.StringVar()
    password = tk.StringVar()

    #e1 = Entry(frame1, textvariable = voter_ID).grid(row = 2, column = 2)
    e2 = Entry(frame1, textvariable = name).grid(row = 3, column = 2)
    e5 = Entry(frame1, textvariable = zone).grid(row = 5, column = 2)
    e6 = Entry(frame1, textvariable = city).grid(row = 6, column = 2)
    e7 = Entry(frame1, textvariable = password).grid(row = 7, column = 2)

    e4 = ttk.Combobox(frame1, textvariable = sex, width=17)
    e4['values'] = ("Male","Female","Transgender")
    e4.grid(row = 4, column = 2)
    e4.current()

    reg = Button(frame1, text="Register", command = lambda: reg_server(root, frame1, name.get(), sex.get(), zone.get(), city.get(), password.get()), width=10)
    Label(frame1, text="").grid(row = 8,column = 0)
    reg.grid(row = 9, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         Register(root,frame1)
