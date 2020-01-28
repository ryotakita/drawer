import cv2
import numpy as np
import csv
import math
import svgwrite
import random

img = np.full((3000, 3000, 3), 128, dtype=np.uint8)

path_csv = input("ファイル名を入力してください。")

f = open(path_csv, 'rt')
dataReader = csv.reader(f)

path_svg = path_csv.strip("csv") + "svg"
path_png = path_csv.strip("csv") + "png"
dwg = svgwrite.Drawing( path_svg,(3000,3000))

for row in dataReader:
    if(len(row) == 4):
        cv2.line(img, (int(round(float(row[0])))+500, int(round(float(row[1])))+500), (int(round(float(row[2])))+500, int(round(float(row[3])))+500), (0, 0, 0), thickness=1, lineType=cv2.LINE_4)
        dwg.add( dwg.line((int(round(float(row[0])))+500,int(round(float(row[1])))+500),(int(round(float(row[2])))+500,int(round(float(row[3])))+500),  stroke=svgwrite.rgb(10, 10, 16, '%')))
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

cv2.imwrite(path_png, img)
#dwg.add( dwg.polygon( points = points))
dwg.save()

dummy = input("処理が終了しました。出力ファイルは" + path_svg + "と" + path_png + "です。")

