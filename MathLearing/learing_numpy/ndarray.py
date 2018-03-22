#coding=utf-8
import numpy as np
# ndarray 简介
# ndarray 是 numpy 库中 一个固定大小,同数据类型的数组容器。
#   NumPy数组的维数称为秩（rank），一维数组的秩为1，二维数组的秩为2，以此类推。在NumPy中，
#   每一个线性的数组称为是一个轴（axes），秩其实是描述轴的数量。比如说，二维数组相当于是一个一维数组，而这个一维数组中每个元素又是一个一维数组。所以这个一维数组就是
#   NumPy中的轴（axes），而轴的数量——秩，就是数组的维数。

# ndarray attributes:
# ndarray.flags 数组的内部信息
# ndarray.shape 数组行列信息.
# ndarray.strides 遍历数组时在每个维度中步骤的字节元组。
# ndarray.ndim 数组的维数
# ndarray.data 数组的起始内存地址.
# ndarray.size 获取数组中元素个数.
# ndarray.itemsize 数组中元素类型所占用的内存大小.
# ndarray.nbytes 数组元素占用的总字节数.
# ndarray.base 数组的基对象
# ndarray.dtype 数组元素的类型
arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]

# ndarray 构造函数
ndarr = np.array(arr)
print("ndarray.flags: ",ndarr.flags)
print("ndarray.shape: ",ndarr.shape)
print("ndarray.strides: ",ndarr.strides)
print("ndarray.ndim: ",ndarr.ndim)
print("ndarray.size: ",ndarr.size)
print("ndarray.itemsize: ",ndarr.itemsize)
print("ndarray.data: ",ndarr.data)
print("ndarray.base: ",ndarr.base)
print("ndarray.nbytes: ",ndarr.nbytes)

# other attributes
#ndarray.T 当前矩阵的转置矩阵.  Same as self.transpose(), except that self is returned
#if self.ndim < 2.
#ndarray.real 数组的真正部分 The real part of the array.
#ndarray.imag 数组的虚部分 The imaginary part of the array.  如果是一个实数矩阵 则 虚部全部为零
#ndarray.flat 数组上的 一维 迭代器 A 1-D iterator over the array.
#ndarray.ctypes 一个对象, 用于简化数组与 ctypes 模块的交互。 An object to simplify the
#interaction of the array with the ctypes module.

print(" A * A \r\n",ndarr * ndarr.T)
print("ndarray.T: \r\n",ndarr.T)
print("ndarray.real: \r\n",ndarr.real)
print("ndarray.imag: ",ndarr.imag)
print("ndarray.flat: ",ndarr.flat)
print("ndarray.ctypes: ",ndarr.ctypes)

# ndarray methods
#An ndarray object has many methods which operate on or with the array in some
#fashion, typically returning an array result.  These methods are briefly
#explained below.  (Each method’s docstring has a more complete description.)

#For the following methods there are also corresponding functions in numpy:
#all, any, argmax, argmin, argpartition, argsort, choose, clip, compress, copy,
#cumprod, cumsum, diagonal, imag, max, mean, min, nonzero, partition, prod,
#ptp, put, ravel, real, repeat, reshape, round, searchsorted, sort, squeeze,
#std, sum, swapaxes, take, trace, transpose, var.

# Array conversion
#ndarray.item(*args) Copy an element of an array to a standard Python scalar
#and return it.
#ndarray.tolist() Return the array as a (possibly nested) list.
#ndarray.itemset(*args) Insert scalar into an array (scalar is cast to array’s
#dtype, if possible)
#ndarray.tostring([order]) Construct Python bytes containing the raw data bytes
#in the array.
#ndarray.tobytes([order]) Construct Python bytes containing the raw data bytes
#in the array.
#ndarray.tofile(fid[, sep, format]) Write array to a file as text or binary
#(default).
#ndarray.dump(file) Dump a pickle of the array to the specified file.
#ndarray.dumps() Returns the pickle of the array as a string.
#ndarray.astype(dtype[, order, casting, ...]) Copy of the array, cast to a
#specified type.
#ndarray.byteswap([inplace]) Swap the bytes of the array elements
#ndarray.copy([order]) Return a copy of the array.
#ndarray.view([dtype, type]) New view of array with the same data.
#ndarray.getfield(dtype[, offset]) Returns a field of the given array as a
#certain type.
#ndarray.setflags([write, align, uic]) Set array flags WRITEABLE, ALIGNED,
#(WRITEBACKIFCOPY and UPDATEIFCOPY), respectively.
#ndarray.fill(value) Fill the array with a scalar value.

#https://www.leiphone.com/news/201706/QprrvzsrZCl4S2lw.html
print("ndarray.flat: ",ndarr)
print(ndarr.sort())
