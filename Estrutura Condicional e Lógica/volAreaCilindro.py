altura=float(input())
raio=float(input())
pi=3.14
volume=pi*(raio**2)*altura
areaBase=pi*(raio**2)
areaLateral=2*pi*raio*altura
areaTotal=(2*areaBase)+areaLateral
print("%.2f"%volume)
print("%.2f"%areaTotal)
