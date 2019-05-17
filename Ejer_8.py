from tkinter import * 
master = Tk()

#Define el texto de las opciones
def var_states():
	print (" male: ",var1.get())
	print ("female: ",var2.get())

#Crea la ventana con los cehckbutton
Label(master, text="Indicar el sexo:").grid(row=0, sticky=W) 
var1 = IntVar() #Se instancia la 1era opcion
Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar() #Se instancia la 2da opcion
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)

#Boton de comando para salir del programa
Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, padx=4)
#Boton de comando para imprimir el resultado actual de los checkboton en la termianal
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
mainloop()
