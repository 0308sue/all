<%@page import="com.board.dto.CommentDTO"%>
<%@page import="com.board.dao.BoardDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
request.setCharacterEncoding("utf-8");
String msg = request.getParameter("msg");
int bnum = Integer.parseInt(request.getParameter("bnum"));
String sid = (String)session.getAttribute("sUserid");
if(sid == null){
	out.println("1");
}else{
BoardDAO dao = BoardDAO.getInstance();
CommentDTO comment = new  CommentDTO();
comment.setBnum(bnum);
comment.setMsg(msg);
comment.setUserid(sid);
dao.commentInsert(comment);

}
%>