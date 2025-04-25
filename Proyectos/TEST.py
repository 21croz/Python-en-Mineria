# importing tkinter and ttk
from tkinter import *
from tkinter import ttk

# root
root = Tk()

# This will depict the features of Simple Checkbutton
Label(root, text ='Simple Checkbutton').place(x = 10, y = 10)
chkbtn1 = Checkbutton(root, text ='Checkbutton1',
			takefocus = 0).place(x = 10, y = 40)
chkbtn2 = Checkbutton(root, text ='Checkbutton2',
			takefocus = 0).place(x = 10, y = 60)


# This will depict the features of ttk.Checkbutton
Label(root, text ='ttk.Checkbutton').place(x = 140, y = 10)
chkbtn1 = ttk.Checkbutton(root, text ='Checkbutton1',
				takefocus = 0).place(x = 140, y = 40)
chkbtn2 = ttk.Checkbutton(root, text ='Checkbutton2', 
				takefocus = 0).place(x = 140, y = 60)

root.mainloop()

