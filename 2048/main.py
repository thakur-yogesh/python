from tkinter import *
import utils
from grid import Grid
root = Tk()

root.geometry("600x400")
root.resizable(False,False) #to stop resizing the window one for width and one for height

center_frame = Frame(
    root,
    bg = 'black' ,#change to black later
    width = utils.width_prct(60),
    height= utils.height_prct(60)
)
center_frame.place(x=utils.width_prct(18),y=utils.height_prct(15))


# center_frame.pack()

# Bind key press and release events to the frame
# center_frame.bind("<Key>", key_press)
# center_frame.focus()
# center_frame.bind('<KeyPress>',enter)
# center_frame.pack()

Grid.bind_event(center_frame)

for ro in range(4):
    for col in range(4):
        g = Grid(ro,col)
        g.create_btn_object(center_frame)
        g.cell_btn_obj.grid(
            column=ro,row=col
        )
Grid.initialize()

root.mainloop()