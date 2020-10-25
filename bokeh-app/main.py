
''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve sliders.py
at your command prompt. Then navigate to the URL
    http://localhost:5006/sliders
in your browser.
'''
import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure

# Set up data
mu = 0
sigma = 1
N = 200
x = np.linspace(-10,10, N)
y = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))

source = ColumnDataSource(data=dict(x=x, y=y))


# Set up plot
plot = figure(plot_height=400, plot_width=400, title="Normal Distribution 正态分布",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[-10, 10], y_range=[0, 0.5])

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)


# Set up widgets
text = TextInput(title="图：", value='Normal Distribution 正态分布')
mean = Slider(title="Mean 均值", value=0.0, start=-5.0, end=5.0, step=0.1)
sd = Slider(title="Standard Deviation 标准差", value=1.0, start=1.0, end=10.0, step=0.1)


# Set up callbacks
def update_title(attrname, old, new):
    plot.title.text = text.value

text.on_change('value', update_title)

def update_data(attrname, old, new):

    # Get the current slider values
    mu = mean.value
    sigma = sd.value

    # Generate the new curve
    x = np.linspace(-10,10, N)
    y = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))

    source.data = dict(x=x, y=y)

for w in [mean, sd]:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = column(text, mean, sd)

curdoc().add_root(row(plot, inputs, width=800))
curdoc().title = "Normal Distribution 正态分布"