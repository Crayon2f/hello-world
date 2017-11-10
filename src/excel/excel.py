# coding=utf-8
# 操作excel
import xlwt
from datetime import datetime

wb = xlwt.Workbook()
ws = wb.add_sheet('first sheet')
ws.write(0, 0, 1234.56)
wb.save('example.xls')
