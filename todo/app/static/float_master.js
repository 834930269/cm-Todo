var draggingObj=null; //dragging Dialog
var diffX=0;
var diffY=0;
var temp=null;
//绑定鼠标事件
function dragging(obj) {
	temp = obj;
	obj.style.position='fixed';
	document.addEventListener("mousedown", mouseDown);
	document.addEventListener("mousemove", mouseMove);
	document.addEventListener("mouseup", mouseUp);
}
//是否点击的是指定div
function getDraggingDialog(e){
	var target=e.target;
	while (target != undefined && target != null && target.tagName.toUpperCase() != 'BODY'){ 
	if (target == temp){ 
		return true; 
	} 
		target = target.parentNode; 
	} 
	return false; 
}

function mouseDown(e) 
{
	if(getDraggingDialog(e)){
		draggingObj = temp;
	};
	
	if(draggingObj!=null){
		diffX=e.clientX-draggingObj.offsetLeft;
		diffY=e.clientY-draggingObj.offsetTop;
	}
				
}
function mouseMove(e) 
{
	if(draggingObj){
		draggingObj.style.left=(e.clientX-diffX)+'px';
		draggingObj.style.top=(e.clientY-diffY)+'px';
	}
}
function mouseUp() 
{
	draggingObj =null;
	diffX=0;
	diffY=0;
}

//js 创建浮动div
function createFloatDiv() {
	var div = document.getElementById("dlgTest");
	if(div==null||div==undefined) {
		var body = document.getElementsByTagName("body")[0];
		body.innerHTML = body.innerHTML+"<div id='dlgTest' style='top: 120px;right: 50px;height:100px; width:120px;background:url(/static/images/SF2.jpg);border-radius:9px;background-size:cover;'>"+
							"<h1 style='font-size: 15px;font-family: fantasy;color:#000'>欢迎来到地平线~</h1></div>"+"</div>";
	}
	div = document.getElementById("dlgTest");		
	dragging(div);
}