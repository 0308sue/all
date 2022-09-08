<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script >
$(document).ready(function(){
	$("#send").click(function () {
		$.getJSON("zipProcess.jsp",
				{"dong":$("#dong").val()},
				function(resp) {
					var str = "<table>"
					$.each(resp,function(key,val){
						str += "<tr>"
						str += "<td>"+val.zipcode+"</td>"
						str += "<td>"+val.sido+"</td>"
						str += "<td>"+val.gugun+"</td>"
						str += "<td>"+val.dong+"</td>"
						str += "<td>"+val.bunji+"</td>"
						
						str += "</tr>"
					})
					var str = "<table>"
					$("#result").html(str);
				})
		
	})
	$("#result").on("click","tr",function(){
		var address =$("td:eq(1)",this).text()+" "+
		$("td:eq(2)",this).text()+" "+
		$("td:eq(3)",this).text()+" "+
		$("td:eq(4)",this).text();
		$(opener.document).find("#zipcode").val($("td:eq(0)",this).text());
		$(opener.document).find("#addr").val(address);
		self.close();
	})
})
</script>
</head>
<body>
<table>
		<tr>
			<td>동이름 입력 : <input type="text" name="dong" id="dong" />
			<input type="button" value="검색" id="send"/>
			</td>
		</tr>
</table>
<div id="result"></div>
</body>
</html>