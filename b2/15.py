import numpy as np

array_string = "1 2 3 4 5"
result_array = np.fromstring(array_string, sep=' ')
print(result_array)
