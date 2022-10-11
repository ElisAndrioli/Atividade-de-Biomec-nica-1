# Atividade 1 de Biomecânica
print("Localize a câmera 1 nos eixos x, y, z")
xc1 = float(input('eixo x = ')) # xc1 = localização da câmera 1 no eixo x
yc1 = float(input('eixo y = ')) # yc1 = localização da câmera 1 no eixo y
zc1 = float(input('eixo z = ')) # zc1 = localização da câmera 1 no eixo z
print('\n\n')

print("Localize a câmera 2 nos eixos x, y, z")
xc2 = float(input('eixo x = ')) # xc2 = localização da câmera 2 no eixo x
yc2 = float(input('eixo y = ')) # yc2 = localização da câmera 2 no eixo y
zc2 = float(input('eixo z = ')) # zc2 = localização da câmera 2 no eixo z
print('\n\n')

print("Localize a projeção da câmera 1 nos eixos x, y, z")
xp1 = float(input('eixo x = ')) # xp1 = projeção da câmera 1 no eixo x
yp1 = float(input('eixo y = ')) # yp1 = projeção da câmera 1 no eixo y
zp1 = float(input('eixo z = ')) # zp1 = projeção da câmera 1 no eixo z
print('\n\n')

print("Localize a projeção da câmera 2 nos eixos x, y, z")
xp2 = float(input('eixo x = ')) # xp2 = projeção da câmera 2 no eixo x
yp2 = float(input('eixo y = ')) # yp2 = projeção da câmera 2 no eixo y
zp2 = float(input('eixo z = ')) # zp2 = projeção da câmera 2 no eixo z
print('\n\n')


vetc1 = [(xc1),(yc1),(zc1)]
vetc2 = [(xc2),(yc2),(zc2)]
vetp1 = [(xp1),(yp1),(zp1)]
vetp2 = [(xp2),(yp2),(zp2)]

# Coeficiente angular da reta 1
mr1xy = (vetp1[1] - vetc1[1]) / (vetp1[0] - vetc1[0])
mr1xz = (vetp1[2] - vetc1[2]) / (vetp1[0] - vetc1[0])
mr1zy = (vetp1[1] - vetc1[1]) / (vetp1[2] - vetc1[2])

# Coeficiente angular da reta 2
mr2xy = (vetp2[1] - vetc2[1]) / (vetp2[0] - vetc2[0])
mr2xz = (vetp2[2] - vetc2[2]) / (vetp2[0] - vetc2[0])
mr2zy = (vetp2[1] - vetc2[1]) / (vetp2[2] - vetc2[2]) 

# No cruzamento 
x1 = (yc2 + (mr1xy * xc1) - (mr2xy * xc2) - yc1) / (mr1xy - mr2xy)
x2 = (zc2 + (mr1xz * xc1) - (mr2xz * xc2) - zc1) / (mr1xz - mr2xz)
y1 = ((mr1xy * x1) - (mr1xy * xc1) + yc1)
z2 = (yc2 + (mr1zy * zc1) - (mr2zy * zc2) - yc1) / (mr1zy - mr2zy)
y2 = ((mr1zy * z2) - (mr1zy * zc1) + yc1)
z1 = ((mr1xz * x2) - (mr1xz * xc1) + zc1)



x = (x1 + x2)/2
y= (y1 + y2)/2
z= (z1 + z2)/2


# Gráfico
# Importando as bibliotecas necessárias
from turtle import onclick 
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d 

# Criando a figura e a projeção 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('eixo X')
ax.set_ylabel('eixo Y')
ax.set_zlabel('eixo Z')

X = [xc1,x,xp1]
Y = [yc1,y,yp1]
Z = [zc1,z,zp1]

X2 = [xc2,x,xp2]
Y2 = [yc2,y,yp2]
Z2 = [zc2,z,zp2]

plt.plot(X,Y,Z, color= 'blue')
plt.plot(X2,Y2,Z2, color = 'red')

# Exibindo o gráfico 
plt.show()

