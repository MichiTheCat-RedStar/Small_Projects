import numpy as np
import matplotlib.pyplot as plt
from random import randint, seed, choice
from time import localtime, strftime

(seed(sd:=input("seed: "))) if input("\nseed? Y/N> ").upper() == "Y" else (seed(sd:=randint(0, 32767)))
clrs = [
    'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Grays', 'Grays_r',
    'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG',
    'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu',
    'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu',
    'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'berlin', 'berlin_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg',
    'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth',
    'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_grey', 'gist_grey_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern',
    'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gist_yerg', 'gist_yerg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'grey', 'grey_r', 'hot', 'hot_r',
    'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'managua', 'managua_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r',
    'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r',
    'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'vanimo', 'vanimo_r',
    'viridis', 'viridis_r', 'winter', 'winter_r'
    ]

width, height = 800, 800
if (answ:=(input("HD level? (-R, -1, 0, 1, 2, 2.5, 3, 4, R)> "))) == "2":
    width, height = 2000, 2000
elif answ=="3":
    width, height = 8000, 8000
elif answ=="2.5":
    width, height = 4000, 4000
elif answ=="0":
    width, height = 200, 200
elif answ=="4":
    width, height = 16000, 16000
elif answ=="-1":
    width, height = 10, 10
elif answ=="-R":
    width, height = (_:=randint(1, 600)), _
elif answ=="R":
    width, height = (_:=randint(1000, 18000)), _
if answ != "": chc1 = answ
else: chc1 = "1"

max_iter = 100
if (answ:=(input("Resolution level? (-R, -1, 0, 1, 2, 3, 4, R)> "))) == "2":
    max_iter = 200
elif answ=="3":
    max_iter = 400
elif answ=="0":
    max_iter = 50
elif answ=="4":
    max_iter = 1600
elif answ=="-1":
    max_iter = 10
elif answ=="-R":
    max_iter = randint(1, 60)
elif answ=="R":
    max_iter = randint(200, 1800)
if answ != "": chc2 = answ
else: chc2 = "1"

xmin, xmax = -2, 1
ymin, ymax = -1.5, 1.5
if (answ:=(input("Size level? (0, 1, 2, 3)> "))) == "2":
    xmin, xmax = -3, 2
    ymin, ymax = -2.5, 2.5
elif answ=="0":
    xmin, xmax = -1, 0.5
    ymin, ymax = -0.75, 0.75
elif answ=="3":
    xmin, xmax = -4, 3
    ymin, ymax = -3, 3
if answ == "": answ = "1"

if input("Save log? Y/N> ").upper() == "Y":
    fl = open("FractalLog.txt", "a")
    fl.write(f"{strftime("%d/%m/%Y, %H:%M:%S", localtime())}\nHD level:\t   {chc1}\nResolution level:  {chc2}\nSize level:\t   {answ}\nSeed:\t\t   {sd}\n\n\n")
    fl.close()

x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)
Z = X + (c:=randint(0, 2)-1+1j) * Y

img = np.zeros(Z.shape, dtype=float)
for i in range(max_iter):
    mask = np.abs(Z) <= (b:=randint(0, 1000))
    Z[mask] = Z[mask] ** (a:=randint(0, 15)) + X[mask] + 1j + Y[mask]
    img += mask

print(f"\nFigure1: {a}/15\nFigere2: {b}/1000\nSeed: {sd}\nJ: {c}\n\nHD level: {chc1}\nResolution level: {chc2}")

plt.figure(figsize=(11, 11))
plt.imshow(img, cmap=(chc3:=choice(clrs)), extent=(xmin, xmax, ymin, ymax))
print("Color map:", chc3)
plt.axis("off")
plt.show()