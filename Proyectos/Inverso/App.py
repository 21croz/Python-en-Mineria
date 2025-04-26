import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

from math import sqrt
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.app_variables()
        self.app_styles()

        self.window_params()

        self.create_menubar()

        self.widgets_create()
        self.widgets_layout()

        self.protocol('WM_DELETE_WINDOW', self.on_closing)
    

    def app_variables(self):
        self.WIDTH = 600
        self.HEIGHT = 520
        
        self.colors = {
            'BG': '#242424',
            'BG_canvas': '#3b3b3b',
            'WHITE': '#ffffff'
        }
        
        self.df = None
        self.df_modified = None
        return
    

    def app_styles(self):
        self.style_label = {
            'bg': self.colors['BG'],
            'fg': self.colors['WHITE']
        }

        self.style_frame = {
            'bg': self.colors['BG']
        }

        self.style_entry = {
            'width': 5
        }
        return
    

    def window_params(self):
        self.title('Inverso de las distancias')

        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.resizable(False, False)

        self.config(bg = self.colors['BG'])
        return
    

    def create_menubar(self):
        self.menubar = tk.Menu(self)

        self.menubar_file = tk.Menu(self.menubar, tearoff = 0)
        self.menubar_file.add_command(label = 'Open File', command = self.open_file)
        self.menubar_file.add_separator()
        self.menubar_file.add_command(label = 'Exit', command = self.on_closing)

        self.menubar.add_cascade(label = 'File', menu = self.menubar_file)

        self.config(menu = self.menubar)
        return
    

    def widgets_create(self):
        self.frame_canvas = tk.Frame(self, height = 380, width = 450, bg = self.colors['BG_canvas'])

        self.frame_options = tk.Frame(self, **self.style_frame)
        self.label_peso = tk.Label(self.frame_options, text = 'Peso', **self.style_label)
        self.entry_peso = tk.Entry(self.frame_options, **self.style_entry)
        self.label_distance = tk.Label(self.frame_options, text = 'Distancia Max.', **self.style_label)
        self.entry_distance = tk.Entry(self.frame_options, **self.style_entry)
        self.button_calculate = tk.Button(self.frame_options, text = 'Calcular', command = self.calculate)
        return
    

    def widgets_layout(self):
        self.frame_canvas.pack(pady = 10)

        self.frame_options.pack(pady = 15)
        self.label_peso.grid(row = 0, column = 0)
        self.entry_peso.grid(row = 0, column = 1)
        self.label_distance.grid(row = 1, column = 0, pady = 5)
        self.entry_distance.grid(row = 1, column = 1)
        self.button_calculate.grid(row = 2, column = 0, columnspan = 2, pady = 5)
        return
    

    def open_file(self):
        filepath = filedialog.askopenfile()
        if filepath:
            try:
                self.df = pd.read_table(filepath, sep = ' ')
                self.df_modified = self.df.copy()
            except Exception as e:
                print(f'Error al leer el archivo: {e}')
        
        self.plot_points()
        return
    

    def plot_points(self):
        for widget in self.frame_canvas.winfo_children():
            widget.destroy()
        
        frame_width = self.frame_canvas.winfo_width()
        frame_height = self.frame_canvas.winfo_height()

        dpi = 100
        fig_width = frame_width/100
        fig_height = frame_height/100

        self.x_col = self.df['X']
        self.y_col = self.df['Y']
        self.grade_col = self.df['grade']
        
        self.fig, self.ax = plt.subplots(figsize = (fig_width, fig_height), dpi = dpi)
        
        scatter = self.ax.scatter(self.x_col, self.y_col, c = self.grade_col, cmap = 'RdYlGn', marker = 's', s = 1)        
        self.ax.set_title('Ley de Cu')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.grid(False)

        cbar = self.fig.colorbar(scatter, ax = self.ax)
        cbar.set_label('Ley')

        self.canvas = FigureCanvasTkAgg(self.fig, master = self.frame_canvas)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill = 'both', expand = True)
        return
    

    def calculate(self):
        self.peso = int(self.entry_peso.get())
        self.dist_max = int(self.entry_distance.get())

        self.x_col = self.df['X']
        self.y_col = self.df['Y']
        self.grade_col = self.df['grade']

        self.data = list(zip(self.x_col, self.y_col, self.grade_col))
        
        self.add_rows()
        return
    

    def add_rows(self):
        coords = set((row.X, row.Y) for row in self.df.itertuples(index = False))
        print(coords)

        for x in range(-100, 101):
            for y in range(-100, 101):
                if (x, y) not in coords:
                    grade = self.inverso_distancia(x, y, self.data, self.dist_max, self.peso)
                    new_row = pd.DataFrame([{'X': x, 'Y': y, 'grade': grade}])
                    self.df_modified = pd.concat([self.df_modified, new_row], ignore_index = True)

        self.update_plot()
        return


    def inverso_distancia(self, x1, y1, data, dist_max = 50, peso=1):
        numerador = 0
        denominador = 0

        for item in data:
            distancia = sqrt((x1 - item[0])**2 + (y1 - item[1])**2)
            if distancia <= dist_max:
                numerador += item[2]/(distancia**peso)
                denominador += 1/(distancia**peso)

        return numerador/denominador
    

    def update_plot(self):
        for widget in self.frame_canvas.winfo_children():
            widget.destroy()
        
        frame_width = self.frame_canvas.winfo_width()
        frame_height = self.frame_canvas.winfo_height()

        dpi = 100
        fig_width = frame_width/100
        fig_height = frame_height/100

        self.x_col = self.df_modified['X']
        self.y_col = self.df_modified['Y']
        self.grade_col = self.df_modified['grade']
        
        self.fig, self.ax = plt.subplots(figsize = (fig_width, fig_height), dpi = dpi)
        
        scatter = self.ax.scatter(self.x_col, self.y_col, c = self.grade_col, cmap = 'RdYlGn', marker = 's', s = 1)        
        self.ax.set_title('Ley de Cu')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.grid(False)

        cbar = self.fig.colorbar(scatter, ax = self.ax)
        cbar.set_label('Ley')

        self.canvas = FigureCanvasTkAgg(self.fig, master = self.frame_canvas)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill = 'both', expand = True)
        return
    

    def on_closing(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.destroy()
        self.quit()
        return



if __name__ == '__main__':
    app = Main()
    app.mainloop()