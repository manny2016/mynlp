#coding=utf-8
"""
行列式演练
"""
import numpy as np

det2 = [[1,5],
        [3,4]]

det3 = [[2,3,5],
        [3,3,6],
        [2,8,9]]

#将数组转换为 numpy 中的数组 ndarray 类型
#ndarray 是一个固定大小的同类型数据的数组的容器。可以通过 .shape 来得到数组的维度。
array1 = np.array(det2)
array2 = np.array(det3)
print(array1.shape) # 输出 2,2
print(array2.shape) # 输出 3,3
print(array2.dtype) # 输出 int32
print(np.linalg.det(array1)) #输出行列式值
print(np.linalg.det(array2)) #输出行列式值

print("ndim: ",array1.ndim) #输出 数组的 秩 (读 [zhì] )
print("ndim: ",array2.ndim) #输出 数组的 秩 (读 [zhì] )

