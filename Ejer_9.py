from tkinter import * 
master = Tk()
#Se crean las etiquetas para indicar el formulario
Label(master, text="First Name").grid(row=0) 
Label(master, text="Last Name").grid(row=1)

#Indica que esas variables requieren ingreso de informacion
e1 = Entry(master) 
e2 = Entry(master)

e1.grid(row=0, column=1)  #Permite llenar en la ubicacion de la celda del FirstName
e2.grid(row=1, column=1) #Permite llenar en la ubicacion de la celda del LastName

mainloop( )
