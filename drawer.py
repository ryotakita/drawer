import cv2
import numpy as np
import csv
import math
import svgwrite
import random
# -*- coding: utf8 -*-
import os, tkinter, tkinter.filedialog, tkinter.messagebox

# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.attributes("-topmost", True)
root.title("SvgViewer")
root.geometry("300x80")


file = tkinter.StringVar()
file.set("test.csv")
def enterFile():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    fileName = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file.set(fileName)

button = tkinter.Button(root, text='パス指定',command = enterFile)
button.pack()

def createSVG():
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

    tkinter.messagebox.showinfo("処理結果","処理が終了しました。")

button2 = tkinter.Button(root, text='実行',command = createSVG)
button2.pack()

Static1 = tkinter.Label(textvariable=file)
Static1.pack()
# 処理ファイル名の出力

#tkinter.messagebox.showinfo('○×プログラム',file)

root.mainloop()





