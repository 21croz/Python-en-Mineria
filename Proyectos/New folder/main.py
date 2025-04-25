import tkinter as tk



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x800')

        self.button_interfaz = tk.Button(self, text = 'Presioname', font = ('Arial', 20), command = self.accion)
        self.button_interfaz.pack()
    

    def accion(self):
        print('Hola Mundo')



if __name__ == '__main__':
    app = App()
    app.mainloop()