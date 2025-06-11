import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(f"800x800")
        self.entry = tk.Entry(self)
        self.entry.pack(pady = 50)

        self.frame_boton = tk.Frame(self)
        self.frame_boton.pack(pady = 10)

        self.button = tk.Button(self.frame_boton, text = 'Presioname', command = self.comando_boton)
        self.button.pack(pady = 10)
    

    def comando_boton(self):
        contenido = self.entry.get()
        print(f"El contenido del entry es {contenido}")
        return


if __name__ == '__main__':
    app = App()
    app.mainloop()