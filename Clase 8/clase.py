import tkinter as tk



class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_variables()
        self.window_settings()

        self.widgets_create()
        self.widgets_layout()
    

    def window_variables(self):
        self.WIN_WIDTH = 800
        self.WIN_HEIGHT = 600

        self.var_radios = tk.StringVar(value = "Cielo")
        return
    

    def window_settings(self):
        self.title("Clase 8 - Radiobuttons")
        self.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")
        self.resizable(False, False)
        return
    

    def widgets_create(self):
        self.label_title = tk.Label(self, text = "Radiobuttons", font = ('Arial', 20, 'bold'))

        self.frame_radios = tk.Frame(self)
        self.radio_cielo = tk.Radiobutton(self.frame_radios, text = "Cielo Abierto", value = "Cielo", variable = self.var_radios, command = self.selected_radio)
        self.radio_subte = tk.Radiobutton(self.frame_radios, text = "Subterránea", value = "Subte", variable = self.var_radios, command = self.selected_radio)
        
        self.label_resultado = tk.Label(self, text = "")
        return
    

    def widgets_layout(self):
        self.label_title.pack(pady = 15)

        self.frame_radios.pack()
        self.radio_cielo.pack()
        self.radio_subte.pack()

        self.label_resultado.pack(pady = 10)
        return
    

    def selected_radio(self):
        click = self.var_radios.get() # "Cielo" ó "Subte"

        if click == "Cielo":
            self.label_resultado.config(text = "Has seleccionado Cielo.")
        elif click == "Subte":
            self.label_resultado.config(text = "Has seleccionado Subterránea.")
        return



if __name__ == "__main__":
    win = MainWindow()
    win.mainloop()