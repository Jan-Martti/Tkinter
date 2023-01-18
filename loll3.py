#Jan-Martti Olop
#11.01.2023
from tkinter import *
from tkinter import ttk



def arvuta(a):
    hind = (sisestus.get())
    arvutus = a*10+55
    tekst2.config(text=arvutus)
    arvutus2 = a*10+55
    tekst3.config(text=arvutus2)
    print(a)
    sisestus.get()
    
    
    


aken = Tk()
aken.resizable(0, 0)
aken.title("KM kalkulaator")
aken.geometry("400x400")


#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=1, column=1)

tekst = Label(aken,
              text="Mitu inimest on kutsutud: ",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=1, column=0, columnspan=1)

tekst.grid(row=1,column=0)

sisestus = Entry(aken)
sisestus.grid(row=2, column=1)

tekst = Label(aken,
              text="Mitu inimest tuleb: ",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=2, column=0, columnspan=1)

tekst.grid(row=2,column=0)

#vahe
joon = Label(aken,
              text="__________________________",
              font="Tahoma 12",
              padx=2,
              pady=2)
joon.grid(row=5, column=0, columnspan=2)

#eelarve
tekst = Label(aken,
              text="Maksimaalne eelarve:",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=6, column=0, sticky="w")

tekst2 = Label(aken,
              text="0.00€",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst2.grid(row=6, column=1, columnspan=3)


tekst = Label(aken,
              text="Minimaalne eelarve:",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=7, column=0, sticky="w")

tekst3 = Label(aken,
              text="0.00€",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst3.grid(row=7, column=1, columnspan=3)

#arvutus nupp
nupp1 = Button(aken, text="Arvuta", width=10, command=arvuta)
nupp1.grid(row=8, column=1)


aken.mainloop()



