<%@page import="com.jqueryAddress.JAddressDAOImpl"%>
<%@page import="com.jqueryAddress.JAddressDAO"%>
<%@page import="java.util.ArrayList"%>
<%@page import="com.jqueryAddress.AddressVO"%>
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
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<%
JAddressDAO dao = JAddressDAOImpl.getInstance();
ArrayList<AddressVO> jarr =  dao.list();
int count = dao.getCount();
%> 
</head>
<script>
$(document).ready(function(){
	$("#btnSearch").click(function () {
		$.ajax({
			type :"get",
			url : "searchProcess.jsp",
			data : {
				"field":$("#field").val(),
				"word":$("#word").val(),
			},
			success : function (resp) {
				var d = JSON.parse(resp);
				var str ="";
				$.each(d.jarrobj,function(key,val){
					str += "<tr>"
					str += "<td>"+val.num +"</td>"
					str += "<td><a href='addrDetail.jsp?num="+val.num+"'>"+val.name +"</a></td>"
					str += "<td>"+val.addr +"</td>"
					str += "<td>"+val.tel +"</td>"
					str += "</tr>"
				})
				$("table tbody").html(str);
				$("#cntSpan").text(d.countObj.count);
			},
			error : function (e) {
				alert("error : "+e);
			}
		})//aj
		
	})//bt
})//do
</script>
<body>

<div class="container">
<div align="right">
<a href="insert.jsp"> 추가하기
/<a href="addlist.jsp"> 전체보기</a><br><br>
</div>

<h2>Jquery Address 전체보기(<span id="cntSpan"><%= count %></span>)</h2>
	<table class="table table-hover">
	<thead>
		<tr>
			<th>번호</th>
			<th>이름</th>
			<th>주소</th>
			<th>전화번호</th>
		</tr>
	</thead>
	<tbody>	
	<%
	for(AddressVO a:jarr){
		%>

		<tr>
			<td><%= a.getNum() %></td>
			<td><a href="addrDetail.jsp?num=<%= a.getNum() %>"> <%= a.getName() %></a></td>
			<td><%= a.getAddr() %></td>
			<td><%= a.getTel() %></td>
		</tr>
		</tr>
		<%
		}
		%>
	</tbody>
	</table>
	<select name="field" id="field">
	<option value="name">이름</option>
	<option value="tel">전화번호</option>
	</select>
	<input type="text" name="word" id="word">
	<input type="button" value="검색" id="btnSearch">

</div>
</body>
</html>