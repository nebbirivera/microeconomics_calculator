import matplotlib.pyplot as plt
import numpy as np
from calc import *

def pltCdouglas(A,ax,ay,px,py,m): #Plots indifference curves, budget constraint
    #and solution for a two-good consumer theory utility maximization problem
    #in  perfect competition with Cobb-Douglas utility.
    xO=cdouglas(A,[ax,ay],[px,py],m,d=0)[0]
    yO=cdouglas(A,[ax,ay],[px,py],m,d=0)[1]
    x=np.linspace(xO/2,2*xO,100) #Creates an a
    bgtF=lambda m,px,py,x: m/py -(px/py)*x #Calcula la restricción presupuestaria
    cd=lambda ax,ay,x,y,A: A*((x)**(ax))*((y)**(ay)) #Calcula la utilidad de una CD
    lvl=lambda h,A,x,ax,ay: (h/(A*x**ax))**(1/ay) #Calcula la función de la isocuanta 
    h=cd(ax=ax,ay=ay,x=xO,y=yO,A=A) #Calculamos la utilidad resultado de optimizar
    isqO=lvl(h=h,A=A,x=x,ax=ax,ay=ay) #Calcula los puntos de la isocuanta
    isq1=lvl(h=h*0.85,A=A,x=x,ax=ax,ay=ay) #Calcula los puntos de la isocuanta
    isq2=lvl(h=h*1.15,A=A,x=x,ax=ax,ay=ay) #Calcula los puntos de la isocuanta
    bgtL=bgtF(m=m,px=px,py=py,x=x) #Calcula los puntos de la rest. pres.
    plt.plot(x,bgtL,'#4f94ff',label='Budget const.') #
    plt.plot(x,isqO,'#ff4f4f',label='$U^*$')
    plt.plot(x,isq1,'0.75')
    plt.plot(x,isq2,'0.75')
    plt.plot(xO,yO,'ko',label='$(x^*,y^*)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
#plot_dem(a=5/3,b=2/3,px=12,py=43,m=500)

#pltCdouglas(A=1,ax=1/3,ay=2/3,px=2,py=3,m=50)
    
def pltLeontief(ax,ay,px,py,m):
    xO,yO=leontief([ax,ay],[px,py],m,d=0)[0],leontief([ax,ay],[px,py],m,d=0)[1]
    x=np.linspace(xO/2,xO*2,100)
    vLx,hLy=np.full(50,xO),np.full(50,yO) #x points for vertical and horizontal part isoquant
    hLx,vLy=np.linspace(xO,2*xO,50),np.linspace(yO,2*yO,50) #y points for vertical and hor. part isoquant
    bgtF=lambda m,px,py,x: m/py -(px/py)*x 
    leoF=lambda ax,ay,x: x*ax/ay
    bgtL=bgtF(m,px,py,x)
    ExPath=leoF(ax,ay,x)
    vLx2,hLy2=np.full(50,xO*1.2),np.full(50,yO*1.2) #other upper isoquant setter
    hLx2,vLy2=np.linspace(xO*1.2,2*xO,50),np.linspace(yO*1.2,2*yO,50) 
    vLx3,hLy3=np.full(50,xO*0.8),np.full(50,yO*0.8) #other lower isoquant setter
    hLx3,vLy3=np.linspace(xO*0.8,2*xO,50),np.linspace(yO*0.8,2*yO,50)
    plt.plot(vLx,vLy,'#ff7c00')
    plt.plot(hLx,hLy,'#ff7c00')
    plt.plot(vLx2,vLy2,'0.8')
    plt.plot(hLx2,hLy2,'0.8')
    plt.plot(vLx3,vLy3,'0.8')
    plt.plot(hLx3,hLy3,'0.8')
    plt.plot(x,bgtL,'#009eff',label='Budget const.')
    plt.plot(x,ExPath,'#8fbbff', label='Expansion path')  
    plt.plot(xO,yO,'ko', label='$(x^*,y^*)$')
    plt.legend()
    plt.show()

def pltSubsitu():
    pass
def pltConWel(a,b,p): #Where demand is: q(p)=a+bp lineal
#Plots demand, price and consumer welfare in perfect competition
    qFp=lambda a,b,x: a+b*x #Calcula la función de demandada inversa
    pFq=lambda a,b,x: -(a/b)+x/b #Calcula la funcion de demanda
    qE=qFp(a=a,b=b,x=p) #Calcula las cantidades demandadas al precio de mdo.
    x=np.linspace(0,qE*2,100) #Crea un array para los valores de x (q)
    y=pFq(a=a,b=b,x=x) #Crea el array para los valores de y (p) demanda
    pV=np.full(100,p) #Crea un array para los valores de p, perf. elástico
    plt.plot(x,y,'#4f94ff',label='Demand') #Grafica la curva de demanda
    plt.plot(x,pV,'#ff462d',label='$p$'+" = "+str(p)) #Grafica el precio perf. elástico
    xE=np.linspace(0,qE,100) #Crea un array para sombrear el excedente
    yE=pFq(a=a,b=b,x=xE) #Crea un array para sombrear el excedente
    plt.fill_between(xE,yE,pV,color='#ffb973',alpha=0.5,label='Cons. Surplus') #Sombrea el exc. del consumidor
    plt.ylabel('$q(p)$')
    plt.xlabel('$p$')
    plt.legend()
    plt.show()  
pltConWel(20,-1,6)
def pltProdWel():
    pass