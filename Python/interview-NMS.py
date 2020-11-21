# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: interview-NMS.py
@time: 2020/11/21 9:04 下午
@desc:
手写nms算法

算法逻辑:
输入: n 行 4 列的候选框数组, 以及对应的 n 行 1 列的置信度数组.
输出: m 行 4 列的候选框数组, 以及对应的 m 行 1 列的置信度数组, m 对应的是去重后的候选框数量
算法流程:

计算 n 个候选框的面积大小
对置信度进行排序, 获取排序后的下标序号, 即采用argsort
将当前置信度最大的框加入返回值列表中
获取当前置信度最大的候选框与其他任意候选框的相交面积
利用相交的面积和两个框自身的面积计算框的交并比, 将交并比大于阈值的框删除.
对剩余的框重复以上过程

"""


import numpy as np

# def py_nms(boxes, threshold):
#     x1 = boxes[:, 0]
#     y1 = boxes[:, 1]
#     x2 = boxes[:, 2]
#     y2 = boxes[:, 3]
#     score = boxes[:, 4]
#
#     areas = (x2 - x1 + 1) * (y2 - y1 + 1)
#     order = np.argsort(score)
#
#     picked_boxes = []
#     while order.size > 0:
#         index = score[-1]
#         picked_boxes.append(index)
#
#         xx1 = np.maximum(x1[index], x1[order[1:]])
#         yy1 = np.maximum(y1[index], y1[order[1:]])
#         xx2 = np.minimum(x2[index], x2[order[1:]])
#         yy2 = np.minimum(y2[index], y2[order[1:]])
#
#         w = np.maximum(0.0, xx2 - xx1 + 1)
#         h = np.maximum(0.0, yy2 - yy1 + 1)
#
#         interArea = w * h
#
#         # 计算重叠度IOU：重叠面积/（面积1+面积2-重叠面积）
#
#         iou = interArea / (areas[index], areas[order[:-1]] - interArea)
#
#         left = np.where(iou < threshold)
#         order = order[left]
#     return picked_boxes

def py_nms(dets, thresh):
    """Pure Python NMS baseline."""
    #x1、y1、x2、y2、以及score赋值
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]

    #每一个候选框的面积
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    print("areas:")
    print(areas)
    #order是按照score降序排序的
    order = scores.argsort()[::-1]
    print("order:")
    print(order)

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        #计算当前概率最大矩形框与其他矩形框的相交框的坐标，会用到numpy的broadcast机制，得到的是向量
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        #计算相交框的面积,注意矩形框不相交时w或h算出来会是负数，用0代替
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        #计算重叠度IOU：重叠面积/（面积1+面积2-重叠面积）
        ovr = inter / (areas[i] + areas[order[1:]] - inter)

        #找到重叠度不高于阈值的矩形框索引
        inds = np.where(ovr <= thresh)[0]
        #将order序列更新，由于前面得到的矩形框索引要比矩形框在原order序列中的索引小1，所以要把这个1加回来
        order = order[inds + 1]
    return keep

if __name__ == '__main__':
    dets = np.array([[30, 20, 230, 200, 1],
                     [50, 50, 260, 220, 0.9],
                     [210, 30, 420, 5, 0.8],
                     [430, 280, 460, 360, 0.7]])
    thresh = 0.35
    keep_dets = py_nms(dets, thresh)
    print(keep_dets)
    print(dets[keep_dets])
