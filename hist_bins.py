import numpy as np
import random
import math

def hist_bins(data):
    data = sorted(data)
    print(data)
    ranges = []
    if (len(data) < 2):
        print("Not enough data provided.")
        exit()

    _min = min(data)
    _max = max(data)
    _range = _max - _min
    number_of_intervals = math.floor(math.sqrt(len(data)))
    interval_len = math.ceil(_range / number_of_intervals)


    data_org_dict = {}

    for i in np.arange(_min, _max, interval_len):
        ranges.append((i, i+interval_len))


    data_org = []

    for x in data:
        for y in ranges:
            if (y[0] <= x and y[1] >= x):
                index = str(y[0]) + "-" + str(y[1])

                if (index not in data_org_dict):
                    data_org_dict[index] = [x]
                else:
                    data_org_dict[index] = data_org_dict[index] + [x]
                data_org.append((y, x))
                break

    return data_org_dict