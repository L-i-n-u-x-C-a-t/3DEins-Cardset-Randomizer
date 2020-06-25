import random
from tkinter import *
from tkinter.messagebox import *

def removeblanklines(): #This removes the blank lines
    with open("gfx/cards.t3s","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if line != "\n":
                f.write(line)
        f.truncate()


def randomizer():
    removeblanklines()
    with open("gfx/cards.t3s","r") as f:
        readed = f.readlines()
        table = readed[1:] #Set a list with all the lines except line 1
        shuftable = random.sample(table, len(table)) #randomizes table into shuftable
        shuftable.insert(0, "--atlas -f rgba8888 -z auto")

    with open("gfx/cards.t3s","r+") as f:
        for item in shuftable:
            f.write("%s\n" % item)
    removeblanklines() #removing lines again to make a clean file
    if askyesno('Randomizing finished !', 'Do you want to exit the app now?'):
        win.destroy()

def tryexcept():
    try:
        randomizer()
    except FileNotFoundError:
        showerror("Error", "gfx/cards.t3s not found. Make sure you run this in the Card_Generator folder.")


win = Tk()
win.title("")
win.geometry('250x175')
title = Label(win, text = "3DEins Card randomizer", font="bold")
title.place(x=30, y=20)
randombutton = Button(win, text = "Randomize cards!", command = tryexcept)
randombutton.place(height=50, width=150, x=50, y=60)
runmake = Label(win, text = "Don't forget to run\nmake after that!")
runmake.place(x=60, y=125)
win.mainloop()
