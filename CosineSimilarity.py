import numpy as np

a = np.array([1, 2])
b = np.array([2, 4])

similarity = np.dot(a, b) / (
    np.linalg.norm(a) * np.linalg.norm(b)
)

print(similarity)