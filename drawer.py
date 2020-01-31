import numpy as np
import csv
import svgwrite
import random
# -*- coding: utf8 -*-
import os, tkinter, tkinter.filedialog, tkinter.messagebox

root = tkinter.Tk()
root.attributes("-topmost", True)
root.title("SvgViewer")
iconfile = "C:/Users/ryota-kita/Documents/SourceCode/drawer/favicon.ico"
root.iconbitmap(default=iconfile)
root.geometry("300x100")

file = tkinter.StringVar()
file.set("test.csv")
def enterFile():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    fileName = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file.set(fileName)

button = tkinter.Button(root, text='path',command = enterFile)
button.grid()

status = tkinter.StringVar()
status.set("waiting")
Static2 = tkinter.Label(textvariable=status)
Static2.grid()

def createSVG():
    status.set("Error Ocurred")
    img = np.full((3000, 3000, 3), 128, dtype=np.uint8)

    path_csv = file.get()
    f = open(path_csv, 'rt')
    datareader = csv.reader(f)

    path_svg = path_csv.strip("csv") + "svg"
    path_png = path_csv.strip("csv") + "png"
    dwg = svgwrite.Drawing( path_svg,(3000,3000))
    

    for row in datareader:
        if(len(row) == 4):
            dwg.add( dwg.line((int(round(float(row[0])))+500,int(round(float(row[1])))+500),( int(round(float(row[2])))+500,  int(round(float(row[3])))+500),  stroke=svgwrite.rgb(10, 10, 16, '%')))
        elif(len(row) == 2):
            x = int(round(float(row[0]))+500)
            y = int(round(float(row[1]))+500)
            dwg.add( dwg.circle((x,y), 1) )
        else:
            points = []
            for num in range(len(row)):
                if(num % 2 == 0) :
                    x = int(round(float(row[num]))+500)
                    y = int(round(float(row[num+1]))+500)
                    points.append([x,y])
            r = random.randint(0,150)
            g = random.randint(0,150)
            b = random.randint(0,150)
            print(points)
            if(len(points) != 0):
                dwg.add( dwg.polygon(points=points, fill=svgwrite.rgb(r,g,b,'%'), stroke="black") )

    #dwg.add( dwg.polygon( points = points))
    dwg.save()

    status.set("Completed")
    os.system(path_svg)


button2 = tkinter.Button(root, text='Do',command = createSVG)
button2.grid()

def FixWindow():
        root.overrideredirect(1)
        root.geometry("1000x25")
        Static2.grid(column=0,row=0)
        button.grid(column=1,row=0)
        buttonFix.grid(column=2,row=1)
        buttonDeFix.grid(column=2,row=0)
        button2.grid(column=3,row=0)
        Static1.grid(column=4,row=0)
        root.configure(bg="white")
        root.wm_attributes("-transparentcolor","white")
def DeFixWindow():
        root.overrideredirect(0)


buttonFix = tkinter.Button(root, text='fixWindow',command = FixWindow)
buttonFix.grid()
buttonDeFix = tkinter.Button(root, text='UndofixWindow',command = DeFixWindow)
buttonDeFix.grid()

Static1 = tkinter.Label(textvariable=file,fg="red")
Static1.grid()

root.mainloop()





