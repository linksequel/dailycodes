import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 创建一个示例矩阵
matrix = np.array([[1, 2, 3], [4, 5, 6]])

def update(frame):
    if frame < matrix.shape[1]:
        temp_matrix = matrix.copy()
        for i in range(matrix.shape[0]):
            temp_matrix[i, frame] = matrix[frame, i]
        return temp_matrix
    else:
        return matrix.T

fig, ax = plt.subplots()
im = ax.imshow(matrix, cmap='viridis')

def init():
    im.set_data(matrix)
    return im,

animation = FuncAnimation(fig, update, frames=matrix.shape[1]+1, init_func=init, blit=True)

plt.show()