import numpy as np
import time
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 100)
y = np.cos(x)

# Enable interactive mode
plt.ion()


figure, ax = plt.subplots(figsize=(8,6))
line1, = ax.plot(x, y)


plt.title("Dynamic Sine Wave Plot",fontsize=25)


plt.xlabel("x",fontsize=18)
plt.ylabel("y",fontsize=18)


for p in range(1000):
    updated_y = np.cos(x-0.05*p)
   
    line1.set_xdata(x)
    line1.set_ydata(updated_y)
   
    figure.canvas.draw()
   
    figure.canvas.flush_events()
    time.sleep(0.1)