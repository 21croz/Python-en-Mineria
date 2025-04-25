import tkinter as tk

from settings import *
from button import AppButton


class Litostatica:
    def __init__(self, parent):
        self.parent = parent

        self.window_params()
        return
    

    def window_params(self):
        self.y_sep = 3
        self.x_sep = 15
        return
    

    def run(self):
        self.widgets_define()
        self.widgets_layout()
        return
    

    def widgets_define(self):
        self.label_title_lito = tk.Label(self.parent, text = 'Litostática', **style_subtitle)
        
        self.frame_entries = tk.Frame(self.parent, bg = BG_COLOR)

        
        self.label_rho = tk.Label(self.frame_entries, text = 'Densidad', **style_label_options)
        self.entry_rho = tk.Entry(self.frame_entries, **style_entry)
        self.label_rho_measure = tk.Label(self.frame_entries, text = 't/m³', **style_label_options)
        
        self.label_g = tk.Label(self.frame_entries, text = 'Gravedad', **style_label_options)
        self.entry_g = tk.Entry(self.frame_entries, **style_entry)
        self.label_g_measure = tk.Label(self.frame_entries, text = 'm/s²', **style_label_options)
        
        self.label_h = tk.Label(self.frame_entries, text = 'Altura', **style_label_options)
        self.entry_h = tk.Entry(self.frame_entries, **style_entry)
        self.label_h_measure = tk.Label(self.frame_entries, text = 'm', **style_label_options)


        self.button_lito_calc = AppButton(self.parent, text = 'Calcular', command = self.litostatica_calc)

        self.label_lito_result = tk.Label(self.parent, text = '', **style_label_result)
        return
    

    def widgets_layout(self):
        self.label_title_lito.pack(pady = (20, 5))

        self.frame_entries.pack()
        
        
        self.label_rho.grid(row = 0, column = 0, pady = self.y_sep, sticky = 'w')
        self.entry_rho.grid(row = 0, column = 1, pady = self.y_sep, padx = self.x_sep)
        self.label_rho_measure.grid(row = 0, column = 2, pady = self.y_sep)
        
        self.label_g.grid(row = 1, column = 0, pady = self.y_sep, sticky = 'w')
        self.entry_g.grid(row = 1, column = 1, pady = self.y_sep, padx = self.x_sep)
        self.label_g_measure.grid(row = 1, column = 2, pady = self.y_sep)
        
        self.label_h.grid(row = 2, column = 0, pady = self.y_sep, sticky = 'w')
        self.entry_h.grid(row = 2, column = 1, pady = self.y_sep, padx = self.x_sep)
        self.label_h_measure.grid(row = 2, column = 2, pady = self.y_sep)


        self.button_lito_calc.pack(pady = 20)

        self.label_lito_result.pack(pady = 20)
        return
    

    def litostatica_calc(self):
        try:
            rho = float(self.entry_rho.get())*1000      # Convertir de t/m^3 a kg/m^3
            g = float(self.entry_g.get())               # [m/s^2]
            h = float(self.entry_h.get())               # [m]
        except:
            return
        
        resultado = rho*g*h                         # [Pa]
        self.label_lito_result.config(text = f'{resultado/1000000:.4f} [MPa]')
        return