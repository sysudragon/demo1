#-*- coding:utf-8 -*-
"""
@author: lxl
@date:0921

import numpy as np

def doubleArray(arr):
    """对每个元素进行翻倍"""

    arr = np.arrap(arr)

    return arr*2
if __name___=='__main__':
    arr=[1,2,3,4]
    print(doubleArray(arr))
