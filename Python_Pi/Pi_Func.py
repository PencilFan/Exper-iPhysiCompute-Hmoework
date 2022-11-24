from math import factorial, sqrt#不用引入pow
import decimal
# 注意Euler与Leibniz的初始n不能为0,而Ramanujan必须从0开始迭代
def pi_Euler(l):
     PiList = []
     s=0
     for n in range(1,l+1):
        an = 1/n**2
        s = s+an
        PiList.append(sqrt(s*6))
     return PiList
def pi_Leibniz(l):
    PiList=[]
    s=0
    for n in range(1,l+1):
        an=an=1/(2*n-1)*pow(-1,n-1)
        s=s+an
        PiList.append(4*s)
    return PiList
def pi_Ramanujan(l):
    PiList=[]
    s=0
    k=sqrt(8)/pow(99,2)
    for n in range(0,l):
        an=factorial(4*n)*(1103+26390*n)/pow(factorial(n),4)/pow(396,4*n)
        s=s+an
        PiList.append(1/(k*s))
    return PiList