import gpt
import math
from tkinter import *
WINDOW=Tk()
WINDOW.geometry("1050x650+200+20")
WINDOW.title("Nomenclature")
columns=21
rows=11

def start():
    answer.set(gpt.func(main_array))
def clear():
    for x in range(0, rows):
        for y in range(0, columns):
            main_array[x][y]=0
    maincanvas.delete('all')
    board = maincanvas.create_image(25, 25, image=IMAGE, anchor=NW)
    maincanvas.tag_bind(board, '<Button>', selected)
    answer.set('')


mainframe=Frame(WINDOW, height=650,width=1050,bg='white')
label=Label(mainframe,height=1,width=50,font=('Times',24),text="Enter the bold line formula of the organic compound")
label.place(x=0,y=0)
button=Button(mainframe,height=1,width=10,text="Enter",font=('Times',22),command=start)
clear=Button(mainframe,height=1,width=10,text="Clear",font=('Times',22),command=clear)

answer=StringVar()
label1=Label(mainframe,height=1,width=50,textvariable=answer,font=('Times',26))
label1.place(x=360,y=600)
clear.place(x=180,y=600)
button.place(x=0,y=600)



main_array=list()


for x in range(0, rows):
    main_array.append([])
    for y in range(0, columns):
        main_array[x].append(0)

maincanvas=Canvas(mainframe,width=1050,height=550,bg='white')
def selected(event):
    for x in range(0,rows):
        for y in range(0,columns):
            boolean=main_array[x][y]
    maincanvas.delete('all')
    board = maincanvas.create_image(25, 25, image=IMAGE, anchor=NW)
    maincanvas.tag_bind(board, '<Button>', selected)
    for x_ in range(0, rows):
        for y_ in range(0, columns):

            if math.sqrt(math.pow((event.x-(25+50*y_)),2)+math.pow((event.y-(25+50*x_)),2))<10:
                main_array[x_][y_]=0 if main_array[x_][y_] else 1
            if main_array[x_][y_]:
                a=maincanvas.create_rectangle(25+50*y_-2,25+50*x_-2,25+50*y_+2,25+50*x_+2,fill='black')
                maincanvas.tag_bind(a,'<Button>',selected)
    for ix in range(0,rows):
        for iy in range(0,columns):
            for ind in [(0,1),(1,0),(0,-1),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]:
                if ix+ind[0]>=0 and ix + ind[0]<rows and iy+ind[1]>=0 and iy + ind[1]<columns:
                    if main_array[ix+ind[0]][iy+ind[1]] and main_array[ix][iy]:
                        b=maincanvas.create_line(25+iy*50,25+ix*50,25+(iy+ind[1])*50,25+(ix+ind[0])*50,width=5)
                        maincanvas.tag_bind(b,'<Button>',selected)
IMAGE=PhotoImage(file='FINAL.png')
board=maincanvas.create_image(25,25,image=IMAGE,anchor=NW)
maincanvas.tag_bind(board,'<Button>',selected)
mainframe.place(x=0,y=0)
maincanvas.place(x=0,y=50)
WINDOW.mainloop()