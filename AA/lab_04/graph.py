import matplotlib.pyplot as plt
import numpy as np

def inter(x, y):
    degree = 3

    A = np.vander(x, degree + 1, increasing=True)

    coefficients = np.linalg.lstsq(A, y, rcond=None)[0]

    def polynomial_interpolator(coeffs, x_val):
        y_val = sum([coeffs[i] * x_val ** i for i in range(len(coeffs))])
        return y_val

    interpolated_y = [polynomial_interpolator(coefficients, val) for val in x]

    return interpolated_y

x = [0, 1, 2, 4, 8, 16, 32, 48, 64]
y = [31.24, 34.82, 30.73, 26.45, 24.03, 15.92, 11.05, 12.4, 11.66]

plt.plot(x, y, '.', c="blue")
plt.plot(x, inter(x, y), '--', c="blue")

plt.grid(True)
plt.xlabel("Число потоков")
plt.ylabel("Время работы, сек")

plt.savefig('graph.pdf')  

plt.show()
