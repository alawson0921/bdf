#File: bdf.py (Binary Decimal Fraction)
#Author: Adam Lawson
import math
from fractions import Fraction

##Finding the n term of the "fraction"

##Scaling Variables (Change only these variables)
depth = 10000000 ##search depth
depthlog = math.floor(math.log(depth,2))
numerator = 1
denominator = 19

##Binary Count
def ispoweroftwo(i):
    if float(math.log(i,2) == int(math.log(i,2))):
        return 1
    else:
        return 0

def binaryfactorization(i):
    c = 0
    if i==0:
        return 0
    elif i==1:
        return 1
    tempi = i
    while(tempi > 0):
        if(tempi == 1):
            return c
        elif(ispoweroftwo(tempi)):
            c+=1
            return c
        elif(tempi%2)==1:
            tempi = tempi - 1
            c+=1
        else:
            tempi=tempi - (2**math.floor(math.log(tempi,2)))
            c+=1

def findfrac(n, d):
    ##TODO: if numerator is larger than 2^n where n is the two power tier, print does not exist
    if(n>depthlog):
        print("Cannot Exist! We cannot have a numerator larger than log_2(denominator)!")
        return
    x = depth
    for i in range(1,x):
        num = binaryfactorization(d*i)
        den = d*i
        #if(num%i == n-1): ##skips dynamically
        if(num == n * i):
            print("Found: {0}/{1} -> {2}/{3} at {1}th term").format(num,den,n,d)
            return
        ##progress bar
        if(i == x * 0.05):
            print("Progress: full depth at 5%")
        elif i == x*0.1:
            print("Progress: full depth at 10%")
        elif i == x*0.15:
            print("Progress: full depth at 15%")
        elif i == x*0.20:
            print("Progress: full depth at 20%")
        elif i == x*0.25:
            print("Progress: full depth at 25%")
        elif i == x*0.30:
            print("Progress: full depth at 30%")
        elif i == x*0.35:
            print("Progress: full depth at 35%")
        elif i == x*0.4:
            print("Progress: full depth at 40%")
        elif i == x*0.45:
            print("Progress: full depth at 45%")
        elif i == x*0.50:
            print("Progress: full depth at 50%")
        elif i == x*0.55:
            print("Progress: full depth at 55%")
        elif i == x*0.60:
            print("Progress: full depth at 60%")
        elif i == x*0.65:
            print("Progress: full depth at 65%")
        elif i == x*0.7:
            print("Progress: full depth at 70%")
        elif i == x*0.75:
            print("Progress: full depth at 75%")
        elif i == x*0.8:
            print("Progress: full depth at 80%")
        elif i == x*0.85:
            print("Progress: full depth at 85%")
        elif i == x*0.9:
            print("Progress: full depth at 90%")
        elif i == x*0.95:
            print("Progress: full depth at 95%")
    print("Not found at depth {0}").format(x)

findfrac(numerator,denominator)