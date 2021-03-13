import random as rand
from numpy import linalg as lg

x1_min = 10     #-1
x1_max = 50     #1
x2_min = 20     #-1
x2_max = 60     #1

y_max = (30-130)*10
y_min = (20-130)*10
print("y_max: "+str(y_max),"\ny_min: "+str(y_min), '\n '  )
a1 = [rand.randint(y_min, y_max) for i in range(5)]
a2 = [rand.randint(y_min, y_max) for i in range(5)]
a3 = [rand.randint(y_min, y_max) for i in range(5)]
print("Y1: "+str(a1), "\nY2: "+str(a2),"\nY3: "+str(a3), '\n ' )
y_aver1 = sum(a1) / len(a1)
y_aver2 = sum(a2) / len(a2)
y_aver3 = sum(a3) / len(a3)
print("Середній Y 1: "+str(y_aver1),"\nСередній Y 2: "+str(y_aver2),"\nСередній Y 3: "+str(y_aver3),'\n ')
a1_vidhul = [y_aver1 - a1[i] for i in range(len(a1))]
a2_vidhul = [y_aver1 - a2[i] for i in range(len(a2))]
a3_vidhul = [y_aver1 - a3[i] for i in range(len(a3))]
print("a1: "+str(a1_vidhul),"\na2: "+str(a2_vidhul),"\na3: "+str(a3_vidhul),'\n ')

a1_vidh_kvad = []
a2_vidh_kvad = []
a3_vidh_kvad = []
for i in range(len(a1)):
    a1_vidh_kvad.append(a1_vidhul[i] ** 2)
    a2_vidh_kvad.append(a2_vidhul[i] ** 2)
    a3_vidh_kvad.append(a3_vidhul[i] ** 2)
print("a1 квадратичне: "+str(a1_vidh_kvad), "\na2 Середній Y : "+str(a2_vidh_kvad),"\na3 Середній Y : "+str(a3_vidh_kvad), '\n')
a1_disp = sum(a1_vidh_kvad) / len(a1_vidh_kvad)
a2_disp = sum(a2_vidh_kvad) / len(a2_vidh_kvad)
a3_disp = sum(a3_vidh_kvad) / len(a3_vidh_kvad)
print("a1 дисперсія: "+str(a1_disp), "\na2 дисперсія: "+str(a2_disp),"\na3 дисперсія: "+str(a3_disp),'\n')
a1_disp_perc = a1_disp / (a1_disp + a2_disp + a3_disp)
a2_disp_perc = a2_disp / (a1_disp + a2_disp + a3_disp)
a3_disp_perc = a3_disp / (a1_disp + a2_disp + a3_disp)
print("a1 регрессія: "+str(a1_disp_perc),"a2 регрессія: "+str(a2_disp_perc), "a3 регрессія: "+str(a3_disp_perc), '\n ')
Fuv1 = a1_disp / a2_disp
Fuv2 = a3_disp / a1_disp
Fuv3 = a3_disp / a2_disp
print("Fuv1: "+str(Fuv1),"\nFuv2: "+str(Fuv2),"\nFuv3: "+str(Fuv3),'\n')
Ouv1 = 3/5*Fuv1
Ouv2 = 3/5*Fuv2
Ouv3 = 3/5*Fuv3
print("Ouv1: "+str(Ouv1),"\nOuv2: "+str(Ouv2),"\nOuv2\ 3: "+str(Ouv3),'\n')
Ruv1 = abs(Ouv1 - 1)/1.79
Ruv2 = abs(Ouv2 - 1)/1.79
Ruv3 = abs(Ouv3 - 1)/1.79
print("Ruv1: "+str(Ruv1),"\nRuv2: "+str(Ruv2),"\nRuv3: "+str(Ruv3))
print(str(Ruv1)+"<Rkr = 2\n",str(Ruv2)+"<Rkr = 2\n",str(Ruv3)+"<Rkr = 2\n")
mx1 = (-1+1+(-1))/3
mx2 = (-1+(-1)+1)/3
my = (y_aver1 + y_aver2+ y_aver3)/3
print("mx1: "+str(mx1),"\nmx2: "+str(mx2),"\nmy: "+str(my),'\n')
A1 = (1+1+1)/3
A2 = (1-1-1)/3
A3 = (1+1+1)/3
print("A1: "+str(A1),"\nA2: "+str(A2),"\nA3: "+str(A3),'\n')
A11 =(-1*y_aver1+1*y_aver2-1*y_aver3)/3
A22 =(-1*y_aver1-1*y_aver2+1*y_aver3)/3
print("A11: "+str(A11),"\nA22: "+str(A22),'\n')
b0 = (lg.det([[my, mx1, mx2],
                 [A11, A1, A2],
                 [A22, A2, A3]]))/(lg.det([[1, mx1, mx2],
                                               [mx1, A1, A2],
                                               [mx2, A2, A3]]))
b1 = (lg.det([[1, my, mx2],
                 [mx1, A11, A2],
                 [mx2, A22, A3]]))/(lg.det([[1, mx1, mx2],
                                               [mx1, A1, A2],
                                               [mx2, A2, A3]]))
b2 = (lg.det([[1, mx1, my],
                 [mx1, A1, A11],
                 [mx2, A2, A22]]))/(lg.det([[1, mx1, mx2],
                                               [mx1, A1, A2],
                                               [mx2, A2, A3]]))
print("b0: "+str(b0),"\nb1: "+str(b1),"\nb2: "+str(b2),'\n')
print("Y1 = : "+str(b0 + b1*-1 + b2*(-1)),"\nY2 = : "+str(b0 + b1*1 + b2*(-1)),"\nY3 = : "+str(b0 + b1*(-1) + b2*1))
print("Y = "+str(b0)+" + "+str(b1)+"*x1 + "+str(b2)+"*x2")
Dx1 = abs(x1_max-x1_min)/2
Dx2 = abs(x2_max-x2_min)/2
x10 = (x1_max+x1_min)/2
x20 = (x2_max+x2_min)/2
print("Dx1: "+str(Dx1),"\nDx2: "+str(Dx2),"\nx10: "+str(x10),'\nx20:'+str(x20),'\n')
a0 = b0-b1*(x10/Dx1)-b2*(x20/Dx2)
a1 = b1/Dx1
a2 = b2/Dx2
print("a0: "+str(a0),"\na1: "+str(a1),"\na2: "+str(a2),'\n')
print("Ynat1 = : "+str(a0 + a1*x1_min + a2*x2_min))
print("Ynat2 = : "+str(a0 + a1*x1_max + a2*x2_min))
print("Ynat3 = : "+str(a0 + a1*x1_min + a2*x2_max))
print("Ynat = "+str(a0)+" + "+str(a1)+"*x1 + "+str(a2)+"*x2")
print(" ")