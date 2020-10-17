import numpy as np
import matplotlib.pyplot as plt


def get_box(a, b):
    box = np.concatenate([np.ones(a), np.zeros(b)])
    np.random.shuffle(box)
    return box

def get_numerator(data, pro, prior):
    n_1 = sum(data)
    n_0 = len(data) - n_1

    return pow(pro[0], n_1) * pow(pro[1], n_0) * prior

def get_denominator(data, pros, priors):
    denominator = 0
    for i in range(3):
        denominator+= get_numerator(data, pros[i], priors[i])
    return denominator

def get_post_probability(box, N, pros, priors, type):
    # generate data with N number
    data = box[:N]
    numerator = get_numerator(data, pros[type], priors[type])
    denominator = get_denominator(data, pros, priors)
    return numerator / denominator


box_1 = get_box(80, 20)
box_2 = get_box(55, 45)
box_3 = get_box(30, 70)

pro = [[0.8, 0.2],
        [0.55, 0.45],
        [0.3, 0.7]]

prior = [1/3, 1/3, 1/3]

def left_C(Box, N):
    data = Box[N:]
    n_1 = sum(data)
    n_0 = len(data) - n_1

    return n_0 / len(data)


# Q26
p = [0.2, 0.45, 0.7]
x = [i for i in range(1, 101)]
# y = [0.2]
# y = [0.45]
y = [0.7]

for i in range(1, 100):
    temp = 0
    for idx in range(3):
        # temp += left_C(box_1, i) * get_post_probability(box_1, i, pro, prior, idx)
        # temp += left_C(box_2, i) * get_post_probability(box_1, i, pro, prior, idx)
        temp += left_C(box_3, i) * get_post_probability(box_1, i, pro, prior, idx)
    y.append(temp)

print(y)
plt.plot(x, y)
plt.show()