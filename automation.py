from openpyxl import Workbook
from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series,
)

wb = Workbook()
ws = wb.active

rows = [
    ['Product Id', 'June', 'September', 'December', 'January'],
    [1, 4, 20, 40, 25],
    [2, 22, 32, 43, 54],
    [3, 30, 55, 21, 12],
    [4, 2, 3, 1, 4],
    [5, 50, 35, 2, 62],
    [6, 2, 3, 12, 5],
]

for row in rows:
    ws.append(row)

chart = ScatterChart()
chart.title = "Products Sales"
chart.style = 12
chart.x_axis.title = "Products Id"
chart.y_axis.title = "Sales"

xvalues = Reference(ws, min_col=1, min_row=2, max_row=7)
for i in range(2, 6):
    values = Reference(ws, min_col=i, min_row=1, max_row=7)
    series = Series(values, xvalues, title_from_data=True)
    chart.series.append(series)

ws.add_chart(chart, "A10")

wb.save("automatePy.xlsx")