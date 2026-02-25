from random import randint, gauss, seed; (mat := True) if (input('matplotlib? Y/N> ') == 'Y') else (mat := False); ren = int(input('range (100): ')); tab = int(input('table (10): '))
if mat: import matplotlib.pyplot as plt    # pip install Matplotlib 
while True:
    (gauss(float(input('mu (0): ')), float(input('sigma (1): ')))) if (input('gauss? (0, 1) Y/N> ') == 'Y') else gauss(0, 1); (seed(float(input('seed: ')))) if (input('seed? (None) Y/N> ') == 'Y') else seed(None, None); table = []; exec('table.append(0); '*tab)
    for _ in range(ren): table[randint(0, len(table)-1)] += int(gauss()+1)
    print(f'\nall\t->\t{table} - seed: {seed()}\n')
    for i in table: print(end = f'{i}\t->\t'), print('#'*i)
    print('\n')
    if mat: plt.plot(table); plt.show()