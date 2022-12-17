#用时间换空间，尽可能减少迭代次数
import numpy as np
class cell:
    '''创建元胞数据类型'''
    def __init__(self,value=0):
        self.value=value
        self.is_iterate=True
        self.neighbors=[]
    def set_value(self,value=0):
        self.value=value
    def set_is_iterate(self,bool=True):
        self.is_iterate=bool
    def set_neighbors(self,NeighborsList):
        self.neighbors=NeighborsList
    def iterate(self,x,y,z,deltaq,beta=1,f=0,g=0):
        if self.is_iterate:
            sum=0
            for neighbor in self.neighbors:
                sum+=neighbor.value
            # new_value=(sum-deltaq**2*f)/(len(self.neighbors)-deltaq**2*g)#f,g传值
            new_value=(sum-deltaq**2*f(x,y,z))/(len(self.neighbors)-deltaq**2*g(x,y,z))#f,g传函数
            delta_value=new_value-self.value
            value=self.value+beta*delta_value
            self.set_value(value)
def Initial(xlist,ylist,zlist,set_Boundary):
    '''初始化元胞(添加邻近元胞列表)并设置边界条件'''
    Nx,Ny,Nz=len(xlist),len(ylist),len(zlist)
    #创建元胞网格点
    UMatCell=cellList=[[[cell() for irow in range(Nx)]
                        for icol in range(Ny)]
                        for ihei in range(Nz)]#只能使用列表推导式
    UMatCell=np.array(UMatCell)#转换为ndarray数据格式方便用UMatCell[i,j,k]形式的索引
    for i in range(Nx):
        for j in range(Ny):
            for k in range(Nz):
                set_Boundary(xlist[i],ylist[j],zlist[k],UMatCell[i,j,k])#设置边界条件
                # 暂时采用取余的办法规避索引溢出的问题
                NeighborsList=[UMatCell[(i-1)%Nx,j,k],UMatCell[(i+1)%Nx,j,k],
                            UMatCell[i,(j-1)%Ny,k],UMatCell[i,(j+1)%Ny,k],
                            UMatCell[i,j,(k-1)%Nz],UMatCell[i,j,(k+1)%Nz],]
                UMatCell[i,j,k].set_neighbors(NeighborsList)
    return UMatCell
def Iteration(xlist,ylist,zlist,tN,UMatCell,f,g,beta=1):
    '''迭代'''
    deltaq=xlist[1]-xlist[0]#x,y,z三个方向的离散化程度相同
    Nx,Ny,Nz=len(xlist),len(ylist),len(zlist)
    shape=np.shape(UMatCell)
    UMatValue=np.zeros(shape)#不能使用empty_like或zeros_like
    UMatValue_tmp=np.zeros(shape)
    for t in np.arange(tN):
        if not (t+1)%10:
            deltaU=abs((np.sum(UMatValue)-np.sum(UMatValue_tmp))/Nx/Ny/Nz)
            print('deltaU=%e'%deltaU)
        for i in range(Nx):
            for j in range(Ny):
                for k in range(Nz):
                    x,y,z=xlist[i],ylist[j],zlist[k]
                    UMatValue_tmp[i,j,k]=UMatValue[i,j,k]
                    # UMatCell[i,j,k].iterate(x,y,z,deltaq,beta,f(x,y,z),g(x,y,z))#f,g传值
                    UMatCell[i,j,k].iterate(x,y,z,deltaq,beta,f,g)#f,g传函数
                    UMatValue[i,j,k]=UMatCell[i,j,k].value
    return UMatValue