
# Imports
from sidekit.bosaris import DetPlot
from sidekit.bosaris.detplot import __probit__ as probit
import numpy as np
import matplotlib.pyplot as plt
from random import gauss

# Creating DetPlot
detPlot = DetPlot()

# Creating figure with matplotlib
fig = plt.figure()
detPlot.__figure__ = fig


# Defining Tar and Non Tar
detPlot.__tar__ = np.asarray([
    [gauss(0.8, 0.07) for i in range(1000)],
    [gauss(0.6, 0.1) for i in range(1000)]
])

detPlot.__non__ = np.asarray([
    [gauss(0.4, 0.1) for i in range(1000)],
    [gauss(0.5, 0.1) for i in range(1000)]
])

# Naming the two plots
detPlot.__sys_name__ = ["good system", "bad system"]

# Defining the title does not seem to work with matplotlib
#detPlot.setTitle("") # Does not work
detPlot.__title__ = "Det curve plot example"

# Defining plot title
plt.title(detPlot.__title__)

# Defining plots
detPlot.plot_steppy_det(idx=0, plot_args=((0.6, 0, 0), '-', 2))
detPlot.plot_steppy_det(idx=1)
# As you can see, you can give as argument the plot_args,
# which is a tuple of size three => (color, line style, line size)

# Modifiate ticks with rates
range_ratios = np.arange(0.1, 1, 0.1)
ax = plt.gca()
xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()
plt.xticks(list(probit(range_ratios)) + [xmin, xmax], ["{:.1f}".format(i) for i in range_ratios] + [0, 1])
plt.yticks(list(probit(range_ratios)) + [ymin, ymax], ["{:.1f}".format(i) for i in range_ratios] + [0, 1])
plt.tick_params(axis="both", labelsize="5")

plt.xlabel("false acceptance rate")
plt.ylabel("false rejection rate")

# Finally, we show only in pdf mod !
plt.savefig("example1.pdf")