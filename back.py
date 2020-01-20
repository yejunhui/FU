#后台
from random import randint
import time
import d
import pmysql,files

p = pmysql.pmysql()

def loginVerify(user,password):
    sql = 'select user from users where user=\'%s\''%user
    ruser = p.msql(sql)
    if ruser != ():
        if user in ruser[0]:
            sql = 'select password from users where user=\'%s\''%user
            rpassword = p.msql(sql)
            if password in rpassword[0]:
                ran = randint(0,99999999)
                sql = 'update users set ran=%s,oldDate=%s where user=\'%s\''%(ran,time.time(),user)
                p.msql(sql)
                return True,ran
            else:
                return False,'密码不正确！'
        else:
            return False,'用户未注册！'
    else:
        return False,'出错'

def loginInVerify(conts):
    sql = 'select user from users where \'user=%s\''%conts['user']
    ruser = p.msql(sql)
    if ruser != ():
        if conts['user'] in ruser[0]:
            return False,'用户已经注册！'
    else:
        sql = 'insert into users (user,password,email,phone,name,createDate) values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');'%(conts['user'],conts['password'],conts['email'],conts['phone'],conts['name'],str(time.time()))
        r = p.msql(sql)
        return True,r

def indexVerify(ran):
    sql = 'select user from users where ran=\'%s\''%ran
    sql2 = 'select password from users where ran=\'%s\''%ran
    sql3 = 'select email from users where ran=\'%s\'' % ran
    sql4 = 'select phone from users where ran=\'%s\'' % ran
    sql5 = 'select name from users where ran=\'%s\'' % ran
    sql6 = 'select oldDate from users where ran=\'%s\'' % ran
    sql7 = 'select createDate from users where ran=\'%s\'' % ran
    user = p.msql(sql)
    password = p.msql(sql2)
    email = p.msql(sql3)
    phone = p.msql(sql4)
    name = p.msql(sql5)
    oldDate = p.msql(sql6)
    createDate = p.msql(sql7)

    oldDate= time.localtime(oldDate[0][0])
    oldDate = str(oldDate.tm_year)+'/'+str(oldDate.tm_mon)+'/'+str(oldDate.tm_mday)+'/'+str(oldDate.tm_hour)+':'+str(oldDate.tm_min)+':'+str(oldDate.tm_sec)

    createDate=time.localtime(createDate[0][0])
    createDate=str(createDate.tm_year)+'/'+str(createDate.tm_mon)+'/'+str(createDate.tm_mday)+'/'+str(createDate.tm_hour)+':'+str(createDate.tm_min)+':'+str(createDate.tm_sec)

    cont={'user':user,'password':password,'email':email,'phone':phone,'name':name,'oldDate':oldDate,'createDate':createDate,'ran':ran}

    return cont

def login(user):
    sql = 'update users set ran=Null where user=\'%s\';'%(user)
    p.msql(sql)

def my(conts):
    sql = 'update users set name=\'%s\',password=\'%s\',email=\'%s\',phone=\'%s\',ran=\'%s\' where user=\'%s\';'%(conts['name'],conts['password'],conts['email'],conts['phone'],conts['ran'],conts['user'])
    p.msql(sql)

def cls():
    p.cls()