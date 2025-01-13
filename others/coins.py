import numpy as np

N = 5  # 这里可以根据你的需求修改 N 的值，表示行数
array = np.random.randint(2, size=(N, 9))

for row in array:
    print(row)

for col in range(array.shape[1]):
    ones_count = np.sum(array[:, col])
    zeros_count = N - ones_count
    if zeros_count > ones_count:
        array[:, col] = 1 - array[:, col]

print("\n处理后的数组：")
for row in array:
    print(row)