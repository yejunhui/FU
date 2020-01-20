#文件文件需要用到pmysql模块

import pmysql
import d,files

p = pmysql.pmysql()

#导入BOM
def bomIn(cont):
    cont['file']= files.readExcel(cont['fileName'])
    for c in cont['file']:
        sql = 'select erp from BOM where erp=\'%s\';'%c[0]
        r = p.msql(sql)
        if c[0] not in r[0]:
            sql = 'insert into users (erp,name,class,dosage,period,nump,unit) values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');'%(cont[0],cont[1],cont[2],cont[3],cont[4],cont[5],cont[6])
            p.msql(sql)
        else:
            pass
#导入盘点表
def excelIn(fileName):
    pass

#导出BOM
def excelBomOut():
    cont= {}
    cont['fileName'] = 'BOM导入模板'
    cont['dat'] = d.bom
    files.dowExcel(cont)

#导出盘点表
def excelCheckOut():
    cont = {}
    cont['fileName']= '盘点导入模板'
    cont['dat'] = d.check
    files.dowExcel(cont)
