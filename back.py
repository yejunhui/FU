#后台
from random import randint
import time
import d
import pmysql,files

p = pmysql.pmysql()

def init():
    it= []
    for item in p.msql('show tables;'):
        for i in item:
            it.append(i)
    if 'users' not in it:
        p.msql('create table users (user text,name text,password text,email text,phone text,createDate double,oldDate double,ran double);')

#登录
def loginVerify(user,password):
    init()
    cont={}
    cont['In']= False
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
                cont['In']= True
                cont['ran']= ran
                return cont
            else:
                return cont
        else:
            return cont
    else:
        return cont

#注册
def loginUpVerify(conts):
    init()
    cont= {}
    sql = 'select user from users where \'user=%s\''%conts['user']
    ruser = p.msql(sql)
    if ruser != ():
        if conts['user'] in ruser[0]:
            cont['In']= False
            return cont
    else:
        sql = 'insert into users (user,password,email,phone,name,createDate) values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');'%(conts['user'],conts['password'],conts['email'],conts['phone'],conts['name'],str(time.time()))
        re = p.msql(sql)
        cont['In']= True
        cont['re']= re
        return cont

#主页
def indexVerify(ran):
    init()
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

    oldDate= time.localtime(int(oldDate[0][0]))
    oldDate = str(oldDate.tm_year)+'/'+str(oldDate.tm_mon)+'/'+str(oldDate.tm_mday)+'/'+str(oldDate.tm_hour)+':'+str(oldDate.tm_min)+':'+str(oldDate.tm_sec)

    createDate=time.localtime(int(createDate[0][0]))
    createDate=str(createDate.tm_year)+'/'+str(createDate.tm_mon)+'/'+str(createDate.tm_mday)+'/'+str(createDate.tm_hour)+':'+str(createDate.tm_min)+':'+str(createDate.tm_sec)

    cont={'user':user,'password':password,'email':email,'phone':phone,'name':name,'oldDate':oldDate,'createDate':createDate,'ran':ran}

    return cont

def login(user):
    init()
    sql = 'update users set ran=Null where user=\'%s\';'%(user)
    p.msql(sql)

def nowMod(conts):
    init()
    sql = 'update users set name=\'%s\',password=\'%s\',email=\'%s\',phone=\'%s\',ran=\'%s\' where user=\'%s\';'%(conts['name'],conts['password'],conts['email'],conts['phone'],conts['ran'],conts['user'])
    p.msql(sql)

def cls():
    p.cls()