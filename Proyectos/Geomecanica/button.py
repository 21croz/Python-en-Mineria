import tkinter as tk



class AppButton(tk.Frame):
    """
    Botón personalizado usado dentro de la ventana principal.
    Se crea un >>>tk.Frame, el cual en su interior contiene un botón.
    El frame cumple la funcitón de mostrarse como el borde del botón.
    """
    def __init__(self, parent, text, bg = '#a55eea', highlightbackground = '#8854d0', command = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.bg = bg
        self.highlightbackground = highlightbackground

        # Configuración del frame.
        self.config(
            highlightbackground = self.highlightbackground,     # Color del borde del botón
            highlightthickness = 3,                             # Grosor del borde del botón
            bd = 0                                              # Borde del frame
            )

        # Configuración del botón dentro del frame.
        button = tk.Button(
            self,
            text = text,                # Texto del botón
            bg = self.bg,             # Color del botón
            fg = 'black',               # Color del texto del botón
            width = 15,                 # Ancho del botón
            border = 0,                 # Borde del botón
            cursor = 'hand2',           # Cursor al pasar el mouse
            command = command           # Función a ejecutar al hacer click
            )
        button.pack()