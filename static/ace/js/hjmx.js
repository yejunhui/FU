var gyyz= document.getElementById("hjyyz").getContext("2d");
var gyyzr= document.getElementById("hjyyz").getContext("2d");
var gyyzb= document.getElementById("hjyyz").getContext("2d");
var gpz= document.getElementById("hjpz").getContext("2d");

var yyzl= document.getElementById("hjlatestpri").value.replace("\"","").split(",");
var yyzo= document.getElementById("hjopenpri").value.replace("\"","").split(",");
var yyzx= document.getElementById("hjmaxpri").value.replace("\"","").split(",");
var yyzn= document.getElementById("hjminpri").value.replace("\"","").split(",");
var hjpz= document.getElementById("hjd").value.replace("\"","").split(",");
var hjzpjg= document.getElementById("hjpzjg").value.replace("\"","").split(",");

//document.getElementById("totalzstdata").innerHTML=y;
//最大值
var max= 400;
//纵/横坐标单位长度
var dw= (1000-20)/(980)*100;
var dwx= (1640-30)/24/3;
//y总长
var maxy= 35500;

gyyz.moveTo(20,10);
gyyz.lineTo(20,980);
gyyz.lineTo(1630,980);
//黄金阴阳烛
for(var i=0;i<yyzl.length;i++){

    if(yyzl[i] > yyzo[i]){
        gyyz.moveTo(dwx/2+20+i*dwx,maxy-yyzn[i]*dw);
        gyyz.fillText(yyzn[i],dwx/2+20+i*dwx,maxy-yyzn[i]*dw)
        gyyz.lineTo(dwx/2+20+i*dwx,maxy-yyzo[i]*dw);
        gyyz.fillText(yyzo[i],dwx/2+20+i*dwx,maxy-yyzo[i]*dw)
        gyyz.fillStyle="red";
        gyyz.fillRect(20+i*dwx,maxy-yyzl[i]*dw,dwx,(yyzl[i]-yyzo[i])*dw);
        gyyz.fillStyle="black";
        gyyz.moveTo(dwx/2+20+i*dwx,maxy-yyzx[i]*dw);
        gyyz.fillText(yyzx[i],dwx/2+20+i*dwx,maxy-yyzx[i]*dw)
        gyyz.lineTo(dwx/2+20+i*dwx,maxy-yyzl[i]*dw);
        gyyz.fillText(yyzl[i],dwx/2+20+i*dwx,maxy-yyzl[i]*dw)
    }
    else{
        gyyz.moveTo(dwx/2+20+i*dwx,maxy-yyzn[i]*dw);
        gyyz.fillText(yyzn[i],dwx/2+20+i*dwx,maxy-yyzn[i]*dw)
        gyyz.lineTo(dwx/2+20+i*dwx,maxy-yyzl[i]*dw);
        gyyz.fillText(yyzl[i],dwx/2+20+i*dwx,maxy-yyzl[i]*dw)
        gyyz.fillStyle="blue";
        gyyz.fillRect(20+i*dwx,maxy-yyzl[i]*dw,dwx,(yyzl[i]-yyzo[i])*dw);
        gyyz.fillStyle="black";
        gyyz.moveTo(dwx/2+20+i*dwx,maxy-yyzx[i]*dw);
        gyyz.fillText(yyzx[i],dwx/2+20+i*dwx,maxy-yyzx[i]*dw)
        gyyz.lineTo(dwx/2+20+i*dwx,maxy-yyzo[i]*dw);
        gyyz.fillText(yyzo[i],dwx/2+20+i*dwx,maxy-yyzo[i]*dw)
    }
//    gyyz.fillRect(20+i*dwx,980-yyzl[i]*dw,dwx,(yyzl[i]-yyzo[i])*dw);
//    gyyz.fillStyle="black";
//    gyyz.moveTo(dwx/2+20+i*dwx,980-yyzx[i]*dw);
//    gyyz.lineTo(dwx/2+20+i*dwx,980-yyzl[i]*dw);


}
if (yyzl[yyzl.length-2]>yyzo[yyzo.length-2]){
    gyyz.fillStyle="red";
    gyyz.fillText('最低价：',80,10);
    gyyz.fillText(yyzn[yyzn.length-2],110,10);
    gyyz.fillText('开盘价：',160,10);
    gyyz.fillText(yyzo[yyzo.length-2],190,10);
    gyyz.fillText('最高价：',240,10);
    gyyz.fillText(yyzx[yyzx.length-2],270,10);
    gyyz.fillText('现在价：',320,10);
    gyyz.fillText(yyzl[yyzl.length-2],350,10);
    gyyz.fillStyle="black";
}
else{
    gyyz.fillStyle="bule";
    gyyz.fillText('最低价：',80,10);
    gyyz.fillText(yyzn[yyzn.length-2],110,10);
    gyyz.fillText('开盘价：',160,10);
    gyyz.fillText(yyzo[yyzo.length-2],190,10);
    gyyz.fillText('最高价：',240,10);
    gyyz.fillText(yyzx[yyzx.length-2],270,10);
    gyyz.fillText('现在价：',320,10);
    gyyz.fillText(yyzl[yyzl.length-2],350,10);
    gyyz.fillStyle="black";
}

//黄金折线
gpz.moveTo(20,maxy-yyzl[0]*dw);
for(var i=0;i<yyzl.length-1;i++){
    gpz.lineTo(20+i*dwx,maxy-yyzl[i]*dw);
    gpz.fillText(yyzl[i],20+i*dwx,maxy-yyzl[i]*dw)
}

//坐标标记
gyyz.stroke();
gpz.stroke();
gyyz.textAlign="right";
//gyyz.fillText(370,20,10);
for(var i=0;i<50;i++){
    gyyz.fillText(366-i*0.6,20,10+i*20)
}
//gyyz.fillText(980/2,20,970/2);
gyyz.fillText('0',20,990);
gyyz.fillText('12H',1630/2,990);
gyyz.fillText('24H',1630,990);

gpz.textAlign="right";
//gpz.fillText(370,20,10);
for(var i=0;i<50;i++){
    gpz.fillText(366-i*0.6,20,10+i*20)
}
//gpz.fillText(980/2,20,970/2);
gpz.fillText('0',20,990);
gpz.fillText(hjpzjg,820,990)
for(var i=0;i<hjd.length;i++){
    gpz.fillText(hjd[i],20+dwx/2+i*dwx,990)
}
//gpz.fillText(hjpzjg,1630/2,990);
//gpz.fillText('24H',1630,990);
if (yyzl[yyzl.length-2]>yyzo[yyzo.length-2]){
    gpz.fillStyle="red";
    gpz.fillText('最低价：',80,10);
    gpz.fillText(yyzn[yyzn.length-2],110,10);
    gpz.fillText('开盘价：',160,10);
    gpz.fillText(yyzo[yyzo.length-2],190,10);
    gpz.fillText('最高价：',240,10);
    gpz.fillText(yyzx[yyzx.length-2],270,10);
    gpz.fillText('现在价：',320,10);
    gpz.fillText(yyzl[yyzl.length-2],350,10);
    gpz.fillStyle="black";
}
else{
    gpz.fillStyle="bule";
    gpz.fillText('最低价：',80,10);
    gpz.fillText(yyzn[yyzn.length-2],110,10);
    gpz.fillText('开盘价：',160,10);
    gpz.fillText(yyzo[yyzo.length-2],190,10);
    gpz.fillText('最高价：',240,10);
    gpz.fillText(yyzx[yyzx.length-2],270,10);
    gpz.fillText('现在价：',320,10);
    gpz.fillText(yyzl[yyzl.length-2],350,10);
    gpz.fillStyle="black";
}
