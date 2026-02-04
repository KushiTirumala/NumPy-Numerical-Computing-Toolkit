import numpy as np
from typing import Tuple

def create_arrays() -> Tuple[np.ndarray, np.ndarray]:
    """Array creation and basics."""
    a = np.array([1, 2, 3, 4])
    b = np.array([[1, 2], [3, 4]])
    return a, b

def vectorized_ops():
    """Broadcasting and universal functions."""
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])
    
    print("Element-wise add:", x + y)
    print("Matrix multiply:", np.dot(x, y))
    print("Broadcast scalar:", x * 2)
    print("Stats:", np.mean(x), np.std(x))

def linear_algebra_demo():
    """Matrix operations."""
    A = np.array([[1, 2], [3, 4]])
    b = np.array([5, 6])
    
    # Solve Ax = b
    x = np.linalg.solve(A, b)
    print("Linear system solution:", x)
    
    # Eigenvalues
    eigvals = np.linalg.eigvals(A)
    print("Eigenvalues:", eigvals)

def stats_analysis(data: np.ndarray):
    """Statistical functions."""
    print("Mean:", np.mean(data))
    print("Median:", np.median(data))
    print("Correlation:", np.corrcoef(data))

def generate_demo_data(n: int = 1000):
    """Random data for testing."""
    return np.random.randn(n, 3)
