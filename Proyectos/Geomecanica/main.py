import tkinter as tk

from settings import *
from button import AppButton
from litostatica import Litostatica
from janssen import Janssen



class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.set_window_params()

        self.widgets_define()
        self.widgets_layout()

        self.define_subwindows()
    

    def set_window_params(self):
        self.title("Geomecánica")
        self.geometry("500x550")
        self.resizable(False, False)

        self.BG_COLOR = to_hex(COLOR['GRAY4'])
        self.config(bg = self.BG_COLOR)
        return
    

    def widgets_define(self):
        self.label_title = tk.Label(self, text= "Geomecánica", **style_title)

        self.frame_options = tk.Frame(self, bg = self.BG_COLOR)
        self.button_lito = AppButton(self.frame_options, text = 'Litostática', command = self.litostatica)
        self.button_janssen = AppButton(self.frame_options, text = 'Janssen', command = self.janssen)
        self.button_janssen_ext = AppButton(self.frame_options, text = 'Janssen Ext.', command = self.janssen_ext)
        self.button_rotacion = AppButton(self.frame_options, text = 'Rotación', command = self.rotacion)
        self.button_kirsch = AppButton(self.frame_options, text = 'Kirsch', command = self.kirsch)
        self.button_taludes = AppButton(self.frame_options, text = 'Taludes', command = self.taludes)

        self.frame_general = tk.Frame(self, bg = self.BG_COLOR)
        return


    def widgets_layout(self):
        self.label_title.pack(pady = 10)

        self.frame_options.pack()
        x_sep = 5
        y_sep = 5
        self.button_lito.grid(row = 0, column = 0, padx = x_sep, pady = y_sep)
        self.button_janssen.grid(row = 0, column = 1, padx = x_sep, pady = y_sep)
        self.button_janssen_ext.grid(row = 0, column = 2, padx = x_sep, pady = y_sep)
        self.button_rotacion.grid(row = 1, column = 0, padx = x_sep, pady = y_sep)
        self.button_kirsch.grid(row = 1, column = 1, padx = x_sep, pady = y_sep)
        self.button_taludes.grid(row = 1, column = 2, padx = x_sep, pady = y_sep)

        self.frame_general.pack()
        return
    

    def define_subwindows(self):
        self.lito = Litostatica(self.frame_general)
        self.janssen = Janssen(self.frame_general)
        return


    def delete_widgets(self):
        for widget in self.frame_general.winfo_children():
            widget.destroy()
        return


    def litostatica(self):
        self.delete_widgets()

        self.lito.run()
    

    def janssen(self):
        self.delete_widgets()

        self.janssen.run()
        return
    

    def janssen_ext(self):
        self.delete_widgets()

        self.label_title_jans_ext = tk.Label(self.frame_general, text = 'Janssen Extendido', **style_subtitle).pack(pady = (20, 5))
        return
    

    def rotacion(self):
        self.delete_widgets()

        self.label_title_rot = tk.Label(self.frame_general, text = 'Rotación de Esfuerzos', **style_subtitle).pack(pady = (20, 5))
        return
    

    def kirsch(self):
        self.delete_widgets()

        self.label_title_kirsch = tk.Label(self.frame_general, text = 'Kirsch', **style_subtitle).pack(pady = (20, 5))
        return
    

    def taludes(self):
        self.delete_widgets()

        self.label_title_talud = tk.Label(self.frame_general, text = 'Taludes', **style_subtitle).pack(pady = (20, 5))
        return



if __name__ == "__main__":
    app = Main()
    app.mainloop()