import plotly.express as px
import csv
import numpy as np
def plotFigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df, x="days Present", y="marks in %")
        fig.show()

def getDataSource(data_path):
    marks_in_percentage=[]
    days_presrnt=[]
    with open (data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["marks in percentage"]))
            days_present.append(float(row["Days Present"]))
return{"x":marks_in_percentage, "y":days_present}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"], datasource["y"])
    print("correlation between marks and dates")

def setup():
    data_path="size_of_tv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    plotfigure(data_path)
setup()
