import os

from flask import Flask, render_template, url_for, request, redirect, make_response, flash, send_from_directory
from random import randint
import time
import d
import pmysql
import back
import files
import plan as pp
import goldCode

app = Flask(__name__)

fp = os.getcwd() + '/files'


# 登录验证
def verify(request):
    cont = {}
    if 'ran' in request.cookies:
        uc = request.cookies.get('user')
        pc = request.cookies.get('password')
        ran = request.cookies.get('ran')
        cont = back.indexVerify(ran)
        cont['user'] = cont['user'][0][0]
        cont['name'] = cont['name'][0][0]
        cont['password'] = cont['password'][0][0]
        cont['email'] = cont['email'][0][0]
        cont['phone'] = cont['phone'][0][0]
        cont['uc'] = uc
        cont['pc'] = pc
        cont['In'] = True

        return cont
    else:
        cont['In'] = False

        return cont


# 登录验证
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    cont = {}
    if request.method == 'POST':
        resp = make_response(redirect(url_for('index')))
        cont['user'] = request.form['user']
        cont['password'] = request.form['password']
        contLogin = back.loginVerify(cont['user'], cont['password'])
        if contLogin['In']:
            cont['ran'] = contLogin['ran']
            resp.set_cookie('user', cont['user'])
            resp.set_cookie('ran', str(cont['ran']))
            return resp
        else:
            cont['ts'] = '用户信息有误，请核对后重试！'
            return render_template('login.html', cont=cont)
    else:
        return render_template('login.html', cont=cont)


# 注册
@app.route('/loginUp', methods=['GET', 'POST'])
def loginUp():
    cont = {}
    if request.method == 'POST':
        cont['password'] = request.form['password']
        if cont['password'] == request.form['password2']:
            cont['user'] = request.form['user']
            cont['name'] = request.form['name']
            cont['password'] = request.form['password']
            cont['email'] = request.form['email']
            cont['phone'] = request.form['phone']
            cont = back.loginUpVerify(cont)
            if cont['In']:
                return redirect(url_for('login'))
    else:
        return render_template('loginUp.html')


# 主页
@app.route('/index', methods=['GET', 'POST'])
def index():
    cont = {}
    cont = verify(request)
    if cont['In']:
        return render_template('index.html', cont=cont)
    else:
        return redirect(url_for('login'))


# 我的家
@app.route('/myFamily', methods=['GET', 'POST'])
def myFamily():
    cont = {}
    cont = verify(request)
    if cont['In']:
        return render_template('myfamilyhome.html', cont=cont)
    else:
        return redirect(url_for('login'))


# 我的图片展
@app.route('/myPhotoShow', methods=['GET', 'POST'])
def myPhotoShow():
    cont = {}
    cont = verify(request)
    if cont['In']:
        return render_template('myPhotoShow.html')
    else:
        return redirect(url_for('login'))


# 个人信息
@app.route('/myMes', methods=['GET', 'POST'])
def myMes():
    cont = {}
    cont = verify(request)
    if cont['In']:
        return render_template('myMes.html', cont=cont)
    else:
        return redirect(url_for('login'))


# 个人信息修改
@app.route('/vMyMes', methods=['GET', 'POST'])
def vMyMes():
    cont = {}
    cont = verify(request)

    if 'v' in request.args:
        cont['v'] = request.args.get('v')
    if cont['In']:
        if request.method == 'POST':
            if 'name' in request.form:
                cont['name'] = request.form['name']
                cont['email'] = request.form['email']
                cont['phone'] = request.form['phone']
            if 'password' in request.form:
                if request.form['password'] == cont['password'] and request.form['npassword'] == request.form[
                    'npassword2']:
                    cont['password'] = request.form['npassword']
            back.nowMod(cont)
            return redirect(url_for('myMes'))
        else:
            if 'v' in request.args:
                cont['v'] = cont['t'] = request.args['v']
                return render_template('vMyMes.html', cont=cont)
            else:
                return redirect(url_for('myMes'))
    else:
        return redirect(url_for('login'))


# 计划系统
@app.route('/plan', methods=['GET', 'POST'])
def plan():
    cont = {}
    cont = verify(request)
    if cont['In']:
        return 'render_template('')'


# 黄金系统
# 股票系统
@app.route('/ace', methods=['GET', 'POST'])
@app.route('/sto', methods=['GET', 'POST'])
@app.route('/gold', methods=['GET', 'POST'])
def ace():
    cont = {}
    cont = verify(request)
    tr1, tr2 = goldCode.goldVariety()
    cont['dat'] = {
        'name': '',
        'task': 0,
        'mes': 0,
        'emailMes': 0,
        'profit': 1,
        'operation': 1,
        'product': 1,
        'oldproduct': 1,
        'nowOperation': 1,
        'hand': 1,
        'oldhand': 1,
        'totalValue': 1,
        'inTotalValue': 1,
        'nowTotalValue': 1,
        'goalTotalValue': 1,
        'zjzzst': '',
        'hjlatestpri': goldCode.goldvol(),
        'hjopenpri': goldCode.goldvol(a='openpri', variety='Au100g'),
        'hjmaxpri': goldCode.goldvol(a='maxpri', variety='Au100g'),
        'hjminpri': goldCode.goldvol(a='minpri', variety='Au100g'),
        'hjpz': tr1,
        'hjpzjg': tr2,
        'gplatestpri': '',
        'gpopenpri': '',
        'gpmaxpri': '',
        'gpminpri': '',
        'gppz': '',
        'gppzjg': ''}
    if cont['In']:
        if request.method == 'POST':
            select = request.args.get('goldSelect')
            cont.dat['name'] = select
            cont['dat']['hjlatestpri'] = goldCode.goldvol(a='latestpri', variety=select)
            cont['dat']['hjopenpri'] = goldCode.goldvol(a='openpri', variety=select)
            cont['dat']['hjmaxpri'] = goldCode.goldvol(a='maxpri', variety=select)
            cont['dat']['hjminpri'] = goldCode.goldvol(a='minpri', variety=select)
            return render_template('ace.html', cont=cont)
        return render_template('ace.html', cont=cont)
    else:
        return redirect(url_for('login'))


# 退出
@app.route('/cls', methods=['GET', 'POST'])
def cls():
    back.login(request.cookies.get('user'))
    resp = make_response(redirect(url_for('login')))
    resp.delete_cookie('ran')
    return resp


# BOM模板
@app.route('/dowb')
def dowb():
    pp.excelBomOut()
    # fp = os.getcwd()+'/files'
    return send_from_directory(fp, 'BOM导入模板.xlsx')
    return redirect(url_for('plan'))


# 盘点模板
@app.route('/dowc')
def dowc():
    pp.excelCheckOut()
    # fp = os.getcwd() + '/files'
    return send_from_directory(fp, '盘点导入模板.xlsx')
    return redirect(url_for('plan'))


# BOM上传
@app.route('/upload')
def upload():
    if request.method == 'POST':
        bom = request.files.get('bom')
        check = request.files.get('check')
        bom.sava(fp + '\\bom.xlsx')
        check.sava(fp + '\\check.xlsx')

        pp.excelIn(fp + '\\check.xlsx')
        conts = {}
        conts['fileName'] = fp + '\\bom.xlsx'
        pp.bomIn(conts)
        return render_template('upload.html')
    else:
        return render_template('upload.html')


# 运行
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
