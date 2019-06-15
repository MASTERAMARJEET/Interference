from math import *

print("Hello! This is a program which gives you back a interference pattern on screen according to the slit that you provide.")
I0=1.0

#SLIT PATTERN DESIGN	
print('Here, you can choose the slit configuration..!')
print('You can choose from among the following... \n 1.Single Slit\n 2.Double Slit\n 3.Two Point Source\n 4.Multiple Slit\n 5.Costumized Slit')
choice=int(input('Enter the one that you want to see:'))
D=float(input("Enter The distance of the screen from the slit (in cm):"))
wvlen=float(input("Enter the wavelenght of light being used (in microns):"))

slit=[]

Screen=[]



if choice==1:
	print('SORRY ! Functionality unavailable for now. !')
	
elif choice==2:
	print('SORRY ! Functionality unavailable for now. !')
		
elif choice==3:
	slt_size=int(input('Enter the distance between the slits {in microns}:'))
	slt_res=slt_size/10
	slt_grid=int(slt_size/slt_res)

	A=[0.0]*(slt_grid+1)
	for i in range(1):
		slit.append(A)
		slit[i][0]=I0
		slit[i][slt_grid]=I0

	print('\nNow! You have to enter the size of screen {in mm}.\n Note that if you enter 10, the screen will extend from -10 mm to 10 mm on both axes.\n You can enter a float also.')

	beta=(wvlen*D*10)/slt_size						# unit -> in mm

	scr_size=beta*10
	scr_res=(beta*1000)/10
	scr_grid=int((scr_size*1000)/scr_res)


	for i in range(len(slit)):
		print(slit[i])

	f=scr_res/slt_res
	g=10000/scr_res


elif choice==4:
	print('SORRY ! Functionality unavailable for now. !')
	
elif choice==5:
	slt_size=int(input('Enter the size of slit {in microns}:'))
	slt_res=int(input('Enter the resolution of the slit {in microns}:'))
	slt_grid=int(slt_size/slt_res)

	for i in range(slt_grid):
		A=[0.0]*slt_grid
		slit.append(A)

	print('\nNow! You have to enter the size of screen {in mm}.\n Note that if you enter 10, the screen will extend from -10 mm to 10 mm on both axes.\n You can enter a float also.')

	scr_size=float(input('Enter the size of the screen:'))
	scr_res=int(input('Enter the resolution of the screen {in microns}:'))
	scr_grid=int((scr_size*1000)/scr_res)

	for i in range(len(slit)):
		print(slit[i])

	f=scr_res/slt_res
	g=10000/scr_res



def phase(i,j,x,y):
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
							I += slit[x][y] + slit[i][j] + 2*sqrt(slit[x][y]*slit[i][j])*phase(i,j,x,y)	
	return(I)


print('scr_grid =',scr_grid)
print('scr_res =',scr_res)
print('scr_size =',scr_size)
print('beta =',beta)
print('slt_grid =',slt_grid)
print('slt_res =',slt_res)
print('slt_size =',slt_size)

p=range(-scr_grid,scr_grid+1)
q=range(-scr_grid,scr_grid+1)

for a in p:
	M=[]
	for b in q:
		M.append(func(a,b))
	Screen.append(M)

for i in range(len(p)):
	print(Screen[i])

