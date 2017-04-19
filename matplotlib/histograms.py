import matplotlib.pyplot as plt

## histograms
x = [2, 4, 6, 8, 10, 12, 14, 15, 25, 24, 20, 32, 35, 33, 45, 46, 26, 50]

bins = [0, 10, 20, 30, 40, 50]

plt.hist(x, bins, histtype="bar", rwidth=0.8)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Simple graph")

plt.legend()

plt.show()
