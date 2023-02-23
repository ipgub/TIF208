from sk_dsp_comm import *       # import every modules from the library
from numpy import *
from matplotlib.pyplot import *

#####################################################
#
# create discrete time axis
n = arange(-5, 15)

#####################################################
#
# create discrete time signals using sigsys module 'dstep'
x1 = sigsys.dstepmen(n)    # create DTS step function turns on at n = 0
x2 = sigsys.dstep(n-5)  # create DTS step function turns on at n = 5

# Third signal - difference
x3 = x1 - x2

#####################################################
#
# Plot the discrete time signals using Stem function.
# Stem function is defined in pyplot library

# First, create figure environment for the plot
fig, ax = subplots(3)
fig.suptitle('Discrete time signal')
# Plot the signal using stem function
ax[0].stem(n, x1)
# Add some additional features to the figure such as grid, label, etc
# ax[0].grid()                       # add gridt
ax[0].axis([ -5, 15, -0.1, 1.1])  # define the x and y axis of the plo
ax[0].set_xticks(n+1)

# second DTS
ax[1].stem(n, x2)
# ax[1].grid()                       # add grid
ax[1].axis([ -5, 15, -0.1, 1.1])  # define the x and y axis of the plot
ax[1].set_xticks(n+1)

# Third DTS = difference between x1 and x2
ax[2].stem(n,x3)
ax[2].axis([ -5, 15, -0.1, 1.1])
ax[2].set_xticks(n+1)

i = 1
for axs in ax.flat:
    axs.set(xlabel=r'Index - $n$', ylabel=r'$x_{idx:d}[n]$'.format(idx=i))
    i=i+1

# We can also save the figure to the file
savefig('mysignal.png')

# Show your figure on the terminal
show()

