from tkinter import * 
class App:
	#Funcion que detecta la interaccion que se tenga con los buttons
	def __init__(self, master): 
		frame = Frame(master) 
		frame.pack()
		self.button = Button(frame, text="SALIR", fg="red",command=frame.quit) #Boton de Salida
		self.button.pack(side=LEFT) 
		self.slogan = Button(frame,text="ENTRAR",command=self.write_slogan) #Boton de Entrada (Imprime el mensaje)
		self.slogan.pack(side=LEFT)
	#Esta Funcion imprime el mensaje en la terminal
	def write_slogan(self):
		print ("Estamos aprendiendo a usar Tkinter!")

root = Tk()
app = App(root) 
root.mainloop()
