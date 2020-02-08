var c= document.getElementById("hjzst").getContext("2d");

var yyzl= document.getElementById("hjlatestpri").value.replace("\"","").split(",");

//document.getElementById("totalzstdata").innerHTML=y;
//最大值
var max= 400;
//纵/横坐标单位长度
var dw= 10;
var dwx= 1;
//y总长
var maxy= 3800;

//画X，Y坐标
c.textAlign='right';
c.moveTo(20,10);
c.lineTo(20,470);
c.lineTo(700,470);

c.moveTo(20,maxy-yyzl[0]*dw);
for(var i=0;i<yyzl.length-1;i++){
    c.lineTo(20+i*dwx,maxy-yyzl[i]*dw);
    //c.fillText(yyzl[i],20+i*dwx,maxy-yyzl[i]*dw)
}

c.stroke();

c.textAlign="right";
c.fillText(max*2,48,10);
c.fillText(max,30,450/2);
c.fillText('0',30,480);
c.fillText('0.5',670/2+30,480);
c.fillText('1',700,480);