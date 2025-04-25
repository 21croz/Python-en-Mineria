import tkinter as tk
from tkinter import ttk

from math import exp, tan, radians, sin
from settings import *
from button import AppButton



class Janssen:
    def __init__(self, parent):
        self.parent = parent

        self.window_params()
        return
    

    def window_params(self):
        self.y_sep = 3
        self.x_sep = 15
        self.check_var = tk.BooleanVar()
        return
    

    def run(self):
        self.widgets_define()
        self.widgets_layout()
        return
    

    def widgets_define(self):
        self.label_title_lito = tk.Label(self.parent, text = 'Janssen', **style_subtitle)

        self.frame_check = tk.Frame(self.parent, bg = BG_COLOR)
        self.check_option = tk.Checkbutton(self.frame_check, variable = self.check_var, command = self.check_func, bg = BG_COLOR)
        self.label_check = tk.Label(self.frame_check, text = 'Opción', **style_label_options)
        
        self.frame_entries = tk.Frame(self.parent, bg = BG_COLOR)

        
        self.label_rh = tk.Label(self.frame_entries, text = 'Radio Hidráulico', **style_label_options)
        self.entry_rh = tk.Entry(self.frame_entries, **style_entry)
        self.label_rh_measure = tk.Label(self.frame_entries, text = 'm', **style_label_options)

        self.label_rho = tk.Label(self.frame_entries, text = 'Densidad (t/m³)', **style_label_options)
        self.entry_rho = tk.Entry(self.frame_entries, **style_entry)
        self.label_rho_measure = tk.Label(self.frame_entries, text = 't/m³', **style_label_options)

        self.label_g = tk.Label(self.frame_entries, text = 'Gravedad (m/s²)', **style_label_options)
        self.entry_g = tk.Entry(self.frame_entries, **style_entry)
        self.label_g_measure = tk.Label(self.frame_entries, text = 'm/s²', **style_label_options)

        self.label_ang = tk.Label(self.frame_entries, text = 'Ángulo de Fricción', **style_label_options)
        self.entry_ang = tk.Entry(self.frame_entries, **style_entry)
        self.label_ang_measure = tk.Label(self.frame_entries, text = '°', **style_label_options)

        self.label_k = tk.Label(self.frame_entries, text = 'Coeficiente k', state = 'disabled', **style_label_options)
        self.entry_k = tk.Entry(self.frame_entries, state = 'disabled', **style_entry)
        self.label_k_measure = tk.Label(self.frame_entries, text = '', **style_label_options)

        self.label_mu = tk.Label(self.frame_entries, text = 'Coeficiente u', state = 'disabled', **style_label_options)
        self.entry_mu = tk.Entry(self.frame_entries, state = 'disabled', **style_entry)
        self.label_mu_measure = tk.Label(self.frame_entries, text = '', **style_label_options)

        self.label_h = tk.Label(self.frame_entries, text = 'Altura', **style_label_options)
        self.entry_h = tk.Entry(self.frame_entries, **style_entry)
        self.label_h_measure = tk.Label(self.frame_entries, text = 'm', **style_label_options)

        
        self.button_lito_calc = AppButton(self.parent, text = 'Calcular', command = self.janssen_calc)

        self.label_lito_result = tk.Label(self.parent, text = '', **style_label_result)
        return
    

    def widgets_layout(self):
        self.label_title_lito.pack(pady = (20, 5))

        self.frame_check.pack()
        self.label_check.grid(row = 0, column = 0)
        self.check_option.grid(row = 0, column = 1)

        self.frame_entries.pack()
        
        
        self.label_rh.grid(row = 0, column = 0, pady = self.y_sep, sticky = 'w')
        self.entry_rh.grid(row = 0, column = 1, pady = self.y_sep, padx = self.x_sep)
        self.label_rh_measure.grid(row = 0, column = 2, pady = self.y_sep, sticky = 'w')

        self.label_rho.grid(row = 1, column = 0, pady = self.y_sep, sticky = 'w')
        self.entry_rho.grid(row = 1, column = 1, pady = self.y_sep, padx = self.x_sep)
        self.label_rho_measure.grid(row = 1, column = 2, pady = self.y_sep, sticky = 'w')

        self.label_g.grid(row = 2, column = 0, pady = self.y_sep, sticky = 'w')
        self.entry_g.grid(row = 2, column = 1, pady = self.y_sep, padx = self.x_sep)
        self.label_g_measure.grid(row = 2, column = 2, pady = self.y_sep, sticky = 'w')

        self.label_ang.grid(row = 3, column = 0, pady = self.y_sep, sticky = 'w')
        self.entry_ang.grid(row = 3, column = 1, pady = self.y_sep, padx = self.x_sep)
        self.label_ang_measure.grid(row = 3, column = 2, pady = self.y_sep, sticky = 'w')

        self.label_k.grid(row = 4, column = 0, pady = self.y_sep, sticky = 'w')
        self.entry_k.grid(row = 4, column = 1, pady = self.y_sep, padx = self.x_sep)
        self.label_k_measure.grid(row = 4, column = 2, pady = self.y_sep, sticky = 'w')

        self.label_mu.grid(row = 5, column = 0, pady = self.y_sep, sticky = 'w')
        self.entry_mu.grid(row = 5, column = 1, pady = self.y_sep, padx = self.x_sep)
        self.label_mu_measure.grid(row = 5, column = 2, pady = self.y_sep, sticky = 'w')

        self.label_h.grid(row = 6, column = 0, pady = self.y_sep, sticky = 'w')
        self.entry_h.grid(row = 6, column = 1, pady = self.y_sep, padx = self.x_sep)
        self.label_h_measure.grid(row = 6, column = 2, pady = self.y_sep, sticky = 'w')

        
        self.button_lito_calc.pack(pady = 10)

        self.label_lito_result.pack(pady = 20)
        return
    

    def check_func(self):
        if self.check_var.get():
            self.label_ang.config(state = 'disabled')
            self.entry_ang.config(state = 'disabled')

            self.label_k.config(state = 'normal')
            self.entry_k.config(state = 'normal')
            self.label_mu.config(state = 'normal')
            self.entry_mu.config(state = 'normal')
        else:
            self.label_ang.config(state = 'normal')
            self.entry_ang.config(state = 'normal')

            self.label_k.config(state = 'disabled')
            self.entry_k.config(state = 'disabled')
            self.label_mu.config(state = 'disabled')
            self.entry_mu.config(state = 'disabled')
        return


    def janssen_calc(self):
        if self.check_var.get():
            try:
                rh = float(self.entry_rh.get())
                rho = float(self.entry_rho.get())
                g = float(self.entry_g.get())
                k = float(self.entry_k.get())
                mu = float(self.entry_mu.get())
                h = float(self.entry_h.get())
            except:
                return

            resultado = (rh*rho*1000*g)/(k*mu)*(1 - exp((-h*k*mu)/rh))
            self.label_lito_result.config(text = f'Presión: {resultado/1000000:.4f} [MPa]')
            return
        
        else:
            try:
                rh = float(self.entry_rh.get())
                rho = float(self.entry_rho.get())
                g = float(self.entry_g.get())
                ang = float(self.entry_ang.get())
                h = float(self.entry_h.get())
            except:
                return
            
            mu = tan(radians(ang))
            k = 1 - sin(radians(ang))
            resultado = (rh*rho*1000*g)/(k*mu)*(1 - exp((-h*mu*k)/rh))
            self.label_lito_result.config(text = f'Presión: {resultado/1000000:.4f} [MPa]')
            return