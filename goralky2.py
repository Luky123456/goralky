import tkinter as tk
import random
import PIL

root = tk.Tk()

count_goralky = -1
w = 500
h = 500
colors = ["pink", "yellow", "blue", "green"]
count = 40
size = 20
moveable = []
processed = []
counter = 0

canvas = tk.Canvas(width=w, height=h, bg='white')
canvas.pack()


def setup():
    global moveable
    for i in range(40):
        x = random.randrange(0, 480)
        y = random.randrange(0, 400)
        ciarka = canvas.create_line(166, 470, 366, 470)
        moveable.append(canvas.create_oval(x, y, x + size, y + size, fill=colors[i // 10], outline=colors[i // 10],))
        canvas.tag_lower(ciarka)

setup()


def checkit(e):
    global processed, moveable, count_goralky
    goralky_zoznam = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)
    if len(goralky_zoznam) != 0 and goralky_zoznam[0] in moveable and count_goralky < 10:
        if len(processed) == 0:
            processed.append(goralky_zoznam[0])
            moveable.remove(goralky_zoznam[0])
            print("stalo sa")
            print(goralky_zoznam)
            count_goralky += 1
            moveit()


def moveit():
    global processed, counter, goralky_list, count_goralky
    if len(processed) != 0 and count_goralky < 10:
        print(canvas.coords(processed[0]))
        coor = canvas.coords(processed[0])
        finalpos = (h - size)
        print(finalpos)
        print(coor[2])
        dx = w - coor[2]
        dy = finalpos - coor[3]
        if 479 < coor[0] < 481:
            coor1 = canvas.coords(processed[0])
            while coor1[0] > 166 + counter * size:
                coor1 = canvas.coords(processed[0])
                canvas.move(processed[0], -1, 0)
                canvas.update()
            else:
                processed.clear()
                counter += 1
                print("finish", counter)
                return processed

        elif dx > dy:
            dx = dx / dy
            dy = 1
        elif dx < dy:
            dy = dy / dx
            dx = 1
        canvas.move(processed[0], dx, dy)
        canvas.after(5, moveit)


def move_on_line():
    if count_goralky < 10:
        lx = canvas.coords(processed[0])
        print(processed[0])
        print(lx)
        if lx > 70 + 20 * counter:
            canvas.move(processed[0], -1, 0)
        canvas.after(5, move_on_line())


canvas.bind("<Button-1>", checkit)
root.mainloop()
