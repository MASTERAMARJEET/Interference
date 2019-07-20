import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

from math import *


class configurator:
	def __init__(self,configure):
		self.configuration = configure

	def create_slit(self,dimen,slt_sz,slt_res,scr_sz,scr_res):
		slt_grid = int(slt_sz/slt_res)
		scr_grid = int((scr_sz*1000)/scr_res)
		factor1 = scr_res/slt_res
		factor2 = 10000/slt_res
		self.parameters = (slt_sz,slt_res,slt_grid,scr_sz,scr_res,scr_grid,factor1,factor2)
		Slit = 0.0
		for i in range(dimen):
			Slit = [Slit]*slt_grid
		self.slit = Slit

		return Slit

		



Intro  = 'Hello! This is a program which gives you back a interference pattern on screen according to the slit that you provide.'

I0 = 1.0

#SLIT PATTERN DESIGN	


Slit_option = int(input('Enter the one that you want to see:')) 
Distance = float(input("Enter The distance of the screen from the slit (in cm):"))
Wavelenght = float(input("Enter the wavelenght of light being used (in microns):"))

Slit = []

Screen = []

if Slit_option  ==  1:#1.Single Slit
	print('SORRY ! Functionality unavailable for now. !')
	
elif Slit_option  ==  2:#2.Double Slit

	Slit_Size = int(input('Enter the distance between the two slits {in microns}:'))
	Slit_Resolution = Slit_Size/4
	slt_grid = int(Slit_Size/Slit_Resolution)

	A = [0.0]*(slt_grid+1)
	for i in range(slt_grid*2):
		Slit.append(A)
		Slit[i][0] = I0
		Slit[i][slt_grid] = I0
		
	print('\nNow! You have to enter the size of screen {in mm}.')
	print(' Note that if you enter 10, the screen will extend from -10 mm to 10 mm on both axes.')
	print(' You can enter a float also.')

	beta = (Wavelenght*Distance*10)/Slit_Size						# unit -> in mm

	Screen_Size = beta*4
	Screen_Resoution = (beta*1000)/10
	scr_grid = int((Screen_Size*1000)/Screen_Resoution)


	for i in range(len(Slit)):
		print(Slit[i])

	f = Screen_Resoution/Slit_Resolution
	g = 10000/Slit_Resolution

		
elif Slit_option == 3:#3.Double Dot
	Slit_Size = int(input('Enter the distance between the point sources {in microns}:'))
	Slit_Resolution = Slit_Size/10
	slt_grid = int(Slit_Size/Slit_Resolution)

	A = [0.0]*(slt_grid+1)
	for i in range(1):
		Slit.append(A)
		Slit[i][0] = I0
		Slit[i][slt_grid] = I0

	print('\nNow! You have to enter the size of screen {in mm}.')
	print(' Note that if you enter 10, the screen will extend from -10 mm to 10 mm on both axes.')
	print(' You can enter a float also.')

	beta = (Wavelenght*Distance*10)/Slit_Size						# unit -> in mm

	Screen_Size = beta*3
	Screen_Resoution = (beta*1000)/10
	scr_grid = int((Screen_Size*1000)/Screen_Resoution)


	for i in range(len(Slit)):
		print(Slit[i])

	f = Screen_Resoution/Slit_Resolution
	g = 10000/Slit_Resolution


elif Slit_option == 4:#4.Multiple Slit
	print('SORRY ! Functionality unavailable for now. !')

elif Slit_option == 5:#5.Multiple Dot
	print('This is the multiple dot option. Here you can choose the number of point sources to have.')
	print('It is recommended to keep it to a max of 5!. ')
	num = int(input('Enter the number of point sources you want:'))
	Slit_Size = int(input('Enter the distance between the point sources {in microns}:'))
	Slit_Resolution = Slit_Size/10
	d = int(Slit_Size/Slit_Resolution)
	slt_grid = d*(num-1)

	A = [0.0]*(slt_grid+1)
	for i in range(1):
		Slit.append(A)
		for j in range(num):
			Slit[i][d*j] = I0

	print('\nNow! You have to enter the size of screen {in mm}.')
	print(' Note that if you enter 10, the screen will extend from -10 mm to 10 mm on both axes.')
	print(' You can enter a float also.')

	beta = (Wavelenght*Distance*10)/Slit_Size						# unit -> in mm

	Screen_Size = beta*3
	Screen_Resoution = (beta*1000)/10
	scr_grid = int((Screen_Size*1000)/Screen_Resoution)


	for i in range(len(Slit)):
		print(Slit[i])

	f = Screen_Resoution/Slit_Resolution
	g = 10000/Slit_Resolution

	
elif Slit_option == 6:#6.Costumized Slit
	Slit_Size = int(input('Enter the size of slit {in microns}:'))
	Slit_Resolution = int(input('Enter the resolution of the slit {in microns}:'))
	slt_grid = int(Slit_Size/Slit_Resolution)

	for i in range(slt_grid):
		A = [0.0]*slt_grid
		Slit.append(A)

	print('\nNow! You have to enter the size of screen {in mm}.')
	print(' Note that if you enter 10, the screen will extend from -10 mm to 10 mm on both axes.')
	print(' You can enter a float also.')

	beta = (Wavelenght*Distance*10)/Slit_Size

	Screen_Size = float(input('Enter the size of the screen:'))
	Screen_Resoution = int(input('Enter the resolution of the screen {in microns}:'))
	scr_grid = int((Screen_Size*1000)/Screen_Resoution)

	for i in range(len(Slit)):
		print(Slit[i])

	f = Screen_Resoution/Slit_Resolution
	g = 10000/Slit_Resolution



def delta(i,j,x,y):
	variable =  cos((2*pi*Slit_Resolution*abs(sqrt((Distance*g)**2 + (a*f-i)**2 + (b*f-j)**2) - sqrt((Distance*g)**2 + (a*f-x)**2 + (b*f-y)**2)))/Wavelenght)
	return variable

def func(a,b):
	I = 0.0
	for i in range(len(Slit)):
		for j in range(len(A)):
			for x in range(i,len(Slit)):
				for y in range(j,len(A)):
					if (x,y) !=  (i,j):
						if Slit[x][y] != 0.0 and  Slit[i][j] != 0.0:
							I +=   (Slit[x][y] + Slit[i][j] + 2*sqrt(Slit[x][y]*Slit[i][j])*delta(i,j,x,y))
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

