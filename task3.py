import sys

def task_3(cashs):
    time = [0]*16
    k=0
    maks = 0
    for cash in cashs:
        for i in cash:
            if k<16:
                time[k] += i
                k+=1
        k=0
    # print(time)
    for i in time:
        if i > maks:
            maks=i
    print(time.index(maks)+1)


if __name__ == '__main__':
    path = sys.argv[1:]
    cash = []
    for i in range(len(path)):
        cash.append([])
        with open(path[i]) as f:
            for line in f:
                cash[i].append(float(line))

    # print(cash)
    task_3(cash)