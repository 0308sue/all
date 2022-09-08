<%@page import="com.exam.FormBean"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">
<title>Insert title here</title>
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="fb" class ="com.exam.FormBean"></jsp:useBean>
<jsp:setProperty property="*" name="fb"/>
</head>
<% 
String[] h = fb.getHobby();
String tmp="";
for(int i=0;i<h.length;i++){
tmp +=h[i] + " ";
}
%>

<body>

이름 : <jsp:getProperty property="name" name="fb"/>
나이 : <jsp:getProperty property="age" name="fb"/>

이름 :<%=fb.getName() %> <br/>

나이 :<%=fb.getAge() %> <br/>

성별 :<%=fb.getGender() %> <br/>

관심분야 :<%=tmp %> <br/>

직업 :<%=fb.getJob() %>
</body>
</html>