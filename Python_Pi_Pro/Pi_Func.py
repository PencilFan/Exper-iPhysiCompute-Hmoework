from math import factorial, sqrt#不用引入pow
import numpy as np
# 注意公式迭代的初始值
def Euler(l):
     PiList=np.zeros(l)
     s=0
     for n in range(1,l+1):
        an = 1/n**2
        s = s+an
        PiList[n-1]=sqrt(s*6)
     return PiList
def Leibniz(l):
    PiList=np.zeros(l)
    s=0
    for n in range(1,l+1):
        an=an=1/(2*n-1)*pow(-1,n-1)
        s=s+an
        PiList[n-1]=4*s
    return PiList
def Ramanujan_by_myself(l):
    PiList=np.zeros(l)
    s=0
    k=sqrt(8)/pow(99,2)
    for n in range(0,l):
        an=factorial(4*n)*(1103+26390*n)/pow(factorial(n),4)/pow(396,4*n)
        s=s+an
        PiList[n]=1/(k*s)
    return PiList

from math import factorial,sqrt,log10
from decimal import Decimal, getcontext
import mpmath as mp
mp.dps = 100000  # number of digits
def ramanujan_by_igfasouza(max_step):
    """ Computing an approximation of pi with a Ramanujan's formula."""
    getcontext().prec = max_step*10  # trick to improve precision
    PiList=[]
    Sum = Decimal(0)
    d_1103 = Decimal(1103)
    d_26390 = Decimal(26390)
    d_396 = Decimal(396)
    for k in range(max_step):
        Sum += ((Decimal(factorial(4 * k))) * (d_1103 + d_26390 * Decimal(k))) / ( (Decimal(factorial(k)))**4 * (d_396**(4*k)))
        my_pi_multiple_factor = Sum * 2 * Decimal(2).sqrt() / Decimal(9801)
        my_pi_reciprocal  = my_pi_multiple_factor**(-1)
        PiList.append(my_pi_reciprocal)
    return PiList