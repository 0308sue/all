<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>MongoDB Insert</h2>
	<form action="insert" method="post">
		empno:<input type="text" name="empno"/><br/>
		ename:<input type="text" name="ename"/><br/>
		job:<input type="text" name="job"/><br/>
		deptno:<input type="text" name="deptno"/><br/>
		<input type="submit" value="추가" >
		<input type="reset" value="취소" >
		<input type="button" value="리스트" onclick="location.href='list'">
	</form>
</body>
</html>