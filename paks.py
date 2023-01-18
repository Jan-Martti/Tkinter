#Jan-Martti Olop
#harjutus 4.3
#kuupäev 17.01.2023
from tkinter import *
import tkinter.messagebox

def eelarve(e):
    l = e*10+55
    return l


def lopp():
    k=sisestus.get()
    t=sisestus2.get()
    g=int(k)
    y=int(t)
    tkinter.messagebox.showinfo("eelarve",eelarve(g))
    tkinter.messagebox.showinfo("eelarve",eelarve(y)) 
    


#aken
aken = Tk()
aken.resizable(0, 0)
aken.title("Eelarce arvutamine")
aken.geometry("400x400")



#info sisestus

sisestus = Entry(aken)
sisestus.grid(row=1, column=3)

sisestus2 = Entry(aken)
sisestus2.grid(row=2, column=3)


nupp=Button(aken, text="kliki siia", command=lopp)
nupp.grid(row=3, column=1)





#k = int(input("Mitu kutsutud: "))
#t = int(input("Mitu tuleb: "))

#print("Maksimaalne eelarve: ", eelarve(k))
#print("Minimaalne eelarve: ", eelarve(t))









aken.mainloop()

