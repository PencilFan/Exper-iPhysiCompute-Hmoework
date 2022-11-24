/*莱布尼茨公式是交错级数可以直接用an来判断精度,但欧拉公式与拉马努金公式都不能用an或sn+1-sn来判断,
为简便起见,在这里用已知的标准数值3.1415926535进行判断*/
double pi_Leibniz(double precision)
{
    double n,an=10,s=0,tmp=precision+1;
    for(n=1;fabs(tmp)>precision;n++)
    {
        an=1/(2*n-1)*pow(-1,n-1);
        s=s+an;
        tmp=an*4;
    }
    return 4*s;
}
double Euler(double precision)
{
    double an=0,n,s=0;
    for(n=1;fabs(sqrt(s*6)-3.1415926535)>precision;n++)
    {
        an=1/pow(n,2);
        s=s+an;
    }
    return sqrt(s*6);
}
double Ramanujan_calc(double precision)
{
    double fact(double n);//函数要提前申明
    double n,k,s=0,an=0;
    k=sqrt(8)/pow(99,2);
    for(n=0;fabs(1/(k*s)-3.1415926535)>precision;n++)
    {
        an=fact(4*n)*(1103+26390*n)/pow(fact(n),4)/pow(396,4*n);
        s=s+an;
    }
    return 1/(k*s);
}
double fact(double n)
{
    double output=1;
    int i;
    for(i=1;i<=n;i++)
    {
         output=output*i;  
    }
    return output;
}