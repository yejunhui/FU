var gyyz= document.getElementById("gpyyz").getContext("2d");
var gpz= document.getElementById("gppz").getContext("2d");

var yyzl= document.getElementById("gplatestpri").value.replace("\"","").split(",");
var yyzo= document.getElementById("gpopenpri").value.replace("\"","").split(",");
var yyzx= document.getElementById("gpmaxpri").value.replace("\"","").split(",");
var yyzn= document.getElementById("gpminpri").value.replace("\"","").split(",");

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
for(var i=0;i<yyzl.length;i++){

    if(yyzl[i] > yyzo[i]){
        gyyz.moveTo(dwx/2+20+i*dwx,maxy-yyzn[i]*dw);
        gyyz.lineTo(dwx/2+20+i*dwx,maxy-yyzo[i]*dw);
        gyyz.fillStyle="red";
        gyyz.fillRect(20+i*dwx,maxy-yyzl[i]*dw,dwx,(yyzl[i]-yyzo[i])*dw);
        gyyz.fillStyle="black";
        gyyz.moveTo(dwx/2+20+i*dwx,maxy-yyzx[i]*dw);
        gyyz.lineTo(dwx/2+20+i*dwx,maxy-yyzl[i]*dw);
    }
    else{
        gyyz.moveTo(dwx/2+20+i*dwx,maxy-yyzn[i]*dw);
        gyyz.lineTo(dwx/2+20+i*dwx,maxy-yyzl[i]*dw);
        gyyz.fillStyle="blue";
        gyyz.fillRect(20+i*dwx,maxy-yyzl[i]*dw,dwx,(yyzl[i]-yyzo[i])*dw);
        gyyz.fillStyle="black";
        gyyz.moveTo(dwx/2+20+i*dwx,maxy-yyzx[i]*dw);
        gyyz.lineTo(dwx/2+20+i*dwx,maxy-yyzo[i]*dw);
    }
//    gyyz.fillRect(20+i*dwx,980-yyzl[i]*dw,dwx,(yyzl[i]-yyzo[i])*dw);
//    gyyz.fillStyle="black";
//    gyyz.moveTo(dwx/2+20+i*dwx,980-yyzx[i]*dw);
//    gyyz.lineTo(dwx/2+20+i*dwx,980-yyzl[i]*dw);


}

gpz.moveTo(20,10);
gpz.lineTo(20,980);
gpz.lineTo(1630,980);
gpz.moveTo(20,maxy-yyzl[0]*dw);
for(var i=1;i<yyzl.length;i++){
    gpz.lineTo(20+i*dwx*5,maxy-yyzl[i]*dw);
}

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
gpz.fillText('12H',1630/2,990);
gpz.fillText('24H',1630,990);