<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

</head>
<!-- 왼 -->
<nav class="navbar navbar-expand-sm bg-secondary navbar-dark mb-5">
<div class="container">
  <!-- Links -->
  <ul class="navbar-nav mr-auto">
    <li class="nav-item">
      <a class="nav-link" href="/app08/">HOME</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="/app08/insert">글쓰기</a>
    </li> 
  </ul>
  
  <ul class="navbar-nav">
<c:choose>
<c:when test="${empty sessionScope.sMember }">
 <li class="nav-item">
      <a class="nav-link" href="/app08/member/join">회원가입</a>
    </li> 
     <li class="nav-item">
      <a class="nav-link" href="/app08/member/login">로그인</a>
    </li>
</c:when>
<c:otherwise>
 <li class="nav-item">
      <a class="navbar-brand" href="/app08/member/logout">(${sessionScope.sMember.name})로그아웃</a>
    </li>
</c:otherwise>
</c:choose>

 
    
  </ul>
</div>
</nav>