import matplotlib.pyplot as plt

## scatter plots
x = [2, 4, 6, 8, 10]
y = [6, 7, 4, 2, 9]

plt.scatter(x, y, label="Sc1", color="r", marker="^")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Simple graph")

plt.legend()

plt.show()
