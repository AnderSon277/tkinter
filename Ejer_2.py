from tkinter import * 
master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you doit.\n(Mahatma Gandhi)" #Guarda el text en una variable
msg = Message(master, text = whatever_you_do) #Crea la ventana del mensaje
msg.config(bg='lightgreen', font=('times', 24, 'italic')) #Cambia el color y formato de letra
msg.pack( )
mainloop( )
