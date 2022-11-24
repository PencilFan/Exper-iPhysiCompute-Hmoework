//不同于Python头文件函数需要用.h文件格式而不是.c文件格式
//
#include <stdio.h>
#include <math.h>
#include "pi_Func.h"
int main()
{
    double precision=1e-4;
    double result_Leibniz=pi_Leibniz(precision);
    double result_Euler=Euler(precision);
    double result_Ramanujan=Ramanujan_calc(precision);
    printf(
        "result_Leibniz=%f\nresult_Euler=%f\nresult_Ramanujan=%lf"
        ,result_Leibniz,result_Euler,result_Ramanujan
        );
    return 0;
}