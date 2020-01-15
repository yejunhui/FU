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
ran = []
r = 0

userList = {}
userListT = {'root':'1220'}
