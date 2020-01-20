#文件操作类
#本文件需要乃至库os,openpyxl,xlrd,d
import os,openpyxl,xlrd
import d as ds

#excel

#写入excel
def dowExcel(cont):
    fp = os.getcwd()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = cont['fileName']
    ws.sheet_properties.tabColor = '1072ba'

    for d in cont['dat']:
        ws.append(d)
    wb.save(fp+'\\files\\'+cont['fileName']+'.xlsx')

#读取excle
def readExcel(cont):
    dat =[]
    wb = xlrd.open_workbook(cont[0]+'.xlsx')
    sheet = wb.sheets()[0]
    max_rows = sheet.nrows
    max_cols = sheet.ncols

    for i in range(5,max_rows):
        dat.append(sheet.row_values(i))

    return dat



#file