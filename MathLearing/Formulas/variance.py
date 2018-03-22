##coding=utf-8
##计算方差
#import numpy as np

#'''
#计算方差
#Note:方差是衡量源数据与期望值相差的度量值
#'''
#def CalculateVariance(array):
#    sum = 0.0
#    summean = 0.0    
#    N = len(array)
#    for x in array:
#        sum+=x
#        summean += x ** 2 #平方
#    av = sum / len(array)#平均数 （期望值）
#    var = summean / N - av ** 2 #方差
#    return var

#def CalculateVarianceByNumpy(array):
#    n = len(array) #h获取数据项个数
#    narray = np.array(array)
#    sum1 = narray.sum()
#    narray2 = narray * narray#矩阵相乘
#    sum2 = narray2.sum()
#    av = sum1 / n
#    var = sum2 / n - av ** 2     
#    return var

#rand = [10.0,5.0,2.0,3.0,9.0]
#print(CalculateVariance(rand))
#print(CalculateVarianceByNumpy(rand))
