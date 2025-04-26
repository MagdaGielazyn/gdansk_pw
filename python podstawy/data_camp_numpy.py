import numpy as np
python_list = [4, 6, 9, 8]
array = np.array(python_list)
print(array)

print(type(array))

python_list_of_list = [[1,2], [3,4], [5,6]]
array = np.array(python_list_of_list)
print(array)

array_zero = np.zeros((5,3))
print(array_zero)


array_random = np.random.random((5,3))

print(array_random)

array_arange1 = np.arange(-5, 5)
array_arange2 = np.arange(5)
array_arange3 = np.arange(-3, 4, 3)
print(array_arange1, array_arange2, array_arange3)

from matplotlib import pyplot as plt
plt.scatter(np.arange(0,7), np.arange(-3,4))
plt.show()