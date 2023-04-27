import numpy

def Newton(x_front,f,df,accuracy=1e-6,max_iter=100):
    '''
    牛顿法求解非线性方程
    :param x_front: x的初始值
    :param f: 函数
    :param df: 导数
    :param accuracy:精确度
    :param max_iter: 最大迭代次数
    :return: 无解或解的值
    '''
    for i in range(max_iter):
        x_back=x_front-f(x_front)/df(x_front)
        if abs(x_back-x_front)<accuracy:
            return x_back,i
        x_front=x_back
    return '该方程无解！'

if __name__ == '__main__':
    x0=int(input("请输入预测值："))
    f=lambda x:2*x*x+10/numpy.exp(x)-5
    df=lambda x:4*x-10/numpy.exp(x)

    ans=Newton(x0,f,df)
    if type(ans)==str:
        print(ans)
    else:
        print("近似解为{:6f}，迭代次数为{:d}".format(ans[0],ans[1]))