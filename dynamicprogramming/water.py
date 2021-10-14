import numpy as np
import matplotlib.pyplot as plt
heights = [10, 5, 2, 9, 7, 8]
n = len(heights)
heights = [0] + heights + [0]
minmaxheights = [[max(heights[:i]), heights[i], max(heights[i + 1:]), min(max(heights[:i]), max(heights[i + 1:])),
                  0 if (min(max(heights[:i]), max(heights[i + 1:])) - heights[i]) <0 else (min(max(heights[:i]), max(heights[i + 1:])) - heights[i])] for i in range(1, n + 1)]
print(minmaxheights)

labels = [x for x in range(len(heights))]
colors = ['red', 'teal', 'pink']
plt.bar(labels, heights, color=colors)

plt.xlabel("Building")
plt.ylabel("Height")
plt.title("Buildings and Heights")
# plt.show()
