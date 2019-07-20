from A1 import *
import sys 

import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

from math import *

class inputs(Ui_MainWindow):
    def setupUi(self, MainMindow):
        Ui_MainWindow.setupUi(self, MainWindow)

        self.Confirm_button.clicked.connect(self.param)

    def param(self):
        configure = self.Slit_Option.currentText()
        D = float(self.Distance.text())
        wvlen = float(self.Wavelength.text())
        slt_sz = float(self.Slit_Size.text())
        slt_sep = float(self.Slit_Separation.text())
        slt_res = float(self.Slit_Resolution.text())
        scr_sz = float(self.Screen_Size.text())
        scr_res = float(self.Screen_Resolution.text())

        return configure,D,wvlen,slt_sz,slt_sep,slt_res,scr_sz,scr_res




class configurator:
    def __init__(self,configure):
        self.configuration = configure

    def create_slit(self,dimen,slt_sz,slt_res,scr_sz,scr_res):
        slt_grid = int(slt_sz/slt_res)
        scr_grid = int((scr_sz*1000)/scr_res)
        factor1 = scr_res/slt_res
        factor2 = 10000/slt_res
        self.parameters = (slt_grid,scr_grid,factor1,factor2)
        Slit = 0.0
        for i in range(dimen):
            Slit = [Slit]*slt_grid
        self.slit = Slit

        return Slit

        
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = inputs()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec_()


Intro  = 'Hello! This is a program which gives you back a interference pattern on screen according to the slit that you provide.'

I0 = 1.0

Buffer = ui.param() 

Slit_option = Buffer[0]
Distance = Buffer[1]
Wavelength = Buffer[2]
Slit_Size = Buffer[3]
Slit_Separation = Buffer[4]
Slit_Resolution = Buffer[5]
Screen_Size = Buffer[6]
Screen_Resoution = Buffer[7]

S1 = configurator(Slit_option)

Slit = S1.create_slit(2,Slit_Size,Slit_Resolution,Screen_Size,Screen_Resoution)

slt_grid,scr_grid,f,g = S1.parameters

print(Slit_option)



beta = (Wavelength*Distance*10)/Slit_Size

Screen = []


for i in range(len(Slit)):
    print(Slit[i])

def delta(i,j,x,y):
    variable =  cos((2*pi*Slit_Resolution*abs(sqrt((Distance*g)**2 + (a*f-i)**2 + (b*f-j)**2)  - sqrt((Distance*g)**2 + (a*f-x)**2 + (b*f-y)**2)))/Wavelength)
    return variable

def func(a,b):
    I = 0.0
    for i in range(len(Slit)):
        for j in range(len(Slit[0])):
            for x in range(i,len(Slit)):
                for y in range(j,len(Slit[0])):
                    if (x,y) !=  (i,j):
                        if Slit[x][y] != 0.0 and  Slit[i][j] != 0.0:
                            I +=   (slit[x][y] + slit[i][j] + 2*sqrt(slit[x][y]*slit[i][j])*delta(i,j,x,y))
    return(I)


print('scr_grid  = ',scr_grid)
print('Screen_Resoution  = ',Screen_Resoution)
print('Screen_Size  = ',Screen_Size)
print('beta  = ',beta)
print('slt_grid  = ',slt_grid)
print('Slit_Resolution  = ',Slit_Resolution)
print('Slit_Size  = ',Slit_Size)

p = range(-scr_grid,scr_grid+1)
q = range(-scr_grid,scr_grid+1)

for a in p:
    M = []
    for b in q:
        M.append(func(a,b))
    Screen.append(M)
'''
for i in range(len(p)):
    print(Screen[i])
'''
xtics = [i*(Screen_Resoution/1000) for i in p]
ytics = [j*(Screen_Resoution/1000) for j in q]

X,Y = np.meshgrid(xtics,ytics)


plt.xlabel('X axis (in mm)', fontsize = 'large')
plt.ylabel('Y axis (in mm)', fontsize = 'large')

plt.contourf(X,Y,Screen,30, cmap = 'gray')
plt.colorbar()
plt.show()


