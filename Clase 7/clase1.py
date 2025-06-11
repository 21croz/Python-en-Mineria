import tkinter as tk

from tkinter import ttk



# Crear variables globales.
contador = 1



def add_rows():
    global contador

    nombre = f"Persona {contador}"
    edad = str(20 + contador)
    tree.insert("", "end", values = (nombre, edad))
    contador += 1
    return



# Creamos nuestra ventana.
root = tk.Tk()



# Parametros de la ventana.
root.title("Clase 7.1 - Treeviews")
root.geometry("800x600")
root.resizable(False, False)



# Crear los widgets.
frame_tree = tk.Frame(root)

scrollbar_tree = ttk.Scrollbar(frame_tree, orient = 'vertical')
tree = ttk.Treeview(frame_tree, columns = ("Nombre", "Edad"), show = 'headings', yscrollcommand = scrollbar_tree.set)

boton_filas = tk.Button(root, text = 'Añadir Filas', command = add_rows)



# Colocamos los widgets.
frame_tree.pack()

scrollbar_tree.pack(side = 'right', fill = 'y')
tree.pack(side = 'left', expand = 'True', fill = 'both')
scrollbar_tree.config(command = tree.yview)

boton_filas.pack(pady = 20)



# Mainloop de la ventana.
root.mainloop()