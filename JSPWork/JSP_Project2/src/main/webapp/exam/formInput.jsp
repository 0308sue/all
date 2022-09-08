<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script>
function check(){
	if(document.getElementById("name").value == ""){
		alert("이름을 입력하세요");
		return;
	}
	if(document.getElementById("age").value == ""){
		alert("나이를 입력하세요");
		return;
	}
	var chk_obj = document.getElementsByName("hobby");
	var checked = 0;
		for (i=0;i<chk_obj.length;i++){
			if(chk_obj[i].checked){
				checked +=1;
				
			}
		}
		if(checked ==0){
		alert("관심분야를 선택하세요");
		return;
	}
	document.getElementById("frm").submit();
}
</script>
</head>
<body>
<form action="formResult.jsp" method="get" id = "frm">
이름 : <input type="text" name = "name" id = "name"><br/>
나이 : <input type="text" name = "age" id = "age"><br/>

성별 : 
<label for="m">남자</label><input type="radio" value = "남" id = "m" name ="gender" checked> 
<label for="f">여자</label><input type="radio" value = "여" id = "f" name ="gender"> <br/>

관심분야 : 
<label for="h1">운동 </label> <input type="checkbox" name="hobby" value="운동" id="h1">
<label for="h2">게임</label> <input type="checkbox" name="hobby" value="게임" id="h2">
<label for="h3">등산</label> <input type="checkbox" name="hobby" value="등산" id="h3">
<label for="h4">영화 </label><input type="checkbox" name="hobby" value="영화" id="h4"><br/>

직업 : 
<select name="job">
<option value="학생">학생</option>
<option value="직장인">직장인</option>
<option value="자영업자">자영업자</option>
<option value="무직">무직</option>
</select><br/>
<!-- <input type="submit" value="전송"/> -->
<input type = "button" value = "클릭" onclick="check()">
</form>
</body>
</html>