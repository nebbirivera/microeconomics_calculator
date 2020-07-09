
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
    elif d==0: X=tuple(X); return X

def leontief(a,p,m,d=1):
    if len(a)!=len(p): 
        return print("Unvalid arguments length.")
    X=[]
    paSum=sum([pi/ai for pi,ai in zip(p,a)])
    for i in range(len(p)):
        X.append(m/(a[i]*paSum))
    if d==1:
        pass
    elif d==0: X=tuple(X); return X

def substitu():
    if len(a)!=len(p): 
        return print("Unvalid arguments length.")
    X=[]
    pass

#print(leontief([1/3,2/3],[3,4],50,d=0))

