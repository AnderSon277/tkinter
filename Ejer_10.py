from tkinter import *
#Funcion para imprimir los datos que se ingresaron
def show_entry_fields():
	print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="First Name").grid(row=0) 
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master) 
e2 = Entry(master)

e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)

#Este boton de accion finaliza el programa
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
#Este boton imprime el resultado acutual de los Labes en la terminal
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
