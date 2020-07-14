from demands import *
import numpy as np

#Slustky effects
#Compensated Icmome
def comIcm(pN,X):#Where pN is the price vector with the new prices
    #and X is the quantity demanded with original prices
    if len(pN)!=len(X): return print("Price and demands vector has different\
        lengths")
    
    return float(np.dot(pN,X)) #Returns the dot product transposing X 

def SubsEf(a,p,pN,m,ptype,s=None,A=None): #Computes substitution effect for a price change
    #A,a,p are the same parameters as the ones in utility functions
    #ptype is the preference utilifuncion type
    #cd:Cobb-Douglas; leo:Leontief; subs:perfect substitutes; ces:CES
    #Where A function constant, and s is the elasticity of substitution in CES function
    if len(p)!=len(pN) or len(p)!=len(a): return print("Invalid arguments p, pN, a length")
    if ptype=='leo' and A!=None: return print("Invalid parameter 'A'")
    if ptype=='CES' and s!=None: return print("CES function missing parameter 's")
    if ptype=='cd' and A==None: A=1
    if ptype=='subs' and A==None: A=0
    
    #set the kind of demand
    if ptype=='cd': dem=cdouglas 
    elif ptype=='leo': dem=leontief 
    elif ptype=='sus': dem=substitu
    #elif ptype=='ces': dem=CES
    
    X1=np.array(dem(A=A,a=a,p=p,m=m,d=0))
    comI=comIcm(pN=pN,X=X1)
    X2=np.array(dem(A=A,a=a,p=pN,m=comI,d=0))
    SubsEfX=tuple(X2-X1)
    return SubsEfX

def IcmEf(a,p,pN,m,ptype,s=None,A=None):
    if len(p)!=len(pN) or len(p)!=len(a): return print("Invalid arguments p, pN, a length")
    if ptype=='leo' and A!=None: return print("Invalid parameter 'A'")
    if ptype=='CES' and s!=None: return print("CES function missing parameter 's")
    if ptype=='cd' and A==None: A=1
    if ptype=='subs' and A==None: A=0

    #set the kind of demand
    if ptype=='cd': dem=cdouglas 
    elif ptype=='leo': dem=leontief 
    elif ptype=='sus': dem=substitu
    #elif ptype=='ces': dem=CES
    
    Xp1=np.array(dem(A=A,a=a,p=p,m=m,d=0)) #calculates x(p,m)
    comI=comIcm(pN=pN,X=Xp1)
    Xp2Icm2=np.array(dem(A=A,a=a,p=pN,m=comI,d=0)) #calculates x(p',m')
    Xp2Icm1=np.array(dem(A=A,a=a,p=pN,m=m,d=0)) #calculates x(p',m)
    IcmEfX=tuple(Xp2Icm1-Xp2Icm2)
    return IcmEfX


def SlskyEf(a,p,pN,m,ptype,s=None,A=None):
    if len(p)!=len(pN) or len(p)!=len(a): return print("Invalid arguments p, pN, a length")
    if ptype=='leo' and A!=None: return print("Invalid parameter 'A' for utility function")
    if ptype=='CES' and s!=None: return print("CES function missing parameter 's")
    if ptype=='cd' and A==None: A=1
    if ptype=='subs' and A==None: A=0
    SubsEfX=np.array(SubsEf(a=a,p=p,pN=pN,m=m,ptype=ptype,s=s,A=A))
    IcmEfX=np.array(IcmEf(a=a,p=p,pN=pN,m=m,ptype=ptype,s=s,A=A))
    SlskyEfX=tuple(SubsEfX+IcmEfX)
    return SlskyEfX


print(SubsEf(a=[4/7,3/7],p=[1,3],pN=[2,3],m=30,ptype='leo'))
print(IcmEf(a=[4/7,3/7],p=[1,3],pN=[2,3],m=30,ptype='leo')) #so far both work fine
print(SlskyEf(a=[4/7,3/7],p=[1,3],pN=[2,3],m=30,ptype='leo')) #so far both work fine
    












