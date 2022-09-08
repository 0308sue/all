<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
$(document).ready(function () {
	$("#getBtn").on("click",function(){
		$.get("process.jsp",
			{
			"id":$("#id").val(),
			"pwd":$("#pwd").val(),
			"method":"get"			
		}
		)
		.done(function(resp){
			$("#result").html(resp);
		})
	})
	$("#postBtn").on("click",function(){
		const test=$.post("process.jsp",
			{
			"id":$("#id").val(),
			"pwd":$("#pwd").val(),
			"method":"postBtn"			
		})
		test.done(function(resp){
			$("#result1").html(resp);
			})
		})
	
	
})
</script>
</head>
<body>

id :<input type="text" name="id" id="id"> <br>
pwd : <input type="password" name="pwd" id="pwd"> <br>

<button type="button" id="getBtn">get전송</button>
<button type="button" id="postBtn">post전송</button>
<button type="button" id="ajaxBtn">ajax전송</button>
<hr>
<div id="result"></div>
<div id="result1"></div>
</body>
</html>