import sys


def task_2_1(data_figure, data):
    for i in data:
        if i in data_figure:
            print(0)
            continue
        # elif (((i[0] - data_figure[0][0]) * (data_figure[1][1] - data_figure[0][1]) - (
        #         data_figure[1][0] - data_figure[0][0]) * (i[1] - data_figure[0][1]) == 0) or
        #       ((i[0] - data_figure[1][0]) * (data_figure[2][1] - data_figure[1][1]) - (
        #               data_figure[2][0] - data_figure[1][0]) * (i[1] - data_figure[1][1]) == 0) or
        #       ((i[0] - data_figure[2][0]) * (data_figure[3][1] - data_figure[2][1]) - (
        #               data_figure[3][0] - data_figure[2][0]) * (i[1] - data_figure[2][1]) == 0) or
        #       ((i[0] - data_figure[0][0]) * (data_figure[3][1] - data_figure[0][1]) - (
        #               data_figure[3][0] - data_figure[0][0]) * (i[1] - data_figure[0][1]) == 0)):
        #     print(1)
        #     continue
        elif ((data_figure[0][0] == i[0] == data_figure[1][0] and data_figure[0][1] <= i[1] <= data_figure[1][1]) or
              (data_figure[1][0] <= i[0] <= data_figure[2][0] and data_figure[1][1] == i[1] == data_figure[2][1]) or
              (data_figure[2][0] == i[0] == data_figure[3][0] and data_figure[2][1] >= i[1] <= data_figure[3][1]) or
              (data_figure[0][0] <= i[0] <= data_figure[3][0] and data_figure[0][1] == i[1] == data_figure[3][1])):
            print(1)
            continue
        elif (((i[0] - data_figure[0][0]) * (data_figure[1][1] - data_figure[0][1]) - (
                data_figure[1][0] - data_figure[0][0]) * (i[1] - data_figure[0][1]) > 0) and
               ((i[0] - data_figure[1][0]) * (data_figure[2][1] - data_figure[1][1]) - (
                       data_figure[2][0] - data_figure[1][0]) * (i[1] - data_figure[1][1]) > 0) and
               ((i[0] - data_figure[2][0]) * (data_figure[3][1] - data_figure[2][1]) - (
                       data_figure[3][0] - data_figure[2][0]) * (i[1] - data_figure[2][1]) > 0) and
               ((i[0] - data_figure[3][0]) * (data_figure[0][1] - data_figure[3][1]) - (
                       data_figure[0][0] - data_figure[3][0]) * (i[1] - data_figure[3][1]) > 0)):
            print(2)
            continue
        # elif (((data_figure[0][0] > i[0] or i[0] > data_figure[1][0]) and (data_figure[0][1] > i[1] or i[1] > data_figure[1][1])) or
        #     ((data_figure[1][0] > i[0] or i[0] > data_figure[2][0]) and (data_figure[1][1] > i[1] or i[1] > data_figure[2][1])) or
        #     ((data_figure[2][0] > i[0] or i[0] > data_figure[3][0]) and (data_figure[2][1] > i[1] or i[1] > data_figure[3][1])) or
        #       ((data_figure[0][0] > i[0] or i[0] > data_figure[3][0]) and (data_figure[0][1] > i[1] or i[1] > data_figure[3][1]))):
        #     print(3)
        #     continue
        else:
            print(3)
            continue


if __name__ == '__main__':
    path = sys.argv[1:]
    data_figure = []
    data = []
    with open(path[0]) as file_fig:
        for line in file_fig:
            data_figure.append([float(x) for x in line.split()])
    # print(data_figure)
    with open(path[1]) as f:
        for line in f:
            data.append([float(x) for x in line.split()])
    # print(data)
    task_2_1(data_figure, data)
