import openpyxl
import openpyxl.chart

class chart():
    def __init__(self):
        self.wb=openpyxl.Workbook()
        self.sheet=self.wb.get_active_sheet()
        self.i=1
    def WriteTime(self,timein):
        self.sheet['A'+str(self.i)]=float(timein)
        self.i+=1
    def DrawChart(self,name='sample',title=''):
        refObj=openpyxl.chart.Reference(self.sheet,1,1,1,self.i-1)
        seriesObj=openpyxl.chart.Series(refObj,title=title)
        chartObj=openpyxl.chart.LineChart()
        chartObj.append(seriesObj)
        chartObj.width=15
        chartObj.height=8
        self.sheet.add_chart(chartObj,'A'+str(self.i+2))
        self.wb.save(name+'.xlsx')

# if __name__ == '__main__':
#     c=chart()
#     c.WriteTime(int(1011))
#     c.WriteTime(str(1111))
#     c.WriteTime(3111)
#     c.DrawChart()