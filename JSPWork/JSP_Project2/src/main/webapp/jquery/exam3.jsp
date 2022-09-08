<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
$(document).ready(function() {
	$("#getBtn").click(function() {
		$.get("process.jsp",
				{
					"id":$("#id").val(),
					"pwd":$("#pwd").val(),
					"method":"get"
				},
				function(resp) {
					//alert(resp)
					$("#result").html(resp);
				}
				
		)
	});
/*	
	$("#postBtn").click(function() {
		$.post("process.jsp",
				{
					"id":$("#id").val(),
					"pwd":$("#pwd").val(),
					"method":"post"
				},
				function(resp) {
					//alert(resp)
					$("#result").html(resp);
				}
				
		);
	});
	*/
	$("#postBtn").on("click",function(){
		$.post("process.jsp",
			{
				id : $("#id").val(),
				pwd:$("#pwd").val(),
				method:"postpost"
			},
			function(res) {
				//alert(resp)
				$("#result").html(res);
	})
	
});
	
	$("#ajaxBtn").on("click",function(){
		$.ajax({
			type : "ajax",
			url : "process.jsp",
			data : {
				id : $("#id").val(),
				pwd:$("#pwd").val(),
				method:"ajax"
			},
			success:function(resp){
				$("#result").html(res);
			},
			error : function (e) {
				alert(e+"error")
			}
		})
		
	})
	
	$("#ajaxBtn_on").on("click",function(){
		$.ajax({
				type : "get",
				url : "process.jsp",
				data : {
				id : $("#id").val(),
				pwd:$("#pwd").val(),
				method:"ajaxajax"
				},
				success:function(resp){
					$("#result").html(res);
				},
				error : function (e) {
					alert(e+"error")
				}
		})
	})
	
	
});
</script>
</head>
<body>

id :<input type="text" name="id" id="id"> <br>
pwd : <input type="password" name="pwd" id="pwd"> <br>

<button type="button" id="getBtn">get전송</button>
<button type="button" id="postBtn">post전송</button>
<button type="button" id="ajaxBtn">ajax전송</button>
<button type="button" id="ajaxBtn_on">ajax_on전송</button>

<hr>
<div id="result"></div>
</body>
</html>