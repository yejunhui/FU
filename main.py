from flask import Flask,render_template,url_for,request,redirect,make_response
from random import randint
import time
import d

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    #判断method形式
    if request.method == 'POST':
        #获得用户名和密码
        d.user = request.form['user']
        d.password = request.form['password']
        #判断是否同意服务协议
        if 'checkbox' in request.form:
            d.userList[d.user]=[d.password]
            #比对用户是否存在
            if d.user in d.userListT:
                    #比对密码
                    if d.userList[d.user][0] == d.userListT[d.user]:
                        d.r = str(randint(0,99999))
                        d.ran.append(d.r)
                        resp = make_response(redirect(url_for('index')))
                        resp.set_cookie('ran',d.r)
                        d.userList[d.user]=d.password
                        return resp
                    else:
                        return render_template('login.html', t=d.t, user=d.user, ts='密码错误！')
            else:
                return render_template('login.html', t=d.t, user='',ts = '没有找到用户信息！')
        else:
            return render_template('login.html', t=d.t, user='', ts='请同意服务协议！')
    else:
        return render_template('login.html',t = d.t,user=d.user)



@app.route('/loginIn',methods=['GET','POST'])
def loginIn():
    if request.method == 'POST':
        if 'checkbox' in request.form:
            if request.form['password'] == request.form['password2']:
                d.user = user = request.form['user']
                if user in d.userListT:
                    return redirect(url_for('login',t=d.t,user=user,ts='用户已经注册！'))
                else:
                    password = request.form['password']
                    email = request.form['email']
                    phone = request.form['phone']
                    d.userListT[user]=[password,email,phone,time.localtime(time.time())]
                    return redirect(url_for('login', t=d.t, user=user, ts='注册成功！请登录！'))
            else:
                return render_template('loginIn.html', t=d.t, user=d.user,ts='输入的再次密码不一致！')
        else:
            return render_template('loginIn.html', t=d.t, user=d.user,ts='请同意服务协议!')
    else:
        return render_template('loginIn.html',t = d.t,user=d.user)

@app.route('/index')
def index():
    if request.cookies.get('ran') in d.ran:
        return render_template('index.html',t = d.t,user=d.user,password='********')
    else:
        return redirect(url_for('login',t=d.t))

@app.route('/plan')
def plan():
    return render_template('plan.html',t = d.t,user=d.user)

@app.route('/stick')
def stick():
    return render_template('stock.html',t = d.t,user=d.user)

@app.route('/gold')
def gold():
    return render_template('gold.html',t = d.t,user=d.user)

@app.route('/sunnyGirl')
def sunnyGirl():
    return render_template('sunnyGirl.html',t = d.t,user=d.user)

@app.route('/cls')
def cls():
    resp = make_response(redirect(url_for('login',t=d.t)))
    if d.user in d.userList:
        del d.userList[d.user]
    d.user = ''
    d.password = ''
    d.ran.remove(d.r)
    resp.delete_cookie('ran')
    return resp



#运行
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)