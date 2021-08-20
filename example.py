from egg.resources.structures import *
from egg.resources.console import ProgressBar, clearConsole

# bar = ProgressBar()
# bar.iterate(printPercent = True)

M = [[255,0,0,255,255,255,0,255], [0,0,0,255,255,255,0,255], [0,255,0,255,0,255,0,255], [0,255,255,255,255,255,0,255], [0,255,255,255,255,255,0,255], [0,0,255,255,255,0,0,255], [0,0,255,255,0,0,0,255], [0,0,255,255,0,0,0,255]]

matriz = Image()
matriz.loadFromBW(M)
matriz.printRGB()

jj = [[[242, 80, 34], [127, 186, 0]], [[0, 164, 239], [255, 185, 0]]]
m = Image()
m.loadFromRGB(jj)
m.printRGB()
m.bias = [255, 0, 0]
m.printRGB()

x = Image()
x.load("example.jpg")
x.printRGB()
x.printBW()

# m.save("micro.jpg") # Not working yet