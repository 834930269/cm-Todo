// 在组件 updated 、窗口重载和尺寸改变时，修改 memo 样式
const resizeMemos = () => {
  let memoWidth = $('.memo').eq(0).width();
  $('.memo').height(memoWidth + 65);
  $('.memo .content').width(memoWidth).height(memoWidth);
};
// 检测是否移动端
const ua = window.navigator.userAgent;
window.isMobile =
  /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Windows Mobile|UCWeb/i.test(ua)
  ? true
  : false;

// 是的话，限制 vue-memo 元素，使溢出滚动
if (window.isMobile) {
  $('#vue-memo')
    .height(window.innerHeight - 60)
    .css('overflow', 'scroll');
}

// 调整所有 memo 的尺寸以响应浏览器
$(window).on('resize', () => {
  helpers.resizeMemos();
});


		let canvasEle = $('.doodle-content')[0];
        let colorsEle = $('.doodle-colors')[0];
        let controllersEle = $('.doodle-controllers')[0];
        initCanvas(canvasEle, colorsEle, controllersEle, null);
		$(function(){
			$('#btn2').click(function(){
				let cav=document.getElementById('cv');
				let image=cav.toDataURL('image/jpeg');
				let title=$('#tt2').val();
				let category=$('#usertype2').val();
				$.post('/upload',{'data':image,'title':title,'category':category},function(result){
					window.location.href=result;
				})
			})
			$('#btn4').click(function(){
				let cav=document.getElementById('cv2');
				let image=cav.toDataURL('image/jpeg');
				let title=$('#tt4').val();
				let id=$(this).attr('reg');
				console.log(id);
				let category=$('#usertype4').val();
				$.post('/update-canvas',{'data':image,'title':title,'category':category,'id':id},function(result){
					window.location.href=result;
				})
			})
			$('#btn3').click(function(){
				let text=$('#ct2').val();
				let title=$('#tt3').val();
				let id=$(this).attr('reg');
				let category=$('#usertype3').val();
				$.post('/update-markdown',{'text':text,'title':title,'category':category,'id':id},function(result){
					window.location.href=result;
				})
			})
			$('#btn1').click(function(){
				let text=$('#ct').val();
				let title=$('#tt1').val();
				let category=$('#usertype1').val();
				$.post('/create-content',{'text':text,'title':title,'category':category},function(result){
					window.location.href=result;
				})
			})
		})
		$('#update-canvas').on('show.bs.modal',function(event){
			console.log("IN");
			let origin = $(event.relatedTarget);
			let id = origin.data('id');
			let title = origin.data('title');
			let imgurl = origin.data('imgurl');
			let category = origin.data('category');
			console.log(imgurl);
			let modal = $(this);
			modal.find('#tt4').val(title);
			modal.find('#usertype4').val(category);
			
			let canvasEle = $('#cv2')[0];
			let colorsEle = $('#cc2')[0];
			let controllersEle = $('#cl2')[0];
			initCanvas(canvasEle, colorsEle, controllersEle, imgurl);
			
			modal.find('#btn4').attr("reg",id);
		})
		$('#update-markdown').on('show.bs.modal',function(event){
			let origin = $(event.relatedTarget);
			let id = origin.data('id');
			let title = origin.data('title');
			let content_text = origin.data('ct');
			let category = origin.data('category');
			let modal = $(this);
			modal.find('#tt3').val(title);
			modal.find('#usertype3').val(category);
			modal.find('#ct2').val(content_text);
			modal.find('#btn3').attr("reg",id);
		})