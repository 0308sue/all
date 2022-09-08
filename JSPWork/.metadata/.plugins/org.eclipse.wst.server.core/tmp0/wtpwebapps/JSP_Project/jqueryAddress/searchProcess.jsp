<%@page import="org.json.simple.JSONObject"%>
<%@page import="org.json.simple.JSONArray"%>
<%@page import="com.jqueryAddress.AddressVO"%>
<%@page import="java.util.ArrayList"%>
<%@page import="com.jqueryAddress.JAddressDAOImpl"%>
<%@page import="com.jqueryAddress.JAddressDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
request.setCharacterEncoding("UTF-8");
String field = request.getParameter("field");
String word = request.getParameter("word");
JAddressDAO dao = JAddressDAOImpl.getInstance();
ArrayList<AddressVO> sarr = dao.searchlist(field, word);
int count = dao.getCount(field,word);
//sarr(java) ---> JSON
JSONArray jarr = new JSONArray();
for(AddressVO avo : sarr){
	JSONObject obj = new JSONObject();
	obj.put("num",avo.getNum());
	obj.put("name",avo.getName());
	obj.put("zipcode",avo.getZipcode());
	obj.put("addr",avo.getAddr());
	obj.put("tel",avo.getTel());
	jarr.add(obj);
}
//count(java) ---> JSON
JSONObject countObj = new JSONObject();
countObj.put("count",count);

JSONObject mainObj = new JSONObject();
mainObj.put("jarrobj", jarr);
mainObj.put("countObj", countObj);

out.println(mainObj.toJSONString());
%>
