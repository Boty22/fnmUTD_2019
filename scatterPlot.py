##
## This sample program demonstrates reading from the samplePlotData.csv file
## and creating a basic scatter plot. The samplePlotData file contains data about
## loans purchased by Fannie Mae - specifically the Seller name, the Unpaid Balance (UPB),
## the Loan to Value (LTV), and the first three digits of the zip code the property
## is in.
##
## More data about each loan is available through the API for manufactured housing and on the
## DVD's for other types of property. This sample program is intended to give you some 
## exposure to reading and visualizing data using the Pandas and Bokeh libraries.
## Please google these library names for more information on the different types of
## visualizations you can create and how you can manupulate Pandas data.
##
## Note: you might get some warning when running the program about the numpy array size changing,
## you can ignore these warnings if they do pop up.
##

## import the libraries we need to run this program
## you might have to install the libraries if they're
## not already available on your computer. You can typically
## use 'pip install pandas' on Macintosh and Linux systems
## and 'easy_install pandas' on Windows systems.
##
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

## the columns in our sample dataset include the following
##
## Seller
## UPB
## LTV
## ZIP3

## read the data from our sample data file into a variable
## so that we can work with it in our program
#
acqData = pd.read_csv('samplePlotData.csv')

## uncomment the line below if you want to see the
## data we just read into the program
#
## print (acqData)

## uncomment the lines below if you want to see the
## headings on the 4 columns in our dataset
#
print ('-------------------------------')
print (acqData.columns.tolist())
print ('-------------------------------')

## create a file to display the results of our
## plot
#
output_file('scatterPlotOutput.html')

## grab just 100 records out of the complete file to
## include in the plot
##
sample = acqData.sample(100)

## convert out sample of 100 records into a source of
## data for the Bokeh library functions to use
##
source = ColumnDataSource(sample)

## create a new instance of a graph for us to start creating
## our graph
##
p = figure()

## define the x and y coordinate labels, identify the source of the data
## to be plotted, set the size of the circles we want to plot and set the 
## color of the circles
##
p.circle (x='UPB', y='LTV', source=source, size=10, color='green')

## add a title to the graph
#
p.title.text='Unpaid Balance vs Loan to Value'

## label the x axis
##
p.xaxis.axis_label = 'Loan to Value (LTV)'

## label the y axis
#
p.yaxis.axis_label = 'Unpaid Balance (UPB)'

## add an instance of the "hovertool". This will allow the graph to
## display actual values for each of the points plotted on the graph
##
hover = HoverTool()

## define the attributes the hovertool should display when we mouse over
## a point on the graph. Note that we give the hovertool a name to use
## along with the name of a column from our dataset
##
hover.tooltips = [
	('Seller', '@SELLER'),
	('Unpaid Balance', '@UPB'),
	('Loan to Value', '@LTV'),
	('Zip3', '@ZIP3')
]

## add the hovertool tips we just defined to the graph
## itself.
#
p.add_tools(hover)

## and finally - display the graph in the browser
#
show (p)












