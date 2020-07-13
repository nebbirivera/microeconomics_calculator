
def cdouglas(A,a,p,m,plot=0,d=1):
    #Consumer where a is a list with alpha values in order from 1 to n.
    #p is a list with prices values order from 1 to n.
    #m is a scalar representing the income
    #m is an optional argument detailing if the user wants a decorated output (1)
    #or just return a list with the results
    if len(a)!=len(p): 
        return print("Unvalid arguments length.")
    X=[] #Stores the demand values for each
    for i in range(len(p)):
        X.append(a[i]*m/(sum(a)*p[i]))
    if d==1:
        pass #incluir output
    elif d==0: X=tuple(X); return X #Returns only marshallian demand

def leontief(a,p,m,plot=0,d=1,A=1): #We put A variable that is not used for convenience of slsky
    if len(a)!=len(p): 
        return print("Unvalid arguments length.")
    X=[]
    paSum=sum([pi/ai for pi,ai in zip(p,a)])
    for i in range(len(p)):
        X.append(m/(a[i]*paSum))
    if d==1:
        pass
    elif d==0: X=tuple(X); return X

def substitu(A,a,p,m,plot=0,d=1):
    if len(a)!=len(p): 
        return print("Unvalid arguments length.")
    X=[]
    pass

#Slustky effects
#Compensated income
def comInc(pN,X):#Where pN is the price vector with the new prices
    #and X is the quantity demanded with original prices
    if len(pN)!=len(X): return print("Price and demands vector has different\
        lengths")

    import numpy as np
    return float(np.dot(pN,X)) #Returns the dot product transposing X 

def SubsEf(a,p,pN,m,ptype,s=None,A=None): #Computes substitution effect for a price change
    #A,a,p are the same parameters as the ones in utility functions
    #ptype is the preference utilifuncion type
    #cd:Cobb-Douglas; leo:Leontief; subs:perfect substitutes; ces:CES
    #Where A function constant, and s is the elasticity of substitution in CES function
    if len(p)!=len(pN) or len(p)!=len(a): return print("Invalid arguments p, pN, a length")
    if ptype=='leo' and A!=None: return print("Invalid parameter 'A'")
    if ptype=='CES' and s!=None: return print("CES function missing parameter 's")
    #set the kind of demand
    if ptype=='cd': dem=cdouglas 
    elif ptype=='leo': dem=leontief 
    elif ptype=='sus': dem=substitu
    #elif ptype=='ces': dem=CES

    import numpy as np
    X1=np.array(dem(A=A,a=a,p=p,m=m,d=0))
    comI=comInc(pN=pN,m=m)
    X2=np.array(dem(A=A,a=a,p=pN,m=comI,d=0))
    SubsEfX=tuple(X2-X1)
    return SubsEfX


    








#print(leontief([1/3,2/3],[3,4],50,d=0))

