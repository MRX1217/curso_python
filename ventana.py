#imporatamos libreria TKinter
import tkinter

#creamos el objeto ventana
ventana = tkinter.Tk()

#le ponemos un titulo a la ventana
ventana.title("ventana")

ventana.resizable()

#Le asignamos un tamaño
ventana.geometry("500x500")

#La funcion mainloop permite visualizar nuestra ventana
ventana.mainloop()
