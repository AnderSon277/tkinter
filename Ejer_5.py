from tkinter import * 
root = Tk()
v = IntVar()
v.set(1)	# initializing the choice, i.e. Python
#Se creean las opciones con su numero 
languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]
#Imprimer el numero de la opcion en la terminal
def ShowChoice(): 
	print (v.get())
#Crea la ventana de interaccion 
Label(root,
	text="""Choose your favourite programming language:""",
	justify = LEFT,
	padx = 20).pack()

#Este ciclo define que opcion se selecciona para 
#dar lugar ba la funcion ShowChoice
for txt, val in languages: 
	Radiobutton(root,
		text=txt, 
		padx = 30, 
		variable=v,
		command=ShowChoice, 
		value=val).pack(anchor=W)

mainloop()
