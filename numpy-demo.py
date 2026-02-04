import numpy as np
import matplotlib.pyplot as plt
from numpy_toolkit import *

# Demos
print("=== NumPy Numerical Computing Toolkit ===\n")

a, b = create_arrays()
print("1D array:", a, "shape:", a.shape)
print("2D array:\n", b, "shape:", b.shape)

print("\n=== Vectorized Operations ===")
vectorized_ops()

print("\n=== Linear Algebra ===")
linear_algebra_demo()

data = generate_demo_data(1000)
stats_analysis(data)

# Visualization
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(np.cumsum(data[:, 0]))
plt.title('Cumulative Sum')

plt.subplot(1, 2, 2)
plt.scatter(data[:, 1], data[:, 2], alpha=0.5)
plt.title('Correlation Scatter')
plt.xlabel('Col 2'); plt.ylabel('Col 3')

plt.tight_layout()
plt.savefig('arrays.png', dpi=150)
plt.show()

print("\nDemo complete! Check arrays.png")
