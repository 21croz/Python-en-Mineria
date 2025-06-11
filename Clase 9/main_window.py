'''
En este archivo deberá crear la ventana principal de la aplicación.
Implemente el diseño de la imagen "main_window.png". Cuando presione
el botón "Roca", se deberá abrir una ventana secundaria con el diseño
del archivo rock_database.py.
'''
import tkinter as tk
from rock_database import RockDatabase



class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_parameters()
        self.window_settings()

        self.widgets_create()
        self.widgets_layout()

    
    def window_parameters(self):
        self.WIDTH = 500
        self.HEIGHT = 300
        return
    

    def window_settings(self):
        self.title("Ventana Principal")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        return
    

    def widgets_create(self):
        self.label_title = tk.Label(self, text = "Bases de datos", font = ('Times New Roman', 25, 'bold'))
        
        self.frame_buttons = tk.Frame(self)
        self.button_rock = tk.Button(self.frame_buttons, text = 'Roca', font = ('Arial', 15), width = 20, command = self.open_rock_database)
        self.button_explosive = tk.Button(self.frame_buttons, text = 'Explosivos', font = ('Arial', 15), width = 20)
        self.button_teams = tk.Button(self.frame_buttons, text = 'Equipos', font = ('Arial', 15), width = 20)
        return
    

    def widgets_layout(self):
        self.label_title.pack(anchor = 'w')

        self.frame_buttons.pack(pady = 20)
        self.button_rock.pack(pady = 5)
        self.button_explosive.pack(pady = 5)
        self.button_teams.pack(pady = 5)
        return
    

    def open_rock_database(self):
        win = RockDatabase(self)
        return



if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()