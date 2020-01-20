#数据文件

from time import localtime,time

#日期
#年
t = localtime(time())
ty = localtime(time()).tm_year
tm = localtime(time()).tm_mon
td = localtime(time()).tm_mday

#用户
user = ''
password = ''
checkbox = ''

userList = {}
userListT = {'root':'zxr.1220','user':'1220'}

dAge=[
    '本系统登录使用账号、密码、随机密码三码对照验证登录！',
    '我们不会以任何方式泄露您的个人信息！',
    '为保证你的账户和信息安全，使用结束后务必点击页面右上方的退出按钮进行退出！',
    '由于您个人使用不当造成的个人信息泄露，本团队概不负责！',
    '当系统为登录状态下会使用到COOKIE，会在用户本地系统存储COOKIE信息！',
    '您一但使用本系统即默认您已经认真阅读并同意服务协议！',
    '本团队保留有最终解释权！',
]

bom = [
    ['BOM导入模板'],
    ['不能更改格式'],
    [],
    [],
    ['erp-品号','name-名称','class-级别','dosage-用量','period-周期','nump-生产人数','unit-单位']
]
check =[
    ['盘点表导入模板'],
    ['不能更改格式'],
    [],
    [],
    ['erp-品号','num-结存数量','unit-单位']
]
