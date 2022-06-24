import tkinter
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo, showerror
import cv2
import numpy as np
from os import listdir
import requests
from os.path import isfile, join

master = tkinter.Tk()
master.geometry("390x350")
flag = 0


def reco():
    print("access granted")
def login():
    if lblpassword.get() == "123" and lblusername.get()=="bhavya":
        reco()
    else:
        print("access denied")


bg_color = "DeepSkyBlue2"
fg_color = "#383a39"
master.configure(background=bg_color)
master.title("Welcome")
# ---heading image
# photo = ImageTk.PhotoImage(Image.open("car.jpg"))
# tkinter.Label(master, image=photo).grid(rowspan = 3, columnspan = 5, row =0,column = 0)
# -------username
tkinter.Label(master, text="Username:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=8, padx=(50, 0),
                                                                                               pady=(20, 10))
lblusername = tkinter.Entry(master)
lblusername.grid(row=8, column=1, padx=(10, 10), pady=(20, 10))
# ----password
tkinter.Label(master, text="Password:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=9, padx=(50, 0),
                                                                                               pady=(20, 10))
lblpassword = tkinter.Entry(master)
lblpassword.grid(row=9, column=1, padx=(10, 10), pady=(20, 10))

# --------button
tkinter.Button(master, text="Login", borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width=15,
               command=login).grid(row=10, padx=(50, 0), pady=(20, 10))
# print(flag)
# print(con)
master.mainloop()


# elon,10:46:32
# JACKMA,10:53:05
# JEFFBEZOS,10:53:09
# ELONMUSK,10:53:19
# BILLGATES,10:53:22