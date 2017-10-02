from tkinter import *

root = Tk()

image_01 = PhotoImage(file = "image/floor.png")
image_02 = PhotoImage(file = "image/wall.png")
map_name = "map.txt"

canvas = Canvas(root, width = 700, height = 700, bg = "white")
canvas.pack()



def import_walls_to_list(file_name):
    try:
        with open(file_name, "r") as f:
            line_list = f.readlines()
            print(line_list)
            return line_list
    except Exception:
        print("File read error!")


def draw_tiles():
    wall_list = import_walls_to_list(map_name)
    distance = 70
    for i, line in enumerate(wall_list):
        for j, value in enumerate(line):
            if str(value) == "0":
                image_floor = canvas.create_image(35+i*distance, 35+j*distance, image = image_01)
            else:
                image_floor = canvas.create_image(35+i*distance, 35+j*distance, image = image_02)

draw_tiles()
root.mainloop()
