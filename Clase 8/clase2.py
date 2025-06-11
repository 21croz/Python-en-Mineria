import tkinter as tk



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_variables()
        self.window_settings()
        
        self.widgets_create()
        self.widgets_layout()
        return
    

    def window_variables(self):
        self.WIDTH = 800
        self.HEIGHT = 600

        self.var_camion = tk.IntVar()
        self.var_pala = tk.IntVar()
        self.var_dozer = tk.IntVar()
        return
    

    def window_settings(self):
        self.title("Clase 8 - Checkbuttons.")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        return
    

    def widgets_create(self):
        self.label_title = tk.Label(self, text = "Clase 8.2 - Checkbuttons", font = ("Times New Roman", 30))
        
        self.frame_check = tk.Frame(self)
        self.check_camion = tk.Checkbutton(self.frame_check, text = "Camión", variable = self.var_camion)
        self.check_pala = tk.Checkbutton(self.frame_check, text = "Pala", variable = self.var_pala)
        self.check_dozer = tk.Checkbutton(self.frame_check, text = "Buldócer", variable = self.var_dozer)
        
        self.button_text = tk.Button(self, text = "Siguiente", command = self.selected_check)
        return
    

    def widgets_layout(self):
        self.label_title.pack(pady = 15)

        self.frame_check.pack()
        self.check_camion.pack()
        self.check_pala.pack()
        self.check_dozer.pack()

        self.button_text.pack(pady = 10)
        return
    

    def selected_check(self):
        # Leer la entrada del usuario.
        # Pasar a la siguiente ventana.
        # Hacer el todo el cálculo para estimar el mejor método.

        # selected = []

        # if self.var_camion.get():
        #     selected.append("Camion")
        # if self.var_pala.get():
        #     selected.append("Pala")
        # if self.var_dozer.get():
        #     selected.append("Buldócer")

        # print(selected)
        return



if __name__ == "__main__":
    app = App()
    app.mainloop()