import os

from flask import Flask,render_template,url_for,request,redirect,make_response,flash,send_from_directory
from random import randint
import time
import d
import pmysql
import back
import files
import plan as pp

app = Flask(__name__)

fp = os.getcwd() + '/files'

def verify(request):
    if 'ran' in request.cookies:
        uc = request.cookies.get('user')
        pc = request.cookies.get('password')
        ran = request.cookies.get('ran')
        cont = back.indexVerify(ran)
        cont['uc']=uc
        cont['pc']=pc
        return cont
    else:
        return ''

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')


@app.route('/loginUp',methods=['GET','POST'])
def loginUp():
        return render_template('loginUp.html')


@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/myFamily',methods=['GET','POST'])
def myFamily():
    return render_template('myfamilyhome.html')


@app.route('/myPhotoShow',methods=['GET','POST'])
def myPhotoShow():
    return render_template('myPhotoShow.html')


#退出
@app.route('/cls',methods=['GET','POST'])
def cls():
    back.login(request.cookies.get('user'))
    resp = make_response(redirect(url_for('login')))
    resp.delete_cookie('ran')
    return resp

#BOM模板
@app.route('/dowb')
def dowb():
    pp.excelBomOut()
    #fp = os.getcwd()+'/files'
    return send_from_directory(fp,'BOM导入模板.xlsx')
    return redirect(url_for('plan'))

#盘点模板
@app.route('/dowc')
def dowc():
    pp.excelCheckOut()
    #fp = os.getcwd() + '/files'
    return send_from_directory(fp, '盘点导入模板.xlsx')
    return redirect(url_for('plan'))

#BOM上传
@app.route('/upload')
def upload():
    if request.method == 'POST':
        bom= request.files.get('bom')
        check= request.files.get('check')
        bom.sava(fp+'\\bom.xlsx')
        check.sava(fp+'\\check.xlsx')

        pp.excelIn(fp+'\\check.xlsx')
        conts = {}
        conts['fileName']=fp+'\\bom.xlsx'
        pp.bomIn(conts)
        return render_template('upload.html')
    else:
        return render_template('upload.html')


#运行
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)