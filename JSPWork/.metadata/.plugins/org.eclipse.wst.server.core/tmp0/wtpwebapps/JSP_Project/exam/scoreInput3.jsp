<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script >
function check() {
	if(document.getElementById("name").value==""){
		alert("이름을 입력하세요");
		return false;
	}
	if(document.getElementById("kor").value==""||isNaN(document.getElementById("kor").value)){
		alert("숫자로 국어 점수를 입력하세요");
		return false;
	}
	if(document.getElementById("eng").value==""||isNaN(document.getElementById("eng").value)){
		alert("숫자로 영어 점수를 입력하세요");
		return false;
	}
	if(document.getElementById("math").value==""||isNaN(document.getElementById("math").value)){
		alert("숫자로 수학 점수를 입력하세요");
		return false;
	}
	return true;
}
</script>
</head>
<body>
<form action="scoreResult.jsp" onsubmit="return check()">
이름 : <input type="text" name = "name" id ="name"><br/>
국어 : <input type="text" name = "kor" id ="kor"><br/>
영어 : <input type="text" name = "eng" id ="eng"><br/>
수학 : <input type="text" name = "math" id ="math"><br/>

<input type="submit" value="submit전송"/>
<input type="button" value="Button"/>

</form>
</body>
</html>