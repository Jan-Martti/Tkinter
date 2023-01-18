#Jan-Martti Olop
#11.01.2023

from tkinter import *

#akna loomine
aken = Tk()
aken.title("kahtlane lipp")

#lõuend
louend = Canvas(aken, width=500, height=300)
louend.pack()

#lipu tegemine
louend.create_rectangle(0, 0, 500, 150,fill="orange")
louend.create_rectangle(0, 150, 500, 300,fill="black")
louend.create_polygon(0, 0, 250, 150, 0, 300,fill="purple")









aken.mainloop()
