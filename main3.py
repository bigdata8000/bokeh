from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
from bokeh.embed import components
import pandas

# Read in csv
df = pandas.read_csv('cars.csv')

#Create ColumnDataSource from data frame
source = ColumnDataSource(df)
output_file('index3.html')

# Car list
car_list = source.data['Car'].tolist()

# Add plot
p = figure(
    y_range=car_list,
    plot_width=800,
    plot_height=600,
    title='Cars with Top Horsepower',
    x_axis_label='Horsepower'
)

p.toolbar.logo=None
# p.toolbar_location=None

# Render glyph
p.hbar(
   y='Car',
   right='Horsepower',
   left=0,
   height=0.4,
   color='orange',
   fill_color=factor_cmap(
       'Car',
       palette=Blues8,
       factors=car_list
   ),
   fill_alpha=0.9,
   source=source,
   #legend='Car'
)

# Add Tooltips
hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@Car</h3>
        <div><strong>Price: </strong>@Price</div>
        <div><strong>Horsepower: </strong>@Horsepower</div>
        <div><img src="@Image" alt="" width="200" /> </div>
    </div>
"""

p.add_tools(hover)  

# Show results
show(p)
