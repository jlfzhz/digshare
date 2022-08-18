import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-5,5,50)
y1 = x1*2
y2 = x1**2-10

plt.figure(figsize=(5,4))
plt.plot(x1, y1)
plt.plot(x1, y2, color="Green", linewidth=3.0, linestyle="--")
plt.savefig("..\\images\\2-1.png")

# plt.show()

plt.subplot(1,2,1)
plt.plot(x1,y1)
plt.subplot(1,2,2)
plt.plot(x1,y2)
# plt.show()


fig = plt.figure(figsize=(9.6,4.8))
ax1 = plt.subplot(121)
ax1.plot(x1,y1)
ax1.spines['right'].set_color('None')

ax2 = plt.subplot(122)
ax2.plot(x1,y2)
ax2.spines['left'].set_color('None')
ax2.yaxis.set_visible(False)
plt.show()
