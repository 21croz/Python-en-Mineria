import tkinter as tk
from tkinter import messagebox



class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_variables()
        self.window_settings()

        self.widgets_create()
        self.widgets_layout()
    

    def window_variables(self):
        self.WIDHT, self.HEIGHT = 400, 400
        return
    

    def window_settings(self):
        self.title("Validacion de entradas")
        self.geometry(f"{self.WIDHT}x{self.HEIGHT}")
        return
    

    def widgets_create(self):
        self.label_numero = tk.Label(self, text = 'Numero')
        self.entry_numero = tk.Entry(self)

        self.label_texto = tk.Label(self, text = 'Texto')
        self.entry_texto = tk.Entry(self)

        self.button_final = tk.Button(self, text = 'Verificar', command = self.verificar_entradas)
        return
    

    def widgets_layout(self):
        self.label_numero.grid(row = 0, column = 0)
        self.entry_numero.grid(row = 0, column = 1)

        self.label_texto.grid(row = 1, column = 0)
        self.entry_texto.grid(row = 1, column = 1)

        self.button_final.grid(row = 2, column = 0, columnspan = 2)
        return
    

    def validate_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
        
    
    def validate_text(self, value):
        if value.isalpha() or value == "":
            return True
        return False
        

    def verificar_entradas(self):
        text_value = self.entry_texto.get()
        number_value = self.entry_numero.get()

        if not self.validate_text(text_value):
            messagebox.showerror("Error", "Ingresaste un número en el Entry de texto")
            return
        
        if not self.validate_number(number_value):
            messagebox.showerror("Error", "Ingresaste texto en el Entry de números")
            return
        return



if __name__ == '__main__':
    root = MainWindow()
    root.mainloop()