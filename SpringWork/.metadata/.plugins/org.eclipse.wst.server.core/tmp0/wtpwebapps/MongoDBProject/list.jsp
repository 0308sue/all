<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>MongoDB List</h2>
<a href="insert">추가하기</a>
<table>
	<tr>
		<th>empno</th>
		<th>ename</th>
		<th>job</th>
		<th>hiredate</th>
		<th>deptno</th>
	</tr>
	<c:forEach items="${listemp }" var="emp">
		<tr>
			<td>${emp.empno}</td>
			<td>${emp.ename}</td>
			<td>${emp.job}</td>
			<td>${emp.hiredate}</td>
			<td>${emp.deptno}</td>
			<td><a href="update?empno=${emp.empno}">수정</a></td>
			<td><a href="delete?empno=${emp.empno}">삭제</a></td>
		</tr>
	</c:forEach>
</table>

</body>
</html>