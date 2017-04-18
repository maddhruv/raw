import matplotlib.pyplot as plt

## bar charts
x = [2, 4, 6, 8, 10]
y = [6, 7, 4, 2, 9]
x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 3, 9, 1]

plt.bar(x, y, label="Bar1", color="r")
plt.bar(x2, y2, label="Bar2", color="g")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Simple graph")

plt.legend()

plt.show()
