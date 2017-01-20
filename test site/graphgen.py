import pygal
import random

def gengraph():
    datalist1 = []
    datalist2 = []
    for x in range(10):
        datalist1.append(random.randint(10,25))
    for x in range(10):
        datalist2.append(random.randint(50,85))

    line_chart = pygal.Line()
    line_chart.title = "Demo Graph"
    line_chart.x_labels = map(str, range(1,12))
    line_chart.add('A', datalist1)
    line_chart.add('B', datalist2)
    line_chart.render_to_file('test.svg')
