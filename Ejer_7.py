from tkinter import * 
master = Tk()
var1 = IntVar()
#Se dan las caracteristicas de la primera opcion
Checkbutton(master, text="Hombre", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
#Se dan las caracteristicas de la segunda opcion
Checkbutton(master, text="Mujer", variable=var2).grid(row=1, sticky=W)
mainloop()
