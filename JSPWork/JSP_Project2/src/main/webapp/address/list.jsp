<%@page import="com.address.Address"%>
<%@page import="java.util.ArrayList"%>
<%@page import="com.address.AddressDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
<script>
function searchCheck() {
	if(document.getElementById("word").value==""){
		alert("검색어를 입력하세요");
		document.getElementById("word").focus();
		return;
	}
	document.getElementById("sfrm").submit();
}
</script>
<%
request.setCharacterEncoding("utf-8");
String field ="";
String word="";
if(request.getParameter("word")!=null){
	field = request.getParameter("field");
	word = request.getParameter("word");
}
AddressDAO dao = AddressDAO.getInstance();
ArrayList<Address> arr =dao.addrList(field,word);
int count = dao.getCount(field,word);
%>
</head>
<body>

<div class="container">
<div align="right">
<a href="insert.jsp"> 추가하기
/<a href="list.jsp"> 전체보기</a><br><br>
</div>

<h2>전체보기(<%= count %>)</h2>
	<table class="table table-hover">
	<thead>
		<tr>
			<th>번호</th>
			<th>이름</th>
			<th>주소</th>
			<th>전화번호</th>
		</tr>
	</thead>
	<%
	for(Address a:arr){
		%>
	<tbody>	
		<tr>
			<td><%= a.getNum() %></td>
			<td><a href="detail.jsp?num=<%= a.getNum() %>"> <%= a.getName() %></a></td>
			<td><%= a.getAddr() %></td>
			<td><%= a.getTel() %></td>
		</tr>
		</tr>
		<%
		}
		%>
	</tbody>
	</table>
	<form action="list.jsp" id="sfrm">
	<select name="field">
	<option value="name">이름</option>
	<option value="tel">전화번호</option>
	</select>
	<input type="text" name="word" id="word">
	<input type="button" value="검색" onclick="searchCheck()">
	</form>
</div>
</body>
</html>