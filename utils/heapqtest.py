# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: heapqtest.py
@time: 2020/7/3 14:12
@desc:
"""

import heapq
from heapq_showtree import show_tree
import random


data = [19, 9, 4, 10, 11]
heap = []


# 重新单元素开始创建heap
def create():
    for i in data:
        heapq.heappush(heap, i)
        show_tree(heap)


# 由内存中已有数据进行heap化
def recreate():
    heapq.heapify(data)
    show_tree(data)


# 访问heap元素
def visitheap():
    recreate()
    for i in range(4):
        small = heapq.heappop(data)
        print("popped: ", small)
        show_tree(data)


# 替换heap顶部元素
def replaceheap():
    recreate()
    for i in [0, 13, 10]:
        small = heapq.heapreplace(data, i)
        show_tree(data)


# 堆的数据极值
def maxandmin():
    print('3 largest :', heapq.nlargest(3, data))
    print('3 smallest:', heapq.nsmallest(3, data))


# 归并排序
def mergesort():
    new_data_list = []
    for i in range(4):
        new_data = list(random.sample(range(1, 101), 5))
        new_data.sort()
        new_data_list.append(new_data)

    for i, d in enumerate(new_data_list):
        print('{}: {}'.format(i, d))
    print("merged!")
    for i in heapq.merge(*new_data_list):
        print(i, end=' ')


if __name__ == '__main__':
    # create()
    # recreate()
    # visitheap()
    # replaceheap()
    # maxandmin()
    mergesort()