# Machine Learning Zoomcamp – Week 1: Linear Algebra Foundations

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.26-blue)](https://numpy.org/)

This repository documents my journey through **Week 1** of the **Machine Learning Zoomcamp**, a comprehensive 4-month course offered by **DataTalksClub**. Week 1 focuses on building the **mathematical foundation** required for machine learning, including linear algebra and matrix operations.

---

## 📘 Week 1 Overview

The goal of this week was to understand the mathematical underpinnings of machine learning algorithms. Key topics included:

- **Matrix Operations**: Matrix multiplication, transposition, and inversion.
- **Linear Algebra Fundamentals**: Dot products, matrix shapes, and their relevance in ML.
- **Practical Applications**: Implementing linear algebra concepts using Python and NumPy.

---

## 🔧 Exercises and Implementations

The exercises involved:

- Computing the transpose of a matrix `X` and performing `X.T @ X`.
- Inverting the resulting matrix `(X.T @ X)^(-1)`.
- Using the inverse to solve linear equations, a fundamental step in linear regression.

---

## 🧪 Example Problem

One of the exercises included:

1. Creating a dataset:

```python
y = [1100, 1300, 800, 900, 1000, 1100, 1200]
````

2. Computing `X.T @ X`, inverting it, multiplying by `X.T`, and then multiplying by `y` to get the weight vector `w`.

```python
import numpy as np

# Example steps
XTX = X.T @ X
XTX_inv = np.linalg.inv(XTX)
w = XTX_inv @ X.T @ y
```

3. Summing all elements of `w` to analyze the result:

```python
total_weight = np.sum(w)
print("Sum of weights:", total_weight)
```

---

## 🛠️ Technologies Used

* **Python** – Programming language for implementation
* **NumPy** – Efficient numerical computations and linear algebra
* **Jupyter Notebooks** – Interactive environment for running exercises

---

## 📌 Key Takeaways

* Mastering linear algebra is essential for understanding machine learning algorithms.
* Operations like matrix multiplication and inversion form the core of regression and many ML models.
* Hands-on exercises help translate theoretical concepts into practical applications.

---

## 🔗 Resources

* [Machine Learning Zoomcamp](https://github.com/DataTalksClub/mlzoomcamp) – Official course repository
* [NumPy Documentation](https://numpy.org/doc/) – For matrix operations and linear algebra
* [Jupyter Notebooks](https://jupyter.org/) – Interactive coding environment

```
