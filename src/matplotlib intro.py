import matplotlib.pyplot as plt
import numpy as np
import math


print("learn matplotlib")

x_points = np.array([2,10])
y_points = np.array([7,200])

print(x_points)
print(y_points)

# plt.plot(x_points, y_points)
# plt.show()

major_categories = ['Computing', 'Engineering', 'Physical Sciences', 'Life Sciences', 'Mathematics']
job_openings = [122000, 57000, 10000, 10000, 9000]
degrees_awarded = [40000, 77000, 19000, 110000, 19000]

x_axis = np.arange(len(job_openings))

plt.figure(figsize=(10,5))
plt.bar(x_axis-0.2, job_openings, 0.4, label='Jobs')
plt.bar(x_axis+0.2, degrees_awarded, 0.4, label='Grads')

plt.xticks(x_axis, major_categories)
plt.ylabel('Job Opening')
plt.title("2022 Annual Total U.S. STEM Jobs")

plt.legend()
plt.show()

t = np.linspace(0, math.pi, 1000)
x = np.sin(t)
y = np.cos(t) + np.power(x, 2.0/3)

plt.scatter(x,y,c=y,cmap=plt.cm.Reds,edgecolors='None',s=40)
plt.scatter(-x,y,c=y,cmap=plt.cm.Reds,edgecolors='None',s=40)

plt.axis([-2,2,-2,2])
plt.title("Love", fontsize=20)
plt.show()