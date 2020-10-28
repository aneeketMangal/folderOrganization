import tkinter
from PIL import Image, ImageTk

from tkinter import messagebox
from tkinter.ttk import *
window = tkinter.Tk()
window.geometry('700x500')
top_frame = tkinter.Frame(window).pack(side = "top")
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

          
image = ImageTk.PhotoImage(file="v.png")
label = tkinter.Label(top_frame, image = image) 

# canvas.create_image(100,100, anchor = tkinter.NW, image=image) 
label.pack()
l1 = tkinter.Label(bottom_frame, text="edureka!",  font=("Arial Bold", 50)).pack()
# l1.grid(column=0, row=0)

# combo = Combobox(window)
# combo['values']= (1, 2, 3, 4, 5, "Text")
# combo.current(3)
# combo.grid(column=0, row=3)


def clickedMainButton():
    messagebox.showinfo('Success', 'Work done succesfully')
 
# def clicked():
#     l1.configure(text="Button was clicked !!")


bt = tkinter.Button(bottom_frame, text="Enter", command=clickedMainButton).pack()
# bt.grid(column=0, row=1)

window.mainloop()