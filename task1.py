import sys
import math
import numpy as np

def mediana(data):
    size = len(data)
    k = size//2
    if size%2==0:
        return 0.5*(data[k]+data[k-1])
    else:
        return data[k]

def average(data):
    s = 0
    for i in range(len(data)):
        s += data[i]
    return s/len(data)


def task_1_1(data):
    a = np.array(data)
    p = np.percentile(a, 90)
    print("%.2f" %p)


def task_1_2(data):
    med = mediana(data)
    print("%.2f" % med)


def task_1_3(data):
    max_ = max(data)
    print("%.2f" % max_)


def task_1_4(data):
    min_ = min(data)
    print("%.2f" % min_)


def task_1_5(data):
    aver = average(data)
    print("%.2f" % aver)


if __name__ == '__main__':
    path = sys.argv[1]
    data = []
    with open(path) as f:
        for line in f:
            data.append(float(line))
    data.sort()
    # print(path)
    # path = "input1.txt"
    task_1_1(data)
    task_1_2(data)
    task_1_3(data)
    task_1_4(data)
    task_1_5(data)
