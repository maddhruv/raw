import matplotlib.pyplot as plt

## stack plots
x = [2, 4, 6, 8, 10]

a = [4, 5, 6, 7, 5]
b = [8, 9, 10, 8, 8]
c = [7, 8, 8, 7, 8]

plt.stackplot(x, a, b, c, colors=["m","b","r"])

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Simple graph")

plt.legend()

plt.show()
