import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from collections import namedtuple
import pdb

Colour = namedtuple('Colour', ['unsorted', 'curr_index', 'sorted', 'facecolour'])

# Tells the program how to draw the graph
# Only called once. at the very start
def init_animate():
    i = 0
    for bar in bars:
        bar.set_height(ypos[i])
        i += 1

def index_gen():
    # First iteration
    yield -1, -1

    for i in range(0, SAMPLES):
        yield i, 0
        for j in range(i, SAMPLES):
            yield j, 1

    yield i, 2
 
    yield i, 3

def animate(data):
    i, flag = data
    
    if flag == 1:
        global lowest_num
        global lowest_position
        bars[i].set_color(COLOURS.unsorted)
        bars[i].set_edgecolor('black')
        if i < SAMPLES - 1:
            bars[i + 1].set_color(COLOURS.curr_index)
            bars[i + 1].set_edgecolor('black')
        if bars[i].get_height() < lowest_num:
            lowest_num = bars[i].get_height()
            lowest_position = i

    if flag == 0:
        if i == 0:
            pass
        else:
            bars[SAMPLES - 1].set_color(COLOURS.unsorted)
            bars[SAMPLES - 1].set_edgecolor('black')
            tmp = bars[i - 1].get_height()
            bars[i - 1].set_height(lowest_num)
            bars[lowest_position].set_height(tmp)
            bars[i - 1].set_color(COLOURS.sorted)
            bars[i - 1].set_edgecolor('black')
            lowest_num = SAMPLES + 1

    # Finished case, setting the 2nd last bar color
    elif flag == 2:
        bars[i].set_color(COLOURS.sorted)
        bars[i].set_edgecolor('black')
        bars[i].set_alpha(1)
        bars[i - 1].set_color(COLOURS.curr_index)
        bars[i - 1].set_edgecolor('black')
        bars[i - 1].set_alpha(1)

    # Finished Case, setting the last bar color
    elif flag == 3:
        bars[i - 1].set_color(COLOURS.sorted)
        bars[i - 1].set_edgecolor('black')
        bars[i - 1].set_alpha(1)
    return bars

global SAMPLES, ypos, bars

SAMPLES = 40 # Amount of data points to sort
SPEED = 10 # in milliseconds, lower is faster
lowest_num = SAMPLES + 1

# 'Colour', ['unsorted', 'curr_index', 'sorted', 'facecolour']
COLOURS = Colour('#eaeaea', '#ff2e63', '#252a34', '#08d9d6')


# Create the figure and the axes, figzise is the size of the window
fig, ax = plt.subplots(figsize=(20, 5))
ax.set_facecolor(COLOURS.facecolour)

# horiz(xpos) -> 1 - 100 in order, vertical(ypos) -> 1 - 100 random
xpos = range(1, SAMPLES + 1)
ypos = random.sample(range(1, SAMPLES + 1), SAMPLES)

# Draw the bars for the chart
bars = ax.bar(xpos, ypos, alpha=1, color=COLOURS.unsorted, edgecolor='black')

# Run the code to animate the bar graph
ani = FuncAnimation(fig, animate, frames=index_gen, repeat=False, init_func=init_animate, interval=SPEED)

# Draw the graph
plt.show()