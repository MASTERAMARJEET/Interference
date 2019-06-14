from math import *

print("Hello! This is a program which gives you back a interference pattern on screen according to the slit that you provide.")
I0=1.0

#SLIT PATTERN DESIGN	
print('Here, you can choose the slit configuration..!')
print('You can choose from among the following... \n 1.Single Slit\n 2.Double Slit\n 3.Two Point Source\n 4.Multiple Slit\n 5.Costumized Slit')
choice=int(input('Enter the one that you want to see:'))
D=float(input("Enter The distance of the screen from the slit (in cm):"))
wvlen=float(input("Enter the wavelenght of light being used (in microns):"))

if choice==1:
	
elif choice==2:
	
elif choice==3:
	slt_size=int(input('Enter the distance between the slits {in microns}:'))
	scr_res=500
	slt_res=50
elif choice==4:
	
elif choice==5:
	slt_size=int(input('Enter the size of slit {in microns}:'))
	scr_res=int(input('Enter the resolution of the screen {in microns}:'))
	slt_res=int(input('Enter the resolution of the slit {in microns}:'))
	slt_grd=int(slt_size/slt_res)

f=scr_res/slt_res
g=10000/scr_res

slit=[]

for i in range(slt_grd):
	A=[0.0]*slt_grd
	slit.append(A)

for i in range(len(slit)):
	print(slit[i])



def diff(i,j,x,y):
	variable= cos((2*pi*slt_res*abs(sqrt((D*g)**2 + (a*f-i)**2 + (b*f-j)**2) - sqrt((D*g)**2 + (a*f-x)**2 + (b*f-y)**2)))/wvlen)
	return variable

def func(a,b):
	I=0.0
	for i in range(len(slit)):
		for j in range(len(A)):
			for x in range(i,len(slit)):
				for y in range(j,len(A)):
					if (x,y) != (i,j):
						if slit[x][y]!=0.0 and  slit[i][j]!=0.0:
							I += slit[x][y] + slit[i][j] + 2*sqrt(slit[x][y]*slit[i][j])*diff(i,j,x,y)	
	return(I)

Screen=[]

print('\nNow! You have to enter the size of screen {in mm}.\n Note that if you enter 10, the screen will extend from -10 mm to 10 mm on both axes.\n You can enter a float also.')

scr_size=float(input('Enter the size of the screen:'))
scr_grid=int((scr_size*1000)/scr_res)

p=range(-scr_grid,scr_grid+1)
q=range(-scr_grid,scr_grid+1)

for a in p:
	M=[]
	for b in q:
		M.append(func(a,b))
	Screen.append(M)

for i in range(len(p)):
	print(Screen[i])