import matplotlib.pyplot as plt

## lines, labels, title, legend
x = [1, 2, 3]
y = [5, 9, 3]
x2 = [1, 2, 3]
y2 = [1, 2, 3]

plt.plot(x, y, label="line")
plt.plot(x2, y2, label="reference")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Simple graph")

plt.legend()

plt.show()
