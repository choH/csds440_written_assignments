import matplotlib.pyplot as plt
import random
import numpy as np

# random.seed(0)


def w(bound):
    return [random.uniform(-bound, bound) for i in range(0, 6)]

def sigmoid(z):
    return 1/(1 + np.exp(-z))

# w = w(10)
w = w(3)
# w = w(0.1)
print(w)

x1_pos = []
x2_pos = []
x1_neg = []
x2_neg = []

def get_pts(w):
    x1 = random.uniform(-5, 5)
    x2 = random.uniform(-5, 5)

    u1 = sigmoid(x1 * w[0] + x2 * w[1])
    u2 = sigmoid(x1 * w[2] + x2 * w[3])
    y = sigmoid(u1 * w[4] + u2 * w[5])

    if y >= 0.5:
        x1_pos.append(x1)
        x2_pos.append(x2)
    else:
        x1_neg.append(x1)
        x2_neg.append(x2)

# w = w(3)
# w = w(0.1

for i in range(10000):
    get_pts(w)



plt.scatter(x1_pos, x2_pos, c = 'lightblue')
plt.scatter(x1_neg, x2_neg, c = 'coral')

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()
