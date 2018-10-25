import os
from tkinter import *
from PIL import ImageTk

root = Tk()

# процедура обновления четырех изображений при нажатии кнопок
def refresh(): 
    global canvas, x, xnum, y, ynum, img1, img2, img3, img4
    
    # промежуточная папка (1)
    first = os.listdir("%s\%s" % (base, level[levelnum])) 
    
    # список папок, представляющих ординату
    x = os.listdir("%s\%s\%s" % (base, level[levelnum],first[0])) 
    if xnum >= len(x)-1:
        xnum = len(x)-2;
    
    # промежуточная папка (2)
    second = os.listdir("%s\%s\%s\%s" % (base, level[levelnum],first[0],x[0]))
    
    # список изображений в папках ординат, представляющих абсциссу
    y = os.listdir("%s\%s\%s\%s\%s" % (base, level[levelnum],first[0],x[xnum],second[0]))
    if ynum >= len(y)-1:
        ynum = len(y)-2;
        
    img1 = ImageTk.PhotoImage(file= path % (base, level[levelnum],first[0],x[xnum],second[0],y[ynum]))
    img2 = ImageTk.PhotoImage(file= path % (base, level[levelnum],first[0],x[xnum],second[0],y[ynum+1]))
    img3 = ImageTk.PhotoImage(file= path % (base, level[levelnum],first[0],x[xnum+1],second[0],y[ynum]))
    img4 = ImageTk.PhotoImage(file= path % (base, level[levelnum],first[0],x[xnum+1],second[0],y[ynum+1]))

    canvas.create_image(0, 0, image=img1, anchor=NW)
    canvas.create_image(0, 256, image=img2, anchor=NW)
    canvas.create_image(256, 0, image=img3, anchor=NW)
    canvas.create_image(256, 256, image=img4, anchor=NW)

# кнопки для масштабирования 
def zoomin(event):
    global levelnum
    if len(level) > (levelnum + 1):
        levelnum += 1;
    refresh()
        
def zoomout(event):
    global levelnum, xnum, ynum
    if levelnum > 0:
        levelnum -= 1;
    refresh()
    
# кнопки для навигации
def down(event):
    global ynum
    if len(y) > (ynum + 2):
        ynum += 1
    refresh()
    
def up(event):
    global ynum
    if  ynum > 0:
        ynum -= 1;
    refresh()
    
def left(event):
    global xnum
    if  xnum > 0:
        xnum -= 1;
    refresh()

def right(event):
    global xnum
    if len(x) > (xnum + 2):
        xnum += 1
    refresh()
    
root.geometry("512x612")


btnup = Button(root, text="up")
btnup.place(x = 100, y = 10, width = 35) 
btndown = Button(root, text="down")
btndown.place(x = 100, y = 45, width = 35)     
btnup.bind("<Button-1>",up)
btndown.bind("<Button-1>",down)   
             
btnleft = Button(root, text="left")
btnleft.place(x = 60, y = 45, width = 35) 
btnright = Button(root, text="right")
btnright.place(x = 140, y = 45, width = 35) 
btnleft.bind("<Button-1>",left)
btnright.bind("<Button-1>",right) 

btnzin = Button(root, text="+")
btnzin.place(x = 190, y = 10, width = 20)  
btnzout = Button(root, text="-")
btnzout.place(x = 190, y = 45, width =20)
btnzin.bind("<Button-1>",zoomin)
btnzout.bind("<Button-1>",zoomout)

levelnum = 0
xnum = 0    
ynum = 0
base = "osmmapMapnik"
path = "%s\%s\%s\%s\%s\%s"

#список папок, представляющих уровни                  
level = os.listdir(base)

canvas = Canvas(width=600, height=600, bg='black')

canvas.place(x=0,y=100,width=512)

refresh()

root.mainloop()
