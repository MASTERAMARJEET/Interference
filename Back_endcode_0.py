from math import cos, sqrt, pi
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')


print('Hello! This is a program which gives you back a interference pattern on\
screen according to the slit that you provide.')

I0 = 1.0

# SLIT PATTERN DESIGN
print('Here, you can choose the slit configuration..!')
print('You can choose from among the following...')
print('\t1.Single Slit')
print('\t2.Double Slit')
print('\t3.Double Dot')
print('\t4.Multiple Slit')
print('\t5.Multiple Dot')
print('\t6.Costumized Slit')
choice = int(input('Enter the one that you want to see:'))
D = float(input("Enter The distance of the screen from the slit (in cm):"))
wvlen = float(input("Enter the wavelenght of light being used (in microns):"))

slit = []

Screen = []

if choice == 1:  # 1.Single Slit
    print('SORRY ! Functionality unavailable for now. !')

elif choice == 2:  # 2.Double Slit

    slt_size = int(
        input('Enter the distance between the two slits {in microns}:'))
    slt_res = slt_size/4
    slt_grid = int(slt_size/slt_res)

    A = [0.0]*(slt_grid+1)
    for i in range(slt_grid*2):
        slit.append(A)
        slit[i][0] = I0
        slit[i][slt_grid] = I0

    print('\nNow! You have to enter the size of screen {in mm}.')
    print(' Note that if you enter 10, the screen will extend from -10 mm to 10 mm on both axes.')
    print(' You can enter a float also.')

    beta = (wvlen*D*10)/slt_size                        # unit -> in mm

    scr_size = beta*4
    scr_res = (beta*1000)/10
    scr_grid = int((scr_size*1000)/scr_res)

    for i in range(len(slit)):
        print(slit[i])

    f = scr_res/slt_res
    g = 10000/slt_res


elif choice == 3:  # 3.Double Dot
    slt_size = int(
        input('Enter the distance between the point sources {in microns}:'))
    slt_res = slt_size/10
    slt_grid = int(slt_size/slt_res)

    A = [0.0]*(slt_grid+1)
    for i in range(1):
        slit.append(A)
        slit[i][0] = I0
        slit[i][slt_grid] = I0

    print('\nNow! You have to enter the size of screen {in mm}.')
    print(' Note that if you enter 10, the screen will extend from -10 mm to 10 mm on both axes.')
    print(' You can enter a float also.')

    beta = (wvlen*D*10)/slt_size                        # unit -> in mm

    scr_size = beta*3
    scr_res = (beta*1000)/10
    scr_grid = int((scr_size*1000)/scr_res)

    for i in range(len(slit)):
        print(slit[i])

    f = scr_res/slt_res
    g = 10000/slt_res


elif choice == 4:  # 4.Multiple Slit
    print('SORRY ! Functionality unavailable for now. !')

elif choice == 5:  # 5.Multiple Dot
    print('This is the multiple dot option. Here you can choose the number of point sources to have.')
    print('It is recommended to keep it to a max of 5!. ')
    num = int(input('Enter the number of point sources you want:'))
    slt_size = int(
        input('Enter the distance between the point sources {in microns}:'))
    slt_res = slt_size/10
    d = int(slt_size/slt_res)
    slt_grid = d*(num-1)

    A = [0.0]*(slt_grid+1)
    for i in range(1):
        slit.append(A)
        for j in range(num):
            slit[i][d*j] = I0

    print('\nNow! You have to enter the size of screen {in mm}.')
    print(' Note that if you enter 10, the screen will extend from -10 mm to 10 mm on both axes.')
    print(' You can enter a float also.')

    beta = (wvlen*D*10)/slt_size                        # unit -> in mm

    scr_size = beta*3
    scr_res = (beta*1000)/10
    scr_grid = int((scr_size*1000)/scr_res)

    for i in range(len(slit)):
        print(slit[i])

    f = scr_res/slt_res
    g = 10000/slt_res


elif choice == 6:  # 6.Costumized Slit
    slt_size = int(input('Enter the size of slit {in microns}:'))
    slt_res = int(input('Enter the resolution of the slit {in microns}:'))
    slt_grid = int(slt_size/slt_res)

    for i in range(slt_grid):
        A = [0.0]*slt_grid
        slit.append(A)

    print('\nNow! You have to enter the size of screen {in mm}.')
    print(' Note that if you enter 10, the screen will extend from -10 mm to 10 mm on both axes.')
    print(' You can enter a float also.')

    beta = (wvlen*D*10)/slt_size

    scr_size = float(input('Enter the size of the screen:'))
    scr_res = int(input('Enter the resolution of the screen {in microns}:'))
    scr_grid = int((scr_size*1000)/scr_res)

    for i in range(len(slit)):
        print(slit[i])

    f = scr_res/slt_res
    g = 10000/slt_res


def delta(i, j, x, y):
    variable = cos((2*pi*slt_res*abs(sqrt((D*g)**2 + (a*f-i)**2 + (b*f-j)**2)
                                     - sqrt((D*g)**2 + (a*f-x)**2 + (b*f-y)**2)))/wvlen)
    return variable


def func(a, b):
    I = 0.0
    for i in range(len(slit)):
        for j in range(len(A)):
            for x in range(i, len(slit)):
                for y in range(j, len(A)):
                    if (x, y) != (i, j):
                        if slit[x][y] != 0.0 and slit[i][j] != 0.0:
                            I += (slit[x][y] + slit[i][j] + 2 *
                                  sqrt(slit[x][y]*slit[i][j])*delta(i, j, x, y))
    return(I)


print('scr_grid =', scr_grid)
print('scr_res =', scr_res)
print('scr_size =', scr_size)
print('beta =', beta)
print('slt_grid =', slt_grid)
print('slt_res =', slt_res)
print('slt_size =', slt_size)

p = range(-scr_grid, scr_grid+1)
q = range(-scr_grid, scr_grid+1)

for a in p:
    M = []
    for b in q:
        M.append(func(a, b))
    Screen.append(M)

xtics = [i*(scr_res/1000) for i in p]
ytics = [j*(scr_res/1000) for j in q]

X, Y = np.meshgrid(xtics, ytics)


plt.xlabel('X axis (in mm)', fontsize='large')
plt.ylabel('Y axis (in mm)', fontsize='large')

plt.contourf(X, Y, Screen, 30, cmap='gray')
plt.colorbar()
plt.show()
