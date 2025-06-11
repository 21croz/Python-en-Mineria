import tkinter as tk
import pandas as pd

from tkinter import ttk, filedialog, messagebox



# 0. Variables Globales
df = None



def open_file():
    global df

    ruta_archivo = filedialog.askopenfilename(title = "Abrir archivo")
    if ruta_archivo:
        df = pd.read_csv(ruta_archivo, sep = ';')
        messagebox.showinfo("Archivo cargado", "Se ha cargado el archivo correctamente.")
        after_read()
    return

def after_read():
    global combo_size_x, combo_size_y, combo_size_z

    combo_values = df.columns.tolist()

    combo_size_x['values'] = combo_values
    combo_size_y['values'] = combo_values
    combo_size_z['values'] = combo_values

    combo_size_x.config(state = 'readonly')
    combo_size_y.config(state = 'readonly')
    combo_size_z.config(state = 'readonly')
    return



# 1. Crear ventana
root = tk.Tk()



# 2. Parametros de la ventana.
root.title("Clase 7.2 - Combobox")
root.geometry("800x600")
root.resizable(False, False)



# 3. Crear widgets.
boton_abrir_archivo = tk.Button(root, text = "Abrir archivo", command = open_file)

frame_combo = tk.Frame(root)
combo_size_x = ttk.Combobox(frame_combo, state = 'disabled')
label_size_x = tk.Label(frame_combo, text = "Tamaño x")
combo_size_y = ttk.Combobox(frame_combo, state = 'disabled')
label_size_y = tk.Label(frame_combo, text = "Tamaño y")
combo_size_z = ttk.Combobox(frame_combo, state = 'disabled')
label_size_z = tk.Label(frame_combo, text = "Tamaño z")



# 4. Colocar widgets
boton_abrir_archivo.pack(pady = 20)

frame_combo.pack(pady = 20)
combo_size_x.grid(row = 0, column = 0, pady = 5)
label_size_x.grid(row = 0, column = 1, pady = 5)
combo_size_y.grid(row = 1, column = 0, pady = 5)
label_size_y.grid(row = 1, column = 1, pady = 5)
combo_size_z.grid(row = 2, column = 0, pady = 5)
label_size_z.grid(row = 2, column = 1, pady = 5)



# 5. Crear barra de menú
menubar = tk.Menu(root)

menubar_file = tk.Menu(menubar, tearoff = 0)
menubar_file.add_command(label = 'Abrir archivo', command = open_file)

menubar.add_cascade(label = 'Archivo', menu = menubar_file)

root.config(menu = menubar)



# 6. Mainloop de la ventana.
root.mainloop()